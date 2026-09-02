---
name: "rar-kody-w-deal-desk"
description: "Produces templated deal briefings, health scores, and competitive analyses for a named company, listing sales agents from the live RAR registry."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/deal_desk_agent", "rar_sha256": "4f0a8d4f0c0a8ddd9f4f02b29efcfedb30080938bc14b66ce752170a3a3f88dd", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "deal_desk_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/deal-desk:f82742c29a5896675a600e0ba62cccd147433cf8887a1289250c5e49a5c4a653", "kind": "skill"}, "version": "1.1.1", "author": "Kody Wildfeuer", "tags": ["deck", "deal", "sales", "b2b", "account-intelligence", "competitive", "pipeline", "crm"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/deal_desk_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `deal_desk_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
