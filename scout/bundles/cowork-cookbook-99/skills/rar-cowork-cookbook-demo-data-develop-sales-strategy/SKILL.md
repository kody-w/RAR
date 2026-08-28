---
name: "rar-cowork-cookbook-demo-data-develop-sales-strategy"
description: "Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_sales_strategy", "rar_sha256": "572f16a9a27f32d7feafcc0e6c488a32f11070ffc039c5f27e748cf3742a5128", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_sales_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_sales_strategy_agent.py` and in the RCI capsule.

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

Develop sales strategy Demo Data Generator — Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_sales_strategy_agent.py` and embedded as the fenced Python below (sha256 572f16a9a27f32d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_sales_strategy_agent.py` first:

```bash
python3 demo_data_develop_sales_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_sales_strategy_agent.py   # or on stdin
python3 demo_data_develop_sales_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales strategy Demo Data Generator — Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_sales_strategy',
    "version": '2.0.0',
    "display_name": 'Develop sales strategy Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop sales strategy in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-develop-sales-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-sales-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3a8d9b521b60094d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-sales-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-develop-sales-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDevelopSalesStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSalesStrategy'
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
    print(DemoDataDevelopSalesStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
