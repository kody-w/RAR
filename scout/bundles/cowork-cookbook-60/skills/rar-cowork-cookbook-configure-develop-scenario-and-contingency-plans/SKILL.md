---
name: "rar-cowork-cookbook-configure-develop-scenario-and-contingency-plans"
description: "Applies a bulk configuration change to develop scenario and contingency plans from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_scenario_and_contingency_plans", "rar_sha256": "c1cf4218c4f01cd8c8196577e42d8fb1120c8718a902b7243b61d715b9c490a5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_scenario_and_contingency_plans`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_scenario_and_contingency_plans_agent.py` and in the RCI capsule.

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

Develop scenario and contingency plans Configuration Bulk Setup — Applies a bulk configuration change to develop scenario and contingency plans from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-scenario-and-contingency-plans
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_scenario_and_contingency_plans_agent.py` and embedded as the fenced Python below (sha256 c1cf4218c4f01cd8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_scenario_and_contingency_plans_agent.py` first:

```bash
python3 configure_develop_scenario_and_contingency_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_scenario_and_contingency_plans_agent.py   # or on stdin
python3 configure_develop_scenario_and_contingency_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop scenario and contingency plans Configuration Bulk Setup — Applies a bulk configuration change to develop scenario and contingency plans from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-scenario-and-contingency-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_scenario_and_contingency_plans',
    "version": '2.0.1',
    "display_name": 'Develop scenario and contingency plans Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop scenario and contingency plans from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-scenario-and-contingency-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-scenario-and-contingency-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bc6665c4d8ba7336',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-scenario-and-contingency-plans'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-develop-scenario-and-contingency-plans', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDevelopScenarioAndContingencyPlans(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopScenarioAndContingencyPlans'
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
    print(ConfigureDevelopScenarioAndContingencyPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
