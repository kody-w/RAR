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
