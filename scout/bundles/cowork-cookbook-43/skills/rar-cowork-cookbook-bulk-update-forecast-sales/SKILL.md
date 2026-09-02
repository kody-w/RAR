---
name: "rar-cowork-cookbook-bulk-update-forecast-sales"
description: "Applies a bulk field update across forecast sales records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_sales", "rar_sha256": "c6519393b921ced53213b37d6fec0b8877bf7ddfca141acb23454a84d889086a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_forecast_sales_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-forecast-sales:2cdf9f08940eb0207b9f26dba41ae7dd1df7785b9c97186ff624a2609ada9576", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_forecast_sales`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_forecast_sales_agent.py` is
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

Forecast sales Bulk Field Update — Applies a bulk field update across forecast sales records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-sales
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_forecast_sales_agent.py` and embedded as the fenced Python below (sha256 c6519393b921ced5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_forecast_sales_agent.py` first:

```bash
python3 bulk_update_forecast_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_forecast_sales_agent.py   # or on stdin
python3 bulk_update_forecast_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast sales Bulk Field Update — Applies a bulk field update across forecast sales records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-forecast-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_forecast_sales',
    "version": '2.0.0',
    "display_name": 'Forecast sales Bulk Field Update',
    "description": 'Applies a bulk field update across forecast sales records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-forecast-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-forecast-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '904ee9fb014da703',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/forecast-sales'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-forecast-sales', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateForecastSales(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateForecastSales'
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
    print(BulkUpdateForecastSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
