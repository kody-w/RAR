---
name: "rar-cowork-cookbook-demo-data-plan-production"
description: "Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_production", "rar_sha256": "2bc05393503f8d86d76eee925a9296e571e78554fb28353a75faea965aec5a38", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_production`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_production_agent.py` and in the RCI capsule.

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

Plan production Demo Data Generator — Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_production_agent.py` and embedded as the fenced Python below (sha256 2bc05393503f8d86…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_production_agent.py` first:

```bash
python3 demo_data_plan_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_production_agent.py   # or on stdin
python3 demo_data_plan_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan production Demo Data Generator — Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_production',
    "version": '2.0.1',
    "display_name": 'Plan production Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-plan-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8672439d2d608843',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-production'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-plan-production', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataPlanProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProduction'
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
    print(DemoDataPlanProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
