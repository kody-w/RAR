---
name: "rar-cowork-cookbook-demo-data-test-and-validate-the-business-continuity-plan"
description: "Generates and creates realistic demo records for test and validate the business continuity plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan", "rar_sha256": "c227f6bf92cd77e1d52bb79eaf3d8fd4f8a3622e2fd05c1429fd3eb55e0fc7d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_test_and_validate_the_business_continuity_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-test-and-validate-the-business-continuity-plan:2d9e854bb257a34d38f62e3a173e71c8e0c0a452a6058c30c8dbd3f810888db2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_test_and_validate_the_business_continuity_plan_agent.py` is
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

Test and validate the business continuity plan Demo Data Generator — Generates and creates realistic demo records for test and validate the business continuity plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-test-and-validate-the-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_test_and_validate_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 c227f6bf92cd77e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_test_and_validate_the_business_continuity_plan_agent.py` first:

```bash
python3 demo_data_test_and_validate_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_test_and_validate_the_business_continuity_plan_agent.py   # or on stdin
python3 demo_data_test_and_validate_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test and validate the business continuity plan Demo Data Generator — Generates and creates realistic demo records for test and validate the business continuity plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-test-and-validate-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan',
    "version": '2.0.0',
    "display_name": 'Test and validate the business continuity plan Demo Data Generator',
    "description": 'Generates and creates realistic demo records for test and validate the business continuity plan in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-test-and-validate-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-test-and-validate-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a393b7d168f4852c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/test-and-validate-the-business-continuity-plan'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-test-and-validate-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTestAndValidateTheBusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTestAndValidateTheBusinessContinuityPlan'
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
    print(DemoDataTestAndValidateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
