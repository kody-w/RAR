---
name: "rar-cowork-cookbook-demo-data-plan-production"
description: "Generates and creates realistic demo records for plan production in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_production", "rar_sha256": "255c03ce65162253941b8f466a4c8a3368af1b65c79963c66432d888574aea84", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_production_agent.py` and embedded as the fenced Python below (sha256 255c03ce65162253…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_production_agent.py` first:

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
    "version": '2.0.0',
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
