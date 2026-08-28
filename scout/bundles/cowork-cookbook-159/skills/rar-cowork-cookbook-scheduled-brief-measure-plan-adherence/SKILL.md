---
name: "rar-cowork-cookbook-scheduled-brief-measure-plan-adherence"
description: "Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_plan_adherence", "rar_sha256": "fb8e3d8a88f2286d0ff0121d34d9cc6e2ba99940fb6b86db6779cd5dd8ade7a7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_measure_plan_adherence`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_measure_plan_adherence_agent.py` and in the RCI capsule.

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

Measure plan adherence Scheduled Email Brief — Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_plan_adherence_agent.py` and embedded as the fenced Python below (sha256 fb8e3d8a88f2286d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_plan_adherence_agent.py` first:

```bash
python3 scheduled_brief_measure_plan_adherence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_plan_adherence_agent.py   # or on stdin
python3 scheduled_brief_measure_plan_adherence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure plan adherence Scheduled Email Brief — Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_plan_adherence',
    "version": '2.0.1',
    "display_name": 'Measure plan adherence Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-measure-plan-adherence',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49fd132883305a3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-plan-adherence'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-measure-plan-adherence', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefMeasurePlanAdherence(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasurePlanAdherence'
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
    print(ScheduledBriefMeasurePlanAdherence().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
