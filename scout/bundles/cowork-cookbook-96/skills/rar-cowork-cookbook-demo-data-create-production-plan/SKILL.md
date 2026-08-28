---
name: "rar-cowork-cookbook-demo-data-create-production-plan"
description: "Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_production_plan", "rar_sha256": "c5cece051377a81577d540548f9a8368b8df615f097078aafde2e3de5e4fe33f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_create_production_plan`. The original RAPP
agent is preserved byte-for-byte in `demo_data_create_production_plan_agent.py` and in the RCI capsule.

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

Create production plan Demo Data Generator — Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 c5cece051377a815…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_create_production_plan_agent.py` first:

```bash
python3 demo_data_create_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_create_production_plan_agent.py   # or on stdin
python3 demo_data_create_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create production plan Demo Data Generator — Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_create_production_plan',
    "version": '2.0.1',
    "display_name": 'Create production plan Demo Data Generator',
    "description": 'Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-create-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-create-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b1dc776c3fe8213',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/create-production-plan'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-create-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataCreateProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCreateProductionPlan'
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
    print(DemoDataCreateProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
