---
name: "rar-cowork-cookbook-teams-update-test-and-validate-the-disaster-recovery-plan"
description: "Drafts a Teams channel post on test and validate the disaster recovery plan status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "572bad145cfe4b32339de7f8a098ad0c6de15db001f568df7a2e334d43fedf8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_test_and_validate_the_disaster_recovery_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-test-and-validate-the-disaster-recovery-plan:2b597704526fb4569d9e9aff45d2e639f0d14f00f399636545afeac3d3301ae1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` is
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

Test and validate the disaster recovery plan Teams Channel Update — Drafts a Teams channel post on test and validate the disaster recovery plan status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-test-and-validate-the-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 572bad145cfe4b32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` first:

```bash
python3 teams_update_test_and_validate_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_test_and_validate_the_disaster_recovery_plan_agent.py   # or on stdin
python3 teams_update_test_and_validate_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test and validate the disaster recovery plan Teams Channel Update — Drafts a Teams channel post on test and validate the disaster recovery plan status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-test-and-validate-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan',
    "version": '2.0.0',
    "display_name": 'Test and validate the disaster recovery plan Teams Channel Update',
    "description": 'Drafts a Teams channel post on test and validate the disaster recovery plan status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-test-and-validate-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-test-and-validate-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '387a766adbab3450',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/test-and-validate-the-disaster-recovery-plan'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-test-and-validate-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateTestAndValidateTheDisasterRecoveryPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTestAndValidateTheDisasterRecoveryPlan'
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
    print(TeamsUpdateTestAndValidateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
