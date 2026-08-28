---
name: "rar-cowork-cookbook-scheduled-brief-measure-plan-adherence"
description: "Schedulable morning-brief email summarizing measure plan adherence for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_plan_adherence", "rar_sha256": "57e2df6708886022d7934dfb783a77667bcda8eaf6ab782cbfe1f5c3df31bfec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_plan_adherence_agent.py` and embedded as the fenced Python below (sha256 57e2df6708886022…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_plan_adherence_agent.py` first:

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
    "version": '2.0.0',
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
