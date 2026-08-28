---
name: "rar-cowork-cookbook-dashboard-balance-supply-and-demand"
description: "Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_balance_supply_and_demand", "rar_sha256": "3d72456691f0c7360c2c02aed4cd2b316ad714f531a057ddb3c09d1e7c3f4d32", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_balance_supply_and_demand`. The original RAPP
agent is preserved byte-for-byte in `dashboard_balance_supply_and_demand_agent.py` and in the RCI capsule.

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

Balance supply and demand Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_balance_supply_and_demand_agent.py` and embedded as the fenced Python below (sha256 3d72456691f0c736…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_balance_supply_and_demand_agent.py` first:

```bash
python3 dashboard_balance_supply_and_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_balance_supply_and_demand_agent.py   # or on stdin
python3 dashboard_balance_supply_and_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Balance supply and demand Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_balance_supply_and_demand',
    "version": '2.0.1',
    "display_name": 'Balance supply and demand Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-balance-supply-and-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17357488517070fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/balance-supply-and-demand'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-balance-supply-and-demand', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardBalanceSupplyAndDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardBalanceSupplyAndDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(DashboardBalanceSupplyAndDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
