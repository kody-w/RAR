---
name: "rar-kody-w-deal-desk"
description: "Produces templated deal briefings, health scores, and competitive analyses for a named company, listing sales agents from the live RAR registry."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/deal_desk_agent", "rar_sha256": "68e3972b5c4a6b1b9f7105524aab0313aefcb121581beb8683fd98a0b90e2827", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.1", "author": "Kody Wildfeuer", "tags": ["deck", "deal", "sales", "b2b", "account-intelligence", "competitive", "pipeline", "crm"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `deal_desk_agent.py` and embedded as the fenced Python below (sha256 68e3972b5c4a6b1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `deal_desk_agent.py` first:

```bash
python3 deal_desk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 deal_desk_agent.py   # or on stdin
python3 deal_desk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/deal_desk_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/deal_desk_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/deal_desk_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
