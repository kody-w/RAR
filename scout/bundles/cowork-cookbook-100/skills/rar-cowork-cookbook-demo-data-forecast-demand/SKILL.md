---
name: "rar-cowork-cookbook-demo-data-forecast-demand"
description: "Generates and creates realistic demo records for forecast demand in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_demand", "rar_sha256": "d10527bc7e9589d89a367d9336333839812ca3d295a4b096969456958ed2b093", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_forecast_demand_agent.py` and embedded as the fenced Python below (sha256 d10527bc7e9589d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_forecast_demand_agent.py` first:

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
    "version": '2.0.0',
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
