---
name: "rar-cowork-cookbook-scheduled-brief-forecast-sales"
description: "Schedulable morning-brief email summarizing forecast sales for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_sales", "rar_sha256": "d30683a2d16d2a055b8703aaaac5a00d1e5c1b1f4078a616d379632d26bc6d35", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_sales_agent.py` and embedded as the fenced Python below (sha256 d30683a2d16d2a05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_sales_agent.py` first:

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
    "version": '2.0.1',
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
