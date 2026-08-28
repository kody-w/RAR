---
name: "rar-aibast-agents-library-account-risk-assessment"
description: "Scores deal risk, churn probability, and financial health with mitigation advice \u2014 on built-in demo accounts, or on real figures you supply via account_data."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/account_risk_assessment", "rar_sha256": "27c4185b7f6ed7654bf6f6b8ded0bf1c3a1043cd1129d20dcc039d46adecd2fb", "source_kind": "rar-agent", "source_commit": "97253417fb81295a2498f58e145e4941a47d7ef3", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "risk-assessment", "churn-prediction", "deal-risk"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/account_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `risk_assessment_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Account Risk Assessment Agent

Evaluates deal risk, churn probability, financial health, and generates
executive risk summaries for enterprise B2B accounts. Combines CRM signals,
financial indicators, and engagement data to produce actionable risk
mitigation recommendations.

Where a real deployment would call risk scoring APIs and financial data
providers, this agent uses a synthetic data layer so it runs anywhere
without credentials.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "account_data": {
      "description": "Score a real account instead of a demo one. Requires 'name'; optionally deal_stage, days_in_stage, opportunity_value, current_spend, expected_close_days, revenue, employees, industry.",
      "type": "object"
    },
    "account_name": {
      "description": "Account to assess. Must be one of the agent's demo accounts \u2014 call list_accounts to see them. An unrecognised name returns an explicit 'no data' response rather than another account's figures.",
      "type": "string"
    },
    "operation": {
      "description": "The risk assessment to perform",
      "enum": [
        "assess_deal_risk",
        "churn_prediction",
        "financial_risk",
        "executive_summary",
        "list_accounts"
      ],
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `risk_assessment_agent.py` and embedded as the fenced Python below (sha256 27c4185b7f6ed765…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `risk_assessment_agent.py` first:

```bash
python3 risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 risk_assessment_agent.py   # or on stdin
python3 risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Account Risk Assessment Agent

Evaluates deal risk, churn probability, financial health, and generates
executive risk summaries for enterprise B2B accounts. Combines CRM signals,
financial indicators, and engagement data to produce actionable risk
mitigation recommendations.

Where a real deployment would call risk scoring APIs and financial data
providers, this agent uses a synthetic data layer so it runs anywhere
without credentials.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import re
import threading
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/account_risk_assessment",
    "version": "1.1.0",
    "display_name": "Account Risk Assessment",
    "description": "Scores deal risk, churn probability, and financial health with mitigation advice — on built-in demo accounts, or on real figures you supply via account_data.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "risk-assessment", "churn-prediction", "deal-risk"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_DEFAULT_ACCOUNT = "acme"

_ACCOUNTS = {
    "acme": {
        "id": "acc-001", "name": "Acme Corporation", "industry": "Manufacturing",
        "revenue": 2_800_000_000, "employees": 12_400,
        "current_spend": 1_200_000, "opportunity_value": 2_400_000,
        "contract_renewal": "8 months", "deal_stage": "Proposal",
        "days_in_stage": 34, "expected_close_days": 21,
    },
    "contoso": {
        "id": "acc-002", "name": "Contoso Ltd", "industry": "Technology",
        "revenue": 980_000_000, "employees": 4_200,
        "current_spend": 680_000, "opportunity_value": 1_100_000,
        "contract_renewal": "3 months", "deal_stage": "Negotiation",
        "days_in_stage": 12, "expected_close_days": 30,
    },
    "fabrikam": {
        "id": "acc-003", "name": "Fabrikam Industries", "industry": "Manufacturing",
        "revenue": 1_500_000_000, "employees": 8_700,
        "current_spend": 450_000, "opportunity_value": 890_000,
        "contract_renewal": "14 months", "deal_stage": "Discovery",
        "days_in_stage": 18, "expected_close_days": 90,
    },
    "northwind": {
        "id": "acc-004", "name": "Northwind Traders", "industry": "Retail",
        "revenue": 620_000_000, "employees": 3_100,
        "current_spend": 220_000, "opportunity_value": 540_000,
        "contract_renewal": None, "deal_stage": "Qualification",
        "days_in_stage": 7, "expected_close_days": 120,
    },
}

_RISK_FACTORS = {
    "acme": [
        {"factor": "No CTO relationship", "category": "Stakeholder", "severity": "High", "weight": 0.25, "score": 82},
        {"factor": "Competitor pricing pressure (-15%)", "category": "Competitive", "severity": "High", "weight": 0.20, "score": 75},
        {"factor": "CFO requires ROI validation", "category": "Financial", "severity": "Medium", "weight": 0.15, "score": 60},
        {"factor": "Days in stage above average", "category": "Velocity", "severity": "Medium", "weight": 0.15, "score": 55},
        {"factor": "New CTO unknown sentiment", "category": "Stakeholder", "severity": "Medium", "weight": 0.10, "score": 50},
        {"factor": "Competitor RFP issued", "category": "Competitive", "severity": "Low", "weight": 0.10, "score": 40},
        {"factor": "Champion strongly engaged", "category": "Stakeholder", "severity": "Low", "weight": 0.05, "score": 15},
    ],
    "contoso": [
        {"factor": "Contract renewal in 3 months", "category": "Timeline", "severity": "High", "weight": 0.30, "score": 78},
        {"factor": "CFO budget cautious", "category": "Financial", "severity": "Medium", "weight": 0.20, "score": 55},
        {"factor": "Incumbent competitor on analytics", "category": "Competitive", "severity": "Medium", "weight": 0.20, "score": 52},
        {"factor": "Strong CTO advocacy", "category": "Stakeholder", "severity": "Low", "weight": 0.15, "score": 18},
        {"factor": "Series D funding (budget available)", "category": "Financial", "severity": "Low", "weight": 0.15, "score": 12},
    ],
    "fabrikam": [
        {"factor": "Early stage discovery", "category": "Velocity", "severity": "Medium", "weight": 0.25, "score": 45},
        {"factor": "New VP IT decision maker", "category": "Stakeholder", "severity": "Medium", "weight": 0.25, "score": 50},
        {"factor": "Low-cost competitor proposal", "category": "Competitive", "severity": "Medium", "weight": 0.20, "score": 55},
        {"factor": "COO champion engaged", "category": "Stakeholder", "severity": "Low", "weight": 0.15, "score": 20},
        {"factor": "Long renewal runway (14 months)", "category": "Timeline", "severity": "Low", "weight": 0.15, "score": 15},
    ],
    "northwind": [
        {"factor": "No existing relationship", "category": "Stakeholder", "severity": "High", "weight": 0.30, "score": 85},
        {"factor": "No products owned", "category": "Adoption", "severity": "High", "weight": 0.25, "score": 80},
        {"factor": "Only 1 discovery call", "category": "Velocity", "severity": "Medium", "weight": 0.20, "score": 60},
        {"factor": "CTO sentiment unknown", "category": "Stakeholder", "severity": "Medium", "weight": 0.15, "score": 55},
        {"factor": "E-commerce launch (budget available)", "category": "Financial", "severity": "Low", "weight": 0.10, "score": 20},
    ],
}

_CHURN_INDICATORS = {
    "acme": {
        "product_usage_trend": "stable", "support_tickets_30d": 3,
        "nps_score": 42, "login_frequency": "daily",
        "feature_adoption_pct": 67, "executive_sponsor_engaged": False,
        "last_qbr_days_ago": 45, "open_support_escalations": 0,
        "historical_churn_rate_industry": 0.12,
    },
    "contoso": {
        "product_usage_trend": "increasing", "support_tickets_30d": 1,
        "nps_score": 58, "login_frequency": "daily",
        "feature_adoption_pct": 52, "executive_sponsor_engaged": True,
        "last_qbr_days_ago": 20, "open_support_escalations": 0,
        "historical_churn_rate_industry": 0.18,
    },
    "fabrikam": {
        "product_usage_trend": "declining", "support_tickets_30d": 7,
        "nps_score": 28, "login_frequency": "weekly",
        "feature_adoption_pct": 34, "executive_sponsor_engaged": False,
        "last_qbr_days_ago": 90, "open_support_escalations": 2,
        "historical_churn_rate_industry": 0.12,
    },
    "northwind": {
        "product_usage_trend": "none", "support_tickets_30d": 0,
        "nps_score": None, "login_frequency": "none",
        "feature_adoption_pct": 0, "executive_sponsor_engaged": False,
        "last_qbr_days_ago": None, "open_support_escalations": 0,
        "historical_churn_rate_industry": 0.15,
    },
}

_FINANCIAL_HEALTH = {
    "acme": {
        "credit_rating": "A", "revenue_growth_yoy": 0.08,
        "debt_to_equity": 0.42, "operating_margin": 0.14,
        "cash_reserves_months": 18, "recent_layoffs": False,
        "budget_cycle": "Q1 (January)", "fiscal_year_end": "December",
        "it_budget_pct_revenue": 0.038,
    },
    "contoso": {
        "credit_rating": "BBB+", "revenue_growth_yoy": 0.22,
        "debt_to_equity": 0.65, "operating_margin": 0.09,
        "cash_reserves_months": 24, "recent_layoffs": False,
        "budget_cycle": "Q1 (January)", "fiscal_year_end": "December",
        "it_budget_pct_revenue": 0.062,
    },
    "fabrikam": {
        "credit_rating": "A-", "revenue_growth_yoy": 0.18,
        "debt_to_equity": 0.35, "operating_margin": 0.16,
        "cash_reserves_months": 14, "recent_layoffs": False,
        "budget_cycle": "Q4 (October)", "fiscal_year_end": "September",
        "it_budget_pct_revenue": 0.029,
    },
    "northwind": {
        "credit_rating": "BB+", "revenue_growth_yoy": 0.05,
        "debt_to_equity": 0.78, "operating_margin": 0.06,
        "cash_reserves_months": 9, "recent_layoffs": True,
        "budget_cycle": "Q1 (January)", "fiscal_year_end": "December",
        "it_budget_pct_revenue": 0.041,
    },
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_account(query):
    """Resolve an account name to a fixture key, or None when there is no match.

    This used to fall back to "acme" for anything it did not recognise, which meant
    asking about a company the agent has never heard of returned Acme Corporation's
    risk numbers with no indication that the question had been quietly swapped. For
    a tool whose output lands in a forecast review, silently answering about the
    wrong account is worse than refusing to answer.
    """
    if not query or not str(query).strip():
        return _DEFAULT_ACCOUNT
    q = str(query).lower().strip()
    if len(q) < 3:
        return None
    for key in _ACCOUNTS:
        if key == _CUSTOM_KEY:
            continue
        if re.search(rf"\b{re.escape(key)}\b", q) or q in _ACCOUNTS[key]["name"].lower():
            return key
    # Looser pass: match on any significant word of the fixture name. Requires a
    # word boundary so "contoso-like" matches but a 4-letter fragment of an
    # unrelated company name does not silently select a fixture.
    for key, acct in _ACCOUNTS.items():
        for word in acct["name"].lower().split():
            if len(word) > 3 and re.search(rf"\b{re.escape(word)}\b", q):
                return key
    return None


_CUSTOM_KEY = "__caller_supplied__"
# Custom accounts are staged in module-level tables, so two concurrent calls would
# otherwise read each other's figures. The brainstem can call agents in parallel.
_CUSTOM_LOCK = threading.Lock()


def _register_custom_account(data):
    """Score a real account the caller passes in, instead of only demo fixtures.

    The demo dataset made this agent a showpiece; accepting `account_data` makes it
    usable on an actual deal. Risk factors are derived from the supplied numbers by
    documented rules below, so the output is traceable to the input rather than
    invented.
    """
    if not isinstance(data, dict) or not str(data.get("name", "")).strip():
        raise ValueError("account_data must be an object containing at least a non-empty 'name'.")

    def _num(key, default=0, integer=False):
        raw = data.get(key, default)
        try:
            val = float(raw or 0)
        except (TypeError, ValueError):
            raise ValueError(f"account_data.{key} must be a number, got {raw!r}")
        if val < 0:
            raise ValueError(f"account_data.{key} cannot be negative, got {raw!r}")
        return int(val) if integer else val

    acct = {
        "id": "caller-supplied",
        "name": str(data["name"]).strip(),
        "industry": str(data.get("industry", "Unspecified")),
        "revenue": _num("revenue", integer=True),
        "employees": _num("employees", integer=True),
        "current_spend": _num("current_spend", integer=True),
        "opportunity_value": _num("opportunity_value", integer=True),
        "contract_renewal": str(data.get("contract_renewal", "unknown")),
        "deal_stage": str(data.get("deal_stage", "Unspecified")),
        "days_in_stage": _num("days_in_stage", integer=True),
        "expected_close_days": _num("expected_close_days", integer=True),
    }

    factors = []
    if acct["days_in_stage"] > 30:
        factors.append({"factor": f"Stalled {acct['days_in_stage']} days in {acct['deal_stage']}",
                        "category": "Momentum", "severity": "High" if acct["days_in_stage"] > 60 else "Medium",
                        "weight": 0.25, "score": min(95, 45 + acct["days_in_stage"])})
    if acct["current_spend"] and acct["opportunity_value"] > acct["current_spend"] * 2:
        factors.append({"factor": "Opportunity is a large multiple of current spend",
                        "category": "Financial", "severity": "Medium", "weight": 0.20, "score": 65})
    if acct["expected_close_days"] > 60:
        factors.append({"factor": f"Close date {acct['expected_close_days']} days out",
                        "category": "Momentum", "severity": "Medium", "weight": 0.15, "score": 55})
    if not acct["revenue"]:
        factors.append({"factor": "No company revenue supplied — financial risk is unscored",
                        "category": "Data", "severity": "Medium", "weight": 0.15, "score": 50})
    if not factors:
        factors.append({"factor": "No elevated risk signals in the supplied figures",
                        "category": "General", "severity": "Low", "weight": 0.10, "score": 25})

    _ACCOUNTS[_CUSTOM_KEY] = acct
    _RISK_FACTORS[_CUSTOM_KEY] = factors
    # Churn and financial scoring need signals the caller has not supplied. Rather
    # than fabricate them, mark them absent so those operations say so plainly.
    _CHURN_INDICATORS[_CUSTOM_KEY] = {}
    _FINANCIAL_HEALTH[_CUSTOM_KEY] = {}
    return _CUSTOM_KEY


def _clear_custom_account():
    for table in (_ACCOUNTS, _RISK_FACTORS, _CHURN_INDICATORS, _FINANCIAL_HEALTH):
        table.pop(_CUSTOM_KEY, None)


def _list_accounts_message():
    rows = "\n".join(
        f"| {a['name']} | {a['industry']} | {a['deal_stage']} | {a['days_in_stage']:.0f} | ${a['opportunity_value']:,.0f} |"
        for k, a in _ACCOUNTS.items() if k != _CUSTOM_KEY
    )
    return (
        "**Accounts available in this agent's demo dataset**\n\n"
        "| Account | Industry | Deal Stage | Days in Stage | Opportunity |\n|---|---|---|---|---|\n"
        f"{rows}\n\n"
        "These are built-in demo figures, not live CRM data. To assess a real account, pass "
        "`account_data` with your own numbers."
    )


def _unknown_account_message(query, operation):
    """What to say when we genuinely do not have data for what was asked."""
    known = "\n".join(
        f"| {a['name']} | {a['industry']} | {a['deal_stage']} | ${a['opportunity_value']:,} |"
        for a in _ACCOUNTS.values()
    )
    return (
        f"**No risk data for \"{query}\"**\n\n"
        f"This agent ships with a built-in demo dataset and has no record of that account, "
        f"so it will not produce a risk assessment for it. Guessing here would put another "
        f"company's numbers under your account's name.\n\n"
        f"**Accounts this agent can assess:**\n\n"
        f"| Account | Industry | Deal Stage | Opportunity |\n|---|---|---|---|\n{known}\n\n"
        f"Re-run `{operation}` with one of the names above, or pass your own figures with "
        f"`account_data` to score a real account:\n\n"
        f"```json\n{{\"operation\": \"{operation}\", \"account_data\": {{\"name\": \"{query}\", "
        f"\"deal_stage\": \"Proposal\", \"days_in_stage\": 30, \"opportunity_value\": 500000, "
        f"\"current_spend\": 100000, \"expected_close_days\": 45}}}}\n```"
    )


def _composite_risk_score(key):
    """Weighted risk score from all factors."""
    factors = _RISK_FACTORS.get(key, [])
    if not factors:
        return 50
    return int(sum(f["score"] * f["weight"] for f in factors))


def _win_probability(key):
    """Derive win probability from risk score."""
    risk = _composite_risk_score(key)
    return max(10, min(95, 100 - risk))


def _churn_probability(key):
    """Compute churn probability from indicators."""
    ind = _CHURN_INDICATORS.get(key, {})
    if not ind or ind["product_usage_trend"] == "none":
        return None

    base = ind["historical_churn_rate_industry"]
    usage_mod = {"increasing": -0.05, "stable": 0.0, "declining": 0.10, "none": 0.20}
    score = base + usage_mod.get(ind["product_usage_trend"], 0)

    if ind["nps_score"] and ind["nps_score"] < 30:
        score += 0.08
    if ind["open_support_escalations"] > 0:
        score += 0.05 * ind["open_support_escalations"]
    if ind["last_qbr_days_ago"] and ind["last_qbr_days_ago"] > 60:
        score += 0.04
    if ind["executive_sponsor_engaged"]:
        score -= 0.06
    if ind["feature_adoption_pct"] >= 60:
        score -= 0.04

    return max(0.02, min(0.85, round(score, 2)))


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class RiskAssessmentAgent(BasicAgent):
    """
    Evaluates deal and account risk across multiple dimensions.

    Operations:
        assess_deal_risk  - comprehensive deal risk analysis
        churn_prediction  - churn probability with contributing factors
        financial_risk    - financial health assessment
        executive_summary - consolidated risk executive summary
        list_accounts     - list the demo accounts this agent can assess

    Unknown account names return an explicit "no data" response listing what is
    available, rather than silently substituting another account's numbers. Pass
    account_data to score a real account from your own figures.
    """

    def __init__(self):
        self.name = "RiskAssessmentAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "assess_deal_risk", "churn_prediction",
                            "financial_risk", "executive_summary", "list_accounts",
                        ],
                        "description": "The risk assessment to perform",
                    },
                    "account_name": {
                        "type": "string",
                        "description": ("Account to assess. Must be one of the agent's demo accounts — "
                                        "call list_accounts to see them. An unrecognised name returns an "
                                        "explicit 'no data' response rather than another account's figures."),
                    },
                    "account_data": {
                        "type": "object",
                        "description": ("Score a real account instead of a demo one. Requires 'name'; "
                                        "optionally deal_stage, days_in_stage, opportunity_value, "
                                        "current_spend, expected_close_days, revenue, employees, industry."),
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "assess_deal_risk")
        dispatch = {
            "assess_deal_risk": self._assess_deal_risk,
            "churn_prediction": self._churn_prediction,
            "financial_risk": self._financial_risk,
            "executive_summary": self._executive_summary,
        }
        if op == "list_accounts":
            return _list_accounts_message()
        handler = dispatch.get(op)
        if not handler:
            valid = ", ".join(sorted(list(dispatch) + ["list_accounts"]))
            return f"**Error:** Unknown operation `{op}`.\n\nValid operations: {valid}."

        account_data = kwargs.get("account_data")
        if account_data:
            if op in ("churn_prediction", "financial_risk"):
                return (f"**`{op}` needs signals you have not supplied**\n\n"
                        f"Churn and financial scoring depend on usage, support and credit data that "
                        f"`account_data` does not carry, and this agent will not invent them. "
                        f"Use `assess_deal_risk` or `executive_summary` with your figures, or run "
                        f"`{op}` against a demo account (`list_accounts`).")
            with _CUSTOM_LOCK:
                try:
                    key = _register_custom_account(account_data)
                except ValueError as e:
                    return f"**Error:** {e}"
                try:
                    body = handler(key)
                except Exception as e:
                    return f"**Error:** could not score the supplied account — {type(e).__name__}: {e}"
                finally:
                    _clear_custom_account()
            return (body + "\n\n_Scored from the figures you supplied, not from the demo dataset._")

        requested = kwargs.get("account_name", "")
        key = _resolve_account(requested)
        if key is None:
            return _unknown_account_message(requested, op)
        body = handler(key)
        if not requested:
            body += (f"\n\n_No account was named, so this shows the default demo account "
                     f"({_ACCOUNTS[_DEFAULT_ACCOUNT]['name']}). Pass `account_name`, or `account_data` "
                     f"for a real account._")
        else:
            body += "\n\n_Figures are from this agent's built-in demo dataset, not live CRM data._"
        return body

    # ── assess_deal_risk ──────────────────────────────────────
    def _assess_deal_risk(self, key):
        acct = _ACCOUNTS[key]
        factors = _RISK_FACTORS.get(key, [])
        risk_score = _composite_risk_score(key)
        win_prob = _win_probability(key)

        factor_rows = ""
        for f in factors:
            factor_rows += f"| {f['factor']} | {f['category']} | {f['severity']} | {f['score']}/100 |\n"

        high_risks = [f for f in factors if f["severity"] == "High"]
        mitigations = ""
        if high_risks:
            mitigations = "\n**Immediate Mitigations Required:**\n"
            for i, r in enumerate(high_risks, 1):
                if r["category"] == "Stakeholder":
                    mitigations += f"{i}. Schedule champion intro to close stakeholder gap\n"
                elif r["category"] == "Competitive":
                    mitigations += f"{i}. Prepare TCO analysis countering competitor pricing\n"
                elif r["category"] == "Financial":
                    mitigations += f"{i}. Deliver customized ROI calculator to economic buyer\n"
                elif r["category"] == "Adoption":
                    mitigations += f"{i}. Offer pilot program to demonstrate value\n"
                else:
                    mitigations += f"{i}. Address: {r['factor']}\n"

        return (
            f"**Deal Risk Assessment: {acct['name']}**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Deal Stage | {acct['deal_stage']} |\n"
            f"| Days in Stage | {acct['days_in_stage']} |\n"
            f"| Opportunity Value | ${acct['opportunity_value']:,} |\n"
            f"| Composite Risk Score | {risk_score}/100 |\n"
            f"| Win Probability | {win_prob}% |\n"
            f"| Expected Close | {acct['expected_close_days']} days |\n\n"
            f"**Risk Factors:**\n\n"
            f"| Factor | Category | Severity | Score |\n|---|---|---|---|\n"
            f"{factor_rows}"
            f"{mitigations}\n"
            f"Source: [Deal Analytics + Risk Models + CRM]\n"
            f"Agents: RiskAssessmentAgent"
        )

    # ── churn_prediction ──────────────────────────────────────
    def _churn_prediction(self, key):
        acct = _ACCOUNTS[key]
        ind = _CHURN_INDICATORS.get(key, {})
        churn_prob = _churn_probability(key)

        if churn_prob is None:
            return (
                f"**Churn Prediction: {acct['name']}**\n\n"
                f"No product usage data available — this is a prospect account.\n"
                f"Churn prediction requires active product usage.\n\n"
                f"Source: [Product Analytics]\nAgents: RiskAssessmentAgent"
            )

        risk_level = "Critical" if churn_prob >= 0.30 else "Elevated" if churn_prob >= 0.15 else "Low"

        indicator_rows = (
            f"| Usage Trend | {ind['product_usage_trend'].title()} |\n"
            f"| Support Tickets (30d) | {ind['support_tickets_30d']} |\n"
            f"| NPS Score | {ind['nps_score']} |\n"
            f"| Login Frequency | {ind['login_frequency'].title()} |\n"
            f"| Feature Adoption | {ind['feature_adoption_pct']}% |\n"
            f"| Executive Sponsor Engaged | {'Yes' if ind['executive_sponsor_engaged'] else 'No'} |\n"
            f"| Last QBR | {ind['last_qbr_days_ago']} days ago |\n"
            f"| Open Escalations | {ind['open_support_escalations']} |\n"
            f"| Industry Churn Rate | {ind['historical_churn_rate_industry']:.0%} |\n"
        )

        actions = ""
        if churn_prob >= 0.20:
            actions = (
                "\n**Retention Actions:**\n"
                "1. Schedule executive business review within 2 weeks\n"
                "2. Assign dedicated CSM for high-touch engagement\n"
                "3. Deliver product adoption workshop\n"
                "4. Address open support escalations immediately\n"
            )
        elif churn_prob >= 0.10:
            actions = (
                "\n**Proactive Measures:**\n"
                "1. Schedule quarterly business review\n"
                "2. Share product roadmap preview\n"
                "3. Introduce executive sponsor program\n"
            )

        return (
            f"**Churn Prediction: {acct['name']}**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Churn Probability | {churn_prob:.0%} |\n"
            f"| Risk Level | {risk_level} |\n"
            f"| Current Spend | ${acct['current_spend']:,}/yr |\n"
            f"| Revenue at Risk | ${int(acct['current_spend'] * churn_prob):,} |\n"
            f"| Contract Renewal | {acct['contract_renewal'] or 'N/A'} |\n\n"
            f"**Contributing Indicators:**\n\n"
            f"| Indicator | Value |\n|---|---|\n"
            f"{indicator_rows}"
            f"{actions}\n"
            f"Source: [Product Analytics + Support + NPS]\n"
            f"Agents: RiskAssessmentAgent"
        )

    # ── financial_risk ────────────────────────────────────────
    def _financial_risk(self, key):
        acct = _ACCOUNTS[key]
        fin = _FINANCIAL_HEALTH.get(key, {})

        if fin["credit_rating"].startswith("A"):
            fin_risk = "Low"
        elif fin["credit_rating"].startswith("B") and "+" in fin["credit_rating"]:
            fin_risk = "Moderate"
        else:
            fin_risk = "Elevated"

        it_budget = int(acct["revenue"] * fin["it_budget_pct_revenue"])
        deal_pct_it_budget = acct["opportunity_value"] / max(it_budget, 1) * 100

        implications = ""
        if fin_risk == "Low":
            implications = (
                "- Strong financial position supports deal progression\n"
                "- Low debt and positive growth indicate budget availability\n"
            )
        elif fin_risk == "Moderate":
            implications = (
                "- Moderate financial caution recommended\n"
                "- Consider phased implementation to manage budget impact\n"
            )
        else:
            implications = (
                "- Elevated risk: validate budget approval path\n"
                "- Recommend smaller pilot to reduce buyer risk\n"
                "- Recent layoffs may signal budget tightening\n"
            )

        return (
            f"**Financial Risk Assessment: {acct['name']}**\n\n"
            f"**Company Financials:**\n\n"
            f"| Indicator | Value |\n|---|---|\n"
            f"| Credit Rating | {fin['credit_rating']} |\n"
            f"| Revenue Growth (YoY) | {fin['revenue_growth_yoy']:.0%} |\n"
            f"| Debt-to-Equity | {fin['debt_to_equity']:.2f} |\n"
            f"| Operating Margin | {fin['operating_margin']:.0%} |\n"
            f"| Cash Reserves | {fin['cash_reserves_months']} months |\n"
            f"| Recent Layoffs | {'Yes' if fin['recent_layoffs'] else 'No'} |\n\n"
            f"**Budget Analysis:**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Est. IT Budget | ${it_budget:,}/yr ({fin['it_budget_pct_revenue']:.1%} of revenue) |\n"
            f"| Deal Value | ${acct['opportunity_value']:,} |\n"
            f"| Deal as % IT Budget | {deal_pct_it_budget:.1f}% |\n"
            f"| Budget Cycle | {fin['budget_cycle']} |\n"
            f"| Fiscal Year End | {fin['fiscal_year_end']} |\n\n"
            f"**Financial Risk Level: {fin_risk}**\n\n"
            f"**Implications:**\n"
            f"{implications}\n"
            f"Source: [D&B + Financial Intelligence + CRM]\n"
            f"Agents: RiskAssessmentAgent"
        )

    # ── executive_summary ─────────────────────────────────────
    def _executive_summary(self, key):
        acct = _ACCOUNTS[key]
        risk_score = _composite_risk_score(key)
        win_prob = _win_probability(key)
        churn_prob = _churn_probability(key)
        fin = _FINANCIAL_HEALTH.get(key, {})
        factors = _RISK_FACTORS.get(key, [])

        high_count = sum(1 for f in factors if f["severity"] == "High")
        med_count = sum(1 for f in factors if f["severity"] == "Medium")

        churn_display = f"{churn_prob:.0%}" if churn_prob is not None else "N/A (prospect)"
        churn_status = "Monitoring" if churn_prob and churn_prob < 0.15 else "Action needed" if churn_prob else "N/A"

        if risk_score >= 65:
            overall = "High Risk"
            recommendation = "Escalate to management, accelerate mitigation actions"
        elif risk_score >= 40:
            overall = "Moderate Risk"
            recommendation = "Address high-severity factors within 2 weeks"
        else:
            overall = "Low Risk"
            recommendation = "Maintain current engagement cadence"

        risk_lines = "".join(
            f"- [{f['severity']}] {f['factor']}\n"
            for f in factors if f["severity"] in ("High", "Medium")
        )

        return (
            f"**Risk Executive Summary: {acct['name']}**\n\n"
            f"**Overall Assessment: {overall}**\n\n"
            f"| Dimension | Score | Status |\n|---|---|---|\n"
            f"| Deal Risk | {risk_score}/100 | {high_count} high, {med_count} medium factors |\n"
            f"| Win Probability | {win_prob}% | {'Above' if win_prob >= 50 else 'Below'} 50% threshold |\n"
            f"| Churn Probability | {churn_display} | {churn_status} |\n"
            f"| Financial Health | {fin.get('credit_rating', 'N/A')} | {fin.get('revenue_growth_yoy', 0):.0%} YoY growth |\n\n"
            f"**Key Risks:**\n"
            f"{risk_lines}\n"
            f"**Recommendation:** {recommendation}\n\n"
            f"**Value at Stake:**\n"
            f"- Opportunity: ${acct['opportunity_value']:,}\n"
            f"- Current ARR: ${acct['current_spend']:,}\n"
            f"- Total at risk: ${acct['opportunity_value'] + acct['current_spend']:,}\n\n"
            f"Source: [Deal Analytics + Financial Intelligence + Product Analytics]\n"
            f"Agents: RiskAssessmentAgent"
        )


if __name__ == "__main__":
    agent = RiskAssessmentAgent()
    for op in ["assess_deal_risk", "churn_prediction", "financial_risk", "executive_summary"]:
        print("=" * 60)
        print(agent.perform(operation=op, account_name="Acme Corporation"))
        print()
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
