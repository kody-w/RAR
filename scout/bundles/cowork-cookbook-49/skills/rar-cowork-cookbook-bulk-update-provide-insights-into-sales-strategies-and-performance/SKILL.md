---
name: "rar-cowork-cookbook-bulk-update-provide-insights-into-sales-strategies-and-performance"
description: "Applies a bulk field update across provide insights into sales strategies and performance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "9ee35d0a1943c35ae073318e203a6063f573ce003a0a617be7371b8a0d7db4e3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` and in the RCI capsule.

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

Provide insights into sales strategies and performance Bulk Field Update — Applies a bulk field update across provide insights into sales strategies and performance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-provide-insights-into-sales-strategies-and-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` and embedded as the fenced Python below (sha256 9ee35d0a1943c35a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` first:

```bash
python3 bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py   # or on stdin
python3 bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide insights into sales strategies and performance Bulk Field Update — Applies a bulk field update across provide insights into sales strategies and performance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-provide-insights-into-sales-strategies-and-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance',
    "version": '2.0.1',
    "display_name": 'Provide insights into sales strategies and performance Bulk Field Update',
    "description": 'Applies a bulk field update across provide insights into sales strategies and performance records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-provide-insights-into-sales-strategies-and-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-provide-insights-into-sales-strategies-and-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f7a7e9275398509',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-provide-insights-into-sales-strategies-and-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateProvideInsightsIntoSalesStrategiesAndPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateProvideInsightsIntoSalesStrategiesAndPerformance'
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
    print(BulkUpdateProvideInsightsIntoSalesStrategiesAndPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
