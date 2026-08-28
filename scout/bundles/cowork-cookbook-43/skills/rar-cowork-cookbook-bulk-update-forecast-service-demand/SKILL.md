---
name: "rar-cowork-cookbook-bulk-update-forecast-service-demand"
description: "Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_service_demand", "rar_sha256": "f69fb2f83987e976bf5f5e667e5aeef115aec1e312e327109741343b41b07756", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_forecast_service_demand`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_forecast_service_demand_agent.py` and in the RCI capsule.

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

Forecast service demand Bulk Field Update — Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_forecast_service_demand_agent.py` and embedded as the fenced Python below (sha256 f69fb2f83987e976…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_forecast_service_demand_agent.py` first:

```bash
python3 bulk_update_forecast_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_forecast_service_demand_agent.py   # or on stdin
python3 bulk_update_forecast_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service demand Bulk Field Update — Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_forecast_service_demand',
    "version": '2.0.0',
    "display_name": 'Forecast service demand Bulk Field Update',
    "description": 'Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-forecast-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-forecast-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8663fa48784bd1b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/forecast-service-demand'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-forecast-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateForecastServiceDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateForecastServiceDemand'
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
    print(BulkUpdateForecastServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
