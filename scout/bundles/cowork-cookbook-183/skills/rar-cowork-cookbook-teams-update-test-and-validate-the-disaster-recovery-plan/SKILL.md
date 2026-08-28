---
name: "rar-cowork-cookbook-teams-update-test-and-validate-the-disaster-recovery-plan"
description: "Drafts a Teams channel post on test and validate the disaster recovery plan status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_and_validate_the_disaster_recovery_plan", "rar_sha256": "900a1282dadd3c7e81aef1b1a229d923a2aa4a71961502cb1209798beef9b5d1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 900a1282dadd3c7e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_test_and_validate_the_disaster_recovery_plan_agent.py` first:

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
    "version": '2.0.1',
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
