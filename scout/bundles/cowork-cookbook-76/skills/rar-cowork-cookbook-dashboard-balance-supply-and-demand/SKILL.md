---
name: "rar-cowork-cookbook-dashboard-balance-supply-and-demand"
description: "Produces a self-contained interactive HTML dashboard for balance supply and demand - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_balance_supply_and_demand", "rar_sha256": "c24a9d8fa9c9e7173f3b1543d9fb0e8706dde86e509092de9d27001c9ff2fe3e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_balance_supply_and_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-balance-supply-and-demand:76c196a50163145d4c52a2b52e1122a3169186733857cc31abee8457979ae23b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_balance_supply_and_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_balance_supply_and_demand_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_balance_supply_and_demand_agent.py` and embedded as the fenced Python below (sha256 c24a9d8fa9c9e717…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_balance_supply_and_demand_agent.py` first:

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
    "version": '2.0.0',
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
