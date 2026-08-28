---
name: "rar-cowork-cookbook-demo-data-test-and-validate-the-business-continuity-plan"
description: "Generates and creates realistic demo records for test and validate the business continuity plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_and_validate_the_business_continuity_plan", "rar_sha256": "c227f6bf92cd77e1d52bb79eaf3d8fd4f8a3622e2fd05c1429fd3eb55e0fc7d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
