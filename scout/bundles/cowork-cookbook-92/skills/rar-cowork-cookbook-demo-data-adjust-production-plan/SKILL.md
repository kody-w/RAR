---
name: "rar-cowork-cookbook-demo-data-adjust-production-plan"
description: "Generates and creates realistic demo records for adjust production plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_adjust_production_plan", "rar_sha256": "44e7c2e5bd36db3417edee3675d28801fff5107359eb988fb0ce049c57b57985", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_adjust_production_plan_agent.py` and embedded as the fenced Python below (sha256 44e7c2e5bd36db34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_adjust_production_plan_agent.py` first:

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
    "version": '2.0.0',
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
