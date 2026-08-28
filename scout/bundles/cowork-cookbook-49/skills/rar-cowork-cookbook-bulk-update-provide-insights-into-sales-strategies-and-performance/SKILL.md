---
name: "rar-cowork-cookbook-bulk-update-provide-insights-into-sales-strategies-and-performance"
description: "Applies a bulk field update across provide insights into sales strategies and performance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "e6db444911afc1acf7f1457e3c003bf594857ba1f36c6db86582ad9e7cb0fe07", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` and embedded as the fenced Python below (sha256 e6db444911afc1ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` first:

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
    "version": '2.0.0',
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
