---
name: "rar-cowork-cookbook-scheduled-brief-provide-insights-into-sales-strategies-and-performance"
description: "Schedulable morning-brief email summarizing provide insights into sales strategies and performance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "c7125e2615b6bc1474dc44758662587b7fb3eaa18d01ce718a3d341154e0f3d7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` and embedded as the fenced Python below (sha256 c7125e2615b6bc14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` first:

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
    "version": '2.0.0',
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
