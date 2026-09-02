---
name: "rar-cowork-cookbook-bulk-update-provide-insights-into-sales-strategies-and-performance"
description: "Applies a bulk field update across provide insights into sales strategies and performance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "e6db444911afc1acf7f1457e3c003bf594857ba1f36c6db86582ad9e7cb0fe07", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-provide-insights-into-sales-strategies-and-performance:43cf05f7d32dc2712a0fd55e0558e8971b4ed10e0ea401c264c6c8f6833642ed", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_provide_insights_into_sales_strategies_and_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_provide_insights_into_sales_strategies_and_performance_agent.py` is
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
