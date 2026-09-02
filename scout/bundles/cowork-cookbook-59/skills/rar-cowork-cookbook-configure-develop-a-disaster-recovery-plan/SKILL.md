---
name: "rar-cowork-cookbook-configure-develop-a-disaster-recovery-plan"
description: "Applies a bulk configuration change to develop a disaster recovery plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_a_disaster_recovery_plan", "rar_sha256": "b5eb9c53cd1ddba70670357dfe99226d57f3278ebe05a39d9a83777334c8c9c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_a_disaster_recovery_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-a-disaster-recovery-plan:232e2ac7d9318fa1244a1d2fe658910546281210cde135e6d7d4c3a34ac494a7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_a_disaster_recovery_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_a_disaster_recovery_plan_agent.py` is
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
