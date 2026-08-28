---
name: "rar-cowork-cookbook-scheduled-brief-provide-insights-into-sales-strategies-and-performance"
description: "Schedulable morning-brief email summarizing provide insights into sales strategies and performance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "44dc851a6ec323b3d8b2daa33650c1c968f9f27048c3fbeb337fde5748ec133f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` and in the RCI capsule.

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

Provide insights into sales strategies and performance Scheduled Email Brief — Schedulable morning-brief email summarizing provide insights into sales strategies and performance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-provide-insights-into-sales-strategies-and-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` and embedded as the fenced Python below (sha256 44dc851a6ec323b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` first:

```bash
python3 scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py   # or on stdin
python3 scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide insights into sales strategies and performance Scheduled Email Brief — Schedulable morning-brief email summarizing provide insights into sales strategies and performance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-provide-insights-into-sales-strategies-and-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance',
    "version": '2.0.1',
    "display_name": 'Provide insights into sales strategies and performance Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing provide insights into sales strategies and performance for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-provide-insights-into-sales-strategies-and-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-provide-insights-into-sales-strategies-and-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c1ff551e52a11080',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-provide-insights-into-sales-strategies-and-performance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefProvideInsightsIntoSalesStrategiesAndPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefProvideInsightsIntoSalesStrategiesAndPerformance'
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
    print(ScheduledBriefProvideInsightsIntoSalesStrategiesAndPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
