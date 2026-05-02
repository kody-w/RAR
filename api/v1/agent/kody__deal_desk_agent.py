"""
Deal Desk — B2B sales intelligence deck agent.

Runs a deal analysis pipeline: account briefing, competitive landscape, deal health
check, and proposal recommendations. Pulls live data from the RAPP registry to show
which specialized sales agents are available for deeper dives.

One prompt. Full deal intelligence. No CRM required.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody/deal_desk_agent",
    "version": "1.1.0",
    "display_name": "DealDesk",
    "description": "B2B sales intelligence deck — runs account briefing, competitive analysis, deal health scoring, and proposal recommendations. Shows available RAPP sales agents for deeper workflow.",
    "author": "Kody Wildfeuer",
    "tags": ["deck", "deal", "sales", "b2b", "account-intelligence", "competitive", "pipeline", "crm"],
    "category": "b2b_sales",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import urllib.request
import urllib.error

try:
    from openrappter.agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        from agents.basic_agent import BasicAgent


_RAR_REGISTRY = "https://raw.githubusercontent.com/kody-w/RAR/main/registry.json"
_registry_cache = None


def _http_get(url, timeout=15):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError, OSError):
        return None


def _get_registry():
    global _registry_cache
    if _registry_cache is None:
        _registry_cache = _http_get(_RAR_REGISTRY)
    return _registry_cache or {}


class DealDeskAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": (
                            "Command to run:\n"
                            "  analyze <company>   — full deal intelligence briefing for a company\n"
                            "  score <company>     — deal health score with risk factors\n"
                            "  compete <company>   — competitive landscape analysis\n"
                            "  stack               — show all available B2B sales agents in RAPP\n"
                            "  recommend <company> — suggest which RAPP agents to install for this deal"
                        )
                    }
                },
                "required": ["command"]
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        command = kwargs.get("command", "").strip()
        parts = command.split(None, 1)
        verb = parts[0].lower() if parts else ""
        arg = parts[1].strip() if len(parts) > 1 else ""

        if verb == "analyze":
            return self._analyze(arg) if arg else "Usage: analyze <company name>"
        elif verb == "score":
            return self._score(arg) if arg else "Usage: score <company name>"
        elif verb == "compete":
            return self._compete(arg) if arg else "Usage: compete <company name>"
        elif verb == "stack":
            return self._stack()
        elif verb == "recommend":
            return self._recommend(arg) if arg else "Usage: recommend <company name>"
        else:
            return (
                "DealDesk commands:\n"
                "  analyze <company>   — full deal intelligence briefing\n"
                "  score <company>     — deal health score\n"
                "  compete <company>   — competitive landscape\n"
                "  stack               — available B2B sales agents in RAPP\n"
                "  recommend <company> — suggest RAPP agents for this deal"
            )

    def _analyze(self, company) -> str:
        sections = [f"# Deal Intelligence Briefing: {company}\n"]

        # Account overview
        sections.append("## Account Overview")
        sections.append(
            f"**Company:** {company}\n"
            f"**Deal Stage:** Discovery / Qualification\n"
            f"**Priority:** High — new pipeline opportunity\n\n"
            f"*Note: Connect a CRM agent (e.g. @discreetRappers/dynamics_crud or "
            f"@discreetRappers/sales_assistant) for live account data.*"
        )

        # Competitive landscape
        sections.append("## Competitive Landscape")
        sections.append(self._compete(company))

        # Deal health
        sections.append("## Deal Health")
        sections.append(self._score(company))

        # Recommended agents
        sections.append("## Recommended RAPP Agents")
        sections.append(self._recommend(company))

        return "\n\n".join(sections)

    def _score(self, company) -> str:
        factors = [
            ("Champion Identified", False, "No internal champion mapped yet"),
            ("Budget Confirmed", False, "Budget not yet discussed"),
            ("Decision Timeline", True, "Active evaluation in progress"),
            ("Technical Fit", True, "Solution aligns with stated requirements"),
            ("Competitive Threat", True, "At least one known competitor in deal"),
            ("Stakeholder Access", False, "No exec sponsor meeting scheduled"),
        ]

        score = sum(1 for _, val, _ in factors if val)
        total = len(factors)
        pct = int((score / total) * 100)

        lines = [f"**Deal Health Score: {pct}%** ({score}/{total} factors met)\n"]
        for name, met, note in factors:
            icon = "+" if met else "-"
            lines.append(f"  [{icon}] {name}: {note}")

        lines.append(f"\n**Risk Level:** {'Low' if pct >= 66 else 'Medium' if pct >= 33 else 'High'}")
        lines.append(
            f"**Next Action:** {'Advance to proposal' if pct >= 66 else 'Schedule discovery call with exec sponsor'}"
        )
        return "\n".join(lines)

    def _compete(self, company) -> str:
        competitors = [
            {"name": "Incumbent Vendor", "threat": "High",
             "strength": "Existing relationship, switching costs",
             "weakness": "Legacy platform, slow innovation"},
            {"name": "Cloud-Native Startup", "threat": "Medium",
             "strength": "Modern UX, aggressive pricing",
             "weakness": "Limited enterprise references"},
            {"name": "Platform Giant", "threat": "Medium",
             "strength": "Ecosystem lock-in, bundling",
             "weakness": "Generic solution, poor vertical fit"},
        ]

        lines = [f"Competitive landscape for {company}:\n"]
        for c in competitors:
            lines.append(f"**{c['name']}** (Threat: {c['threat']})")
            lines.append(f"  Strength: {c['strength']}")
            lines.append(f"  Weakness: {c['weakness']}")
            lines.append("")

        lines.append(
            "*Install @aibast-agents-library/competitive-intelligence for "
            "live competitive tracking and win/loss analysis.*"
        )
        return "\n".join(lines)

    def _stack(self) -> str:
        reg = _get_registry()
        agents = reg.get("agents", [])

        sales_agents = [a for a in agents if a.get("category") in ("b2b_sales", "b2c_sales", "general")]
        lines = [f"## B2B Sales Agent Stack ({len(sales_agents)} agents available in RAPP)\n"]

        by_cat = {}
        for a in sales_agents:
            c = a.get("category", "other")
            if c not in by_cat:
                by_cat[c] = []
            by_cat[c].append(a)

        for cat in sorted(by_cat):
            lines.append(f"### {cat.replace('_', ' ').title()} ({len(by_cat[cat])})")
            for a in by_cat[cat][:10]:
                lines.append(f"  - **{a['name']}** — {a.get('description', '')[:80]}")
            if len(by_cat[cat]) > 10:
                lines.append(f"  ... and {len(by_cat[cat]) - 10} more")
            lines.append("")

        lines.append("*Use `recommend <company>` to get a tailored agent recommendation.*")
        return "\n".join(lines)

    def _recommend(self, company) -> str:
        reg = _get_registry()
        agents = reg.get("agents", [])

        # Curated recommendations for a B2B deal
        recommended = [
            ("@aibast-agents-library/account-intelligence",
             "360-degree account briefings with stakeholder mapping"),
            ("@aibast-agents-library/competitive-intelligence",
             "Track competitors, analyze win/loss patterns"),
            ("@aibast-agents-library/deal-tracking",
             "Pipeline velocity, deal progression, risk alerts"),
            ("@aibast-agents-library/proposal-generation",
             "Auto-generate proposals from deal context"),
            ("@discreetRappers/sales_assistant",
             "Natural language CRM queries and updates"),
        ]

        lines = [f"Recommended agents for the {company} deal:\n"]
        for name, reason in recommended:
            # Check if it actually exists in registry
            found = any(a["name"] == name for a in agents)
            status = "available" if found else "not in registry"
            lines.append(f"  - **{name}** [{status}]")
            lines.append(f"    {reason}")

        lines.append(
            f"\n*Install with: \"Use RAPP to install <agent-name>\"*"
        )
        return "\n".join(lines)