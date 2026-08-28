---
name: "rar-kody-w-deal-desk"
description: "Produces templated deal briefings, health scores, and competitive analyses for a named company, listing sales agents from the live RAR registry."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/deal_desk_agent", "rar_sha256": "4f0a8d4f0c0a8ddd9f4f02b29efcfedb30080938bc14b66ce752170a3a3f88dd", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.1.1", "author": "Kody Wildfeuer", "tags": ["deck", "deal", "sales", "b2b", "account-intelligence", "competitive", "pipeline", "crm"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/deal_desk_agent`. The original RAPP
agent is preserved byte-for-byte in `deal_desk_agent.py` and in the RCI capsule.

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

Deal Desk — B2B sales intelligence deck agent.

Runs a deal analysis pipeline: account briefing, competitive landscape, deal health
check, and proposal recommendations. Pulls live data from the RAPP registry to show
which specialized sales agents are available for deeper dives.

One prompt. Full deal intelligence. No CRM required.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "command": {
      "description": "Command to run:\n  analyze <company>   \u2014 full deal intelligence briefing for a company\n  score <company>     \u2014 deal health score with risk factors\n  compete <company>   \u2014 competitive landscape analysis\n  stack               \u2014 show all available B2B sales agents in RAPP\n  recommend <company> \u2014 suggest which RAPP agents to install for this deal",
      "type": "string"
    }
  },
  "required": [
    "command"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `deal_desk_agent.py` and embedded as the fenced Python below (sha256 4f0a8d4f0c0a8ddd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `deal_desk_agent.py` first:

```bash
python3 deal_desk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 deal_desk_agent.py   # or on stdin
python3 deal_desk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
    "name": "@kody-w/deal_desk_agent",
    "version": "1.1.1",
    "display_name": "DealDesk",
    "description": "Produces templated deal briefings, health scores, and competitive analyses for a named company, listing sales agents from the live RAR registry.",
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
