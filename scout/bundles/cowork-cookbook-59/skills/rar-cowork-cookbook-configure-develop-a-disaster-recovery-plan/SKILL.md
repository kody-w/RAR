---
name: "rar-cowork-cookbook-configure-develop-a-disaster-recovery-plan"
description: "Applies a bulk configuration change to develop a disaster recovery plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_a_disaster_recovery_plan", "rar_sha256": "b5eb9c53cd1ddba70670357dfe99226d57f3278ebe05a39d9a83777334c8c9c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_a_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 b5eb9c53cd1ddba7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_a_disaster_recovery_plan_agent.py` first:

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
    "version": '2.0.0',
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
