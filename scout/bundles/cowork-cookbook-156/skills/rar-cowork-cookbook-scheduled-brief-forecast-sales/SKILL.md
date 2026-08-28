---
name: "rar-cowork-cookbook-scheduled-brief-forecast-sales"
description: "Schedulable morning-brief email summarizing forecast sales for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_sales", "rar_sha256": "73d5f3d2865b8e13b2b906b92b582bc1126ed109012d93f61d9489ccab19b28a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_sales`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_sales_agent.py` and in the RCI capsule.

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
