---
name: "rar-cowork-cookbook-configure-develop-scenario-and-contingency-plans"
description: "Applies a bulk configuration change to develop scenario and contingency plans from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_scenario_and_contingency_plans", "rar_sha256": "f9db387b58f7c69f4f9af634c11e2c4bcca65cc3b8e9a7791a8d4a264644181a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_scenario_and_contingency_plans_agent.py` and embedded as the fenced Python below (sha256 f9db387b58f7c69f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_scenario_and_contingency_plans_agent.py` first:

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
    "version": '2.0.0',
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
