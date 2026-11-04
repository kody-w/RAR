"""Local CSV charge checks, with no network code or bank sign-in."""
import calendar
import csv
import hashlib
import io
import json
import logging
import os
import re
import threading
from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0", "name": "@kody-w/money_watch_agent",
    "version": "1.0.0", "display_name": "Money Watch",
    "description": "Checks local bank exports for repeated charges, price rises and likely renewals.",
    "author": "kody-w", "tags": ["money", "csv", "local"],
    "category": "finance", "quality_tier": "community",
    "requires_env": [], "dependencies": ["@rapp/basic_agent"],
}

_LOCK = threading.RLock()
_HEADERS = {
    "date": ("transactiondate", "date", "posteddate", "postingdate", "postdate", "bookingdate"),
    "merchant": ("description", "merchant", "payee", "transactiondescription", "details", "name", "memo"),
    "amount": ("amount", "transactionamount", "total"),
    "debit": ("debit", "debits", "debitamount", "withdrawal", "withdrawals", "moneyout"),
    "credit": ("credit", "credits", "creditamount", "deposit", "deposits", "moneyin"),
    "type": ("type", "transactiontype", "debitcredit", "drcr", "creditdebitindicator"),
    "account": ("accountnumber", "account", "accountno", "cardnumber", "cardaccount"),
}
_PAYMENT = re.compile(r"\b(?:payment|thank\s+you|credit|refund)\b", re.I)


class CSVColumnsError(ValueError):
    """A required CSV column could not be identified without guessing."""


def money_dir():
    return Path(os.environ.get("MONEY_WATCH_DIR") or "~/.brainstem/money-watch").expanduser()


@contextmanager
def _locked():
    import fcntl
    with _LOCK:
        money_dir().mkdir(parents=True, exist_ok=True)
        with (money_dir() / ".lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            yield


def load_state():
    state = {"transactions": [], "told": [], "forgotten": []}
    path = money_dir() / "money.jsonl"
    if path.exists():
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                if line.strip():
                    state = json.loads(line)
    if not isinstance(state, dict) or any(not isinstance(state.get(key), list)
                                          for key in ("transactions", "told", "forgotten")):
        raise ValueError("The saved charge list is damaged")
    return state


def _save(state):
    with (money_dir() / "money.jsonl").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(state) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def _merchant(value):
    return " ".join(value.casefold().split())


def _amount(value):
    value = value.strip().replace(",", "").replace("$", "").replace("\u00a3", "").replace("\u20ac", "")
    if value.startswith("(") and value.endswith(")"):
        value = "-" + value[1:-1]
    try:
        number = Decimal(value)
    except InvalidOperation as error:
        raise ValueError("A charge amount is not a number") from error
    if not number.is_finite() or number != number.quantize(Decimal("0.01")):
        raise ValueError("A charge amount needs no more than two decimal places")
    return number


def _date(value):
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%m-%d-%Y",
                "%d %b %Y", "%d %B %Y", "%d-%b-%Y"):
        try:
            return datetime.strptime(value.strip(), fmt).date().isoformat()
        except ValueError:
            pass
    raise ValueError("A transaction date could not be read")


def _infer_columns(rows):
    columns = dict.fromkeys(_HEADERS)
    if not rows:
        return columns
    fields = list(rows[0])

    def all_parse(field, parser):
        try:
            for row in rows:
                parser(row[field])
            return True
        except ValueError:
            return False

    dates = [field for field in fields if all_parse(field, _date)]
    if len(dates) == 1:
        columns["date"] = dates[0]
    numbers = [field for field in fields if field not in dates and all_parse(field, _amount)]
    if len(numbers) > 1:
        marked = [field for field in numbers if any(
            re.search(r"[.+\-$\u00a3\u20ac()]", row[field]) for row in rows)]
        if len(marked) == 1:
            numbers = marked
    if len(numbers) == 1:
        columns["amount"] = numbers[0]
    text_fields = [field for field in fields if field not in dates
                   and not all_parse(field, _amount)
                   and all(any(char.isalpha() for char in row[field]) for row in rows)]
    if text_fields:
        columns["merchant"] = max(text_fields, key=lambda field: sum(len(row[field]) for row in rows))
    return columns


