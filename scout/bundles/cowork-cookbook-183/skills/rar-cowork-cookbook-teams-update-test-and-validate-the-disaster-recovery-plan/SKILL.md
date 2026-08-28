---
name: "rar-cowork-cookbook-teams-update-test-and-validate-the-disaster-recovery-plan"
description: "Drafts a Teams channel post on test and validate the disaster recovery plan status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "572bad145cfe4b32339de7f8a098ad0c6de15db001f568df7a2e334d43fedf8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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
