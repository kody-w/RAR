---
name: "rar-cowork-cookbook-bulk-update-forecast-sales"
description: "Applies a bulk field update across forecast sales records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_sales", "rar_sha256": "c6519393b921ced53213b37d6fec0b8877bf7ddfca141acb23454a84d889086a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_forecast_sales`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_forecast_sales_agent.py` and in the RCI capsule.

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