def _csv_rows(text):
    try:
        dialect = csv.Sniffer().sniff(text[:8192], delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    raw = [row for row in csv.reader(io.StringIO(text), dialect=dialect, strict=True)
           if any(value.strip() for value in row)]
    if not raw:
        raise CSVColumnsError("date, description, amount")
    width = len(raw[0])
    for number, row in enumerate(raw, 1):
        if len(row) != width:
            raise ValueError(f"Row {number} has missing or extra columns")
    normalized = {re.sub(r"[^a-z]", "", field.casefold()): str(i)
                  for i, field in enumerate(raw[0])}
    known_headers = {alias for aliases in _HEADERS.values() for alias in aliases}
    has_header = bool(known_headers.intersection(normalized))
    rows = [dict(zip(map(str, range(width)), row)) for row in (raw[1:] if has_header else raw)]
    if has_header:
        columns = {key: next((normalized[alias] for alias in aliases if alias in normalized), None)
                   for key, aliases in _HEADERS.items()}
    else:
        columns = _infer_columns(rows)
    missing = []
    for key, label in (("date", "date"), ("merchant", "description"), ("amount", "amount")):
        if columns[key] is None and not (key == "amount" and columns["debit"] is not None):
            missing.append(label)
    if missing:
        raise CSVColumnsError(", ".join(missing))
    if not rows:
        raise ValueError("The export has no transactions")
    return rows, columns, has_header and "cardmember" in normalized


def read_csv(path):
    text = Path(path).expanduser().read_text(encoding="utf-8-sig")
    rows, columns, card_export = _csv_rows(text)
    negative_charges = bool(columns["amount"] and any(
        _amount(row[columns["amount"]]) < 0 and not _PAYMENT.search(row[columns["merchant"]])
        for row in rows))
    signed = negative_charges and not card_export
    out = []
    for row in rows:
        merchant = _merchant(row[columns["merchant"]])
        if not merchant:
            raise ValueError("A transaction has no description")
        at = _date(row[columns["date"]])
        if columns["debit"]:
            value = row[columns["debit"]].strip()
            amount = abs(_amount(value)) if value else Decimal(0)
            credit = row[columns["credit"]].strip() if columns["credit"] else ""
            if credit and _amount(credit) and amount:
                raise ValueError("A transaction has both a debit and a credit")
        else:
            raw = _amount(row[columns["amount"]])
            kind = row[columns["type"]].strip().casefold() if columns["type"] else ""
            if raw < 0 and _PAYMENT.search(merchant):
                amount = Decimal(0)
            elif signed:
                amount = -raw
            elif card_export:
                amount = raw
            elif kind in {"credit", "cr", "crdt", "deposit", "payment", "refund", "income"}:
                amount = Decimal(0)
            elif kind in {"debit", "dr", "dbit", "purchase", "sale", "withdrawal", "charge"}:
                amount = abs(raw)
            else:
                amount = raw
        if amount > 0:
            item = {"date": at, "merchant": merchant, "amount": f"{amount:.2f}"}
            account = row[columns["account"]].strip().casefold() if columns["account"] else ""
            if account:
                item["account"] = account
            out.append(item)
    return out, ("debit and credit columns set the charge direction" if columns["debit"]
                 else "negative amounts are treated as charges" if signed
                 else "positive amounts are treated as charges unless marked as credits")


def _key(transaction):
    return (transaction["date"], transaction["merchant"], transaction["amount"], transaction.get("account", ""))


def _next(at, period):
    months = 1 if period == "monthly" else 12
    year, month = divmod(at.year * 12 + at.month - 1 + months, 12)
    month += 1
    return date(year, month, min(at.day, calendar.monthrange(year, month)[1]))


def findings(transactions, today=None):
    today = today or date.today()
    groups = defaultdict(list)
    for transaction in transactions:
        groups[(transaction["merchant"], transaction.get("account", ""))].append(transaction)
    results = []

    def add(kind, merchant, **fields):
        item = {"kind": kind, "merchant": merchant, **fields}
        item["id"] = hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest()
        results.append(item)

    for (merchant, account), charges in sorted(groups.items()):
        account_fields = {"account": account} if account else {}
        charges.sort(key=lambda item: (item["date"], Decimal(item["amount"])))
        duplicate_occurrences = Counter()
        for i, current in enumerate(charges):
            for previous in reversed(charges[:i]):
                gap = (date.fromisoformat(current["date"]) - date.fromisoformat(previous["date"])).days
                if gap > 3:
                    break
                if current["amount"] == previous["amount"]:
                    pair = (previous["date"], current["date"], current["amount"])
                    duplicate_occurrences[pair] += 1
                    add("duplicate", merchant, amount=current["amount"],
                        dates=[previous["date"], current["date"]], occurrence=duplicate_occurrences[pair], **account_fields)
        periods = []
        for i, current in enumerate(charges):
            # Same-week extra charges must not hide a monthly or yearly pattern.
            previous = next((old for old in reversed(charges[:i])
                             if (date.fromisoformat(current["date"]) -
                                 date.fromisoformat(old["date"])).days > 3), None)
            if not previous:
                continue
            gap = (date.fromisoformat(current["date"]) - date.fromisoformat(previous["date"])).days
            period = "monthly" if 26 <= gap <= 35 else "yearly" if 350 <= gap <= 380 else None
            if period:
                periods.append(period)
                if Decimal(current["amount"]) > Decimal(previous["amount"]):
                    add("price_rise", merchant, before=previous["amount"],
                        amount=current["amount"], date=current["date"], period=period, **account_fields)
        if periods:
            period = Counter(periods).most_common(1)[0][0]
            latest = charges[-1]
            add("recurring", merchant, period=period, amount=latest["amount"], date=latest["date"], **account_fields)
            expected = _next(date.fromisoformat(latest["date"]), period)
            if expected >= today:
                add("renewal", merchant, period=period, date=expected.isoformat(), amount=latest["amount"], **account_fields)
    return results


def _describe(item):
    merchant, kind = item["merchant"], item["kind"]
    if kind == "price_rise":
        return f"{merchant} rose from {item['before']} to {item['amount']} on {item['date']}"
    if kind == "duplicate":
        return f"{merchant} may have charged {item['amount']} twice on {' and '.join(item['dates'])}"
    if kind == "recurring":
        return f"{merchant} looks {item['period']} at {item['amount']}"
    return f"{merchant} may renew on {item['date']} for {item['amount']}"


class MoneyWatchAgent(BasicAgent):
    def __init__(self):
        self.name = "MoneyWatch"
        self.metadata = {
            "name": self.name, "description": "Check local bank or card CSV files; never connects to a bank or uploads data.",
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["read", "list_findings", "forget"]},
                "path": {"type": "string"}, "merchant": {"type": "string"}},
                "required": ["action"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        try:
            with _locked():
                state = load_state()
                action = kwargs.get("action")
                if action == "read":
                    path = kwargs.get("path")
                    if not isinstance(path, str) or not path.strip():
                        return "Please give the path to a bank or card CSV export."
                    try:
                        incoming, direction = read_csv(path)
                    except CSVColumnsError as error:
                        logging.warning("Money Watch could not identify CSV columns: %s", error)
                        return f"Money Watch could not read this export; missing columns: {error}."
                    existing = Counter(_key(item) for item in state["transactions"])
                    seen = Counter()
                    added = 0
                    for item in incoming:
                        if item["merchant"] in state["forgotten"]:
                            continue
                        key = _key(item)
                        seen[key] += 1
                        if seen[key] > existing[key]:
                            state["transactions"].append(item)
                            added += 1
                    _save(state)
                    today = date.today()
                    found = findings(state["transactions"], today=today)
                    return (f"Read {added} new charges on this computer; {direction}."
                            f" Renewals checked from {today.isoformat()} (today, local time); findings: "
                            + ("; ".join(_describe(item) for item in found) or "none yet") + ".")
                if action == "list_findings":
                    today = date.today()
                    found = findings(state["transactions"], today=today)
                    return (f"Renewals checked from {today.isoformat()} (today, local time); findings: "
                            + ("; ".join(_describe(item) for item in found) or "none yet") + ".")
                if action == "forget":
                    merchant = kwargs.get("merchant")
                    if not isinstance(merchant, str) or not merchant.strip():
                        return "Please give the merchant name to leave out."
                    merchant = _merchant(merchant)
                    state["transactions"] = [item for item in state["transactions"] if item["merchant"] != merchant]
                    if merchant not in state["forgotten"]:
                        state["forgotten"].append(merchant)
                    _save(state)
                    return (f"{merchant} is left out of checks and future imports."
                            " Saved history and your original exports are kept, not erased.")
                return "Please choose read, list_findings or forget."
        except Exception:
            logging.exception("Money Watch could not finish")
            return "Money Watch could not finish; please check the CSV columns, amounts, dates and saved charge folder."

    def system_context(self):
        try:
            with _locked():
                state = load_state()
                fresh = [item for item in findings(state["transactions"])
                         if item["kind"] in {"price_rise", "duplicate"} and item["id"] not in state["told"]]
                if not fresh:
                    return None
                state["told"].extend(item["id"] for item in fresh)
                _save(state)
                return "Money needs a look: " + "; ".join(_describe(item) for item in fresh) + "."
        except Exception:
            logging.exception("Money Watch could not check new findings")
            return "Money Watch could not check new charges; please check the saved charge folder."
