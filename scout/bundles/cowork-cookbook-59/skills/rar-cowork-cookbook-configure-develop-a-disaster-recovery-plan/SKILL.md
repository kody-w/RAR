---
name: "rar-cowork-cookbook-configure-develop-a-disaster-recovery-plan"
description: "Applies a bulk configuration change to develop a disaster recovery plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_a_disaster_recovery_plan", "rar_sha256": "93820757e509258590bb9d9c38340d6e3ead91d4f94b994cd25999b96b18a04f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_a_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_a_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Develop a disaster recovery plan Configuration Bulk Setup — Applies a bulk configuration change to develop a disaster recovery plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-a-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_a_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 93820757e5092585…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_a_disaster_recovery_plan_agent.py` first:

```bash
python3 configure_develop_a_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_a_disaster_recovery_plan_agent.py   # or on stdin
python3 configure_develop_a_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a disaster recovery plan Configuration Bulk Setup — Applies a bulk configuration change to develop a disaster recovery plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-a-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_a_disaster_recovery_plan',
    "version": '2.0.1',
    "display_name": 'Develop a disaster recovery plan Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop a disaster recovery plan from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-a-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-a-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '45d5c22b213306d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-disaster-recovery-plan'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-develop-a-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDevelopADisasterRecoveryPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopADisasterRecoveryPlan'
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
    print(ConfigureDevelopADisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
