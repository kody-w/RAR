---
name: "rar-kody-w-deal-desk"
description: "Produces templated deal briefings, health scores, and competitive analyses for a named company, listing sales agents from the live RAR registry."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/deal_desk_agent", "rar_sha256": "68e3972b5c4a6b1b9f7105524aab0313aefcb121581beb8683fd98a0b90e2827", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.1", "author": "Kody Wildfeuer", "tags": ["deck", "deal", "sales", "b2b", "account-intelligence", "competitive", "pipeline", "crm"]}
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
