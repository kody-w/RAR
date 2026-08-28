---
name: "rar-cowork-cookbook-demo-data-create-production-plan"
description: "Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_production_plan", "rar_sha256": "ff97129c25f9a6a153c582102ce6bf183562e1cf8e2d0769e197be340daa6114", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 ff97129c25f9a6a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_create_production_plan_agent.py` first:

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
    "version": '2.0.0',
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
