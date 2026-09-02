---
name: "rar-cowork-cookbook-configure-develop-scenario-and-contingency-plans"
description: "Applies a bulk configuration change to develop scenario and contingency plans from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_scenario_and_contingency_plans", "rar_sha256": "f9db387b58f7c69f4f9af634c11e2c4bcca65cc3b8e9a7791a8d4a264644181a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_scenario_and_contingency_plans_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-scenario-and-contingency-plans:2a53307dfb1a518bcde3d7592304dd7f0f120330e1e63aafc3fe723556f5730c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_scenario_and_contingency_plans`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_scenario_and_contingency_plans_agent.py` is
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
