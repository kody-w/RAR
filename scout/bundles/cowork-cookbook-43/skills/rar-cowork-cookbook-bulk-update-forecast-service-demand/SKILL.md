---
name: "rar-cowork-cookbook-bulk-update-forecast-service-demand"
description: "Applies a bulk field update across forecast service demand records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_service_demand", "rar_sha256": "f69fb2f83987e976bf5f5e667e5aeef115aec1e312e327109741343b41b07756", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_forecast_service_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-forecast-service-demand:f9a62f3a513acda3809c9fd611f376b95a89a42aa4ce1b61e590e1b825917645", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_forecast_service_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_forecast_service_demand_agent.py` is
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
