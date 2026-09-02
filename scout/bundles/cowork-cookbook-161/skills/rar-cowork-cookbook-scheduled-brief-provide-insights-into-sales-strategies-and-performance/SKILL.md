---
name: "rar-cowork-cookbook-scheduled-brief-provide-insights-into-sales-strategies-and-performance"
description: "Schedulable morning-brief email summarizing provide insights into sales strategies and performance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance", "rar_sha256": "c7125e2615b6bc1474dc44758662587b7fb3eaa18d01ce718a3d341154e0f3d7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-provide-insights-into-sales-strategies-and-performance:0fed8dd29800de5757d7f5d181c3af4facd764bf67f1e781938300547d1725bb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_provide_insights_into_sales_strategies_and_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_provide_insights_into_sales_strategies_and_performance_agent.py` is
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
