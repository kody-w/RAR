---
name: "rar-cowork-cookbook-demo-data-adjust-production-plan"
description: "Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_adjust_production_plan", "rar_sha256": "c1b93b387ae14b859d6fc7dd81fe6633d3e0449103307ef756e489dd2c7fd46e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_adjust_production_plan`. The original RAPP
agent is preserved byte-for-byte in `demo_data_adjust_production_plan_agent.py` and in the RCI capsule.

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

Adjust production plan Demo Data Generator — Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-adjust-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_adjust_production_plan_agent.py` and embedded as the fenced Python below (sha256 c1b93b387ae14b85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_adjust_production_plan_agent.py` first:

```bash
python3 demo_data_adjust_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_adjust_production_plan_agent.py   # or on stdin
python3 demo_data_adjust_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust production plan Demo Data Generator — Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-adjust-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_adjust_production_plan',
    "version": '2.0.1',
    "display_name": 'Adjust production plan Demo Data Generator',
    "description": 'Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-adjust-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-adjust-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd097dae42363ef4c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/adjust-production-plan'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-adjust-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAdjustProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAdjustProductionPlan'
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
    print(DemoDataAdjustProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
