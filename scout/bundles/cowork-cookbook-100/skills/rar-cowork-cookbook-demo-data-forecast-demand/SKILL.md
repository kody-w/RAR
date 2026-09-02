---
name: "rar-cowork-cookbook-demo-data-forecast-demand"
description: "Generates and creates realistic demo records for forecast demand in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_demand", "rar_sha256": "d10527bc7e9589d89a367d9336333839812ca3d295a4b096969456958ed2b093", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_forecast_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-forecast-demand:699b5f8f79065a4aacac1bcc21af8a349b0c8aad80c47e57a2afa829f85ddaea", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_forecast_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_forecast_demand_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
