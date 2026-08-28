---
name: "rar-cowork-cookbook-demo-data-forecast-demand"
description: "Generates and creates realistic demo records for forecast demand in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_demand", "rar_sha256": "fcd77837a0f86524c69d9ba101cacef6266630976ec16a80f1688988fd2ef4c7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_forecast_demand`. The original RAPP
agent is preserved byte-for-byte in `demo_data_forecast_demand_agent.py` and in the RCI capsule.

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

Forecast demand Demo Data Generator — Generates and creates realistic demo records for forecast demand in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_forecast_demand_agent.py` and embedded as the fenced Python below (sha256 fcd77837a0f86524…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_forecast_demand_agent.py` first:

```bash
python3 demo_data_forecast_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_forecast_demand_agent.py   # or on stdin
python3 demo_data_forecast_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast demand Demo Data Generator — Generates and creates realistic demo records for forecast demand in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_forecast_demand',
    "version": '2.0.1',
    "display_name": 'Forecast demand Demo Data Generator',
    "description": 'Generates and creates realistic demo records for forecast demand in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-forecast-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-forecast-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b56da79536394d4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/forecast-demand'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-forecast-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataForecastDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataForecastDemand'
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
    print(DemoDataForecastDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
