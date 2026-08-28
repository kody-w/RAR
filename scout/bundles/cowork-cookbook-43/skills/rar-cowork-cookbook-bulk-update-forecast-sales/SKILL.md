---
name: "rar-cowork-cookbook-bulk-update-forecast-sales"
description: "Applies a bulk field update across forecast sales records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_forecast_sales", "rar_sha256": "f0fec4911730a735c68b1b6d3166a254e345834a7413c15ef853a7e9d1e609a5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_forecast_sales_agent.py` and embedded as the fenced Python below (sha256 f0fec4911730a735…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_forecast_sales_agent.py` first:

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
    "version": '2.0.1',
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
