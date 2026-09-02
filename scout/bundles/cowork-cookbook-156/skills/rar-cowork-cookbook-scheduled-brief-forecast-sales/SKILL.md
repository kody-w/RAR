---
name: "rar-cowork-cookbook-scheduled-brief-forecast-sales"
description: "Schedulable morning-brief email summarizing forecast sales for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_sales", "rar_sha256": "73d5f3d2865b8e13b2b906b92b582bc1126ed109012d93f61d9489ccab19b28a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_forecast_sales_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-forecast-sales:64511148edf4458d48970555bb654cff5a87adca0eb428c9e6891d403fcff826", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_forecast_sales`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_forecast_sales_agent.py` is
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

Forecast sales Scheduled Email Brief — Schedulable morning-brief email summarizing forecast sales for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-sales
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_sales_agent.py` and embedded as the fenced Python below (sha256 73d5f3d2865b8e13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_sales_agent.py` first:

```bash
python3 scheduled_brief_forecast_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_sales_agent.py   # or on stdin
python3 scheduled_brief_forecast_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast sales Scheduled Email Brief — Schedulable morning-brief email summarizing forecast sales for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_sales',
    "version": '2.0.0',
    "display_name": 'Forecast sales Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing forecast sales for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe820ba3a8f058fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/forecast-sales'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-forecast-sales', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefForecastSales(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastSales'
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
    print(ScheduledBriefForecastSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
