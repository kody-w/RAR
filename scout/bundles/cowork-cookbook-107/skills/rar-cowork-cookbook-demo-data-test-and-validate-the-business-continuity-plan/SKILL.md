---
name: "rar-cowork-cookbook-demo-data-test-and-validate-the-business-continuity-plan"
description: "Generates and creates realistic demo records for test and validate the business continuity plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan", "rar_sha256": "37dc53629674656c1ba7b6e45971e6eb35a99359782862fdec18686c684bab7b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `demo_data_test_and_validate_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_test_and_validate_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 37dc53629674656c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_test_and_validate_the_business_continuity_plan_agent.py` first:

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
    "version": '2.0.1',
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
