---
name: "rar-cowork-cookbook-scheduled-brief-measure-frontline-worker-service-performance"
description: "Schedulable morning-brief email summarizing measure frontline worker service performance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance", "rar_sha256": "a898d30859ceeed8f849eeabe150196f88d7c31c702bc7736afd864133f86e44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_measure_frontline_worker_service_performance_agent.py` and in the RCI capsule.

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

Measure frontline worker service performance Scheduled Email Brief — Schedulable morning-brief email summarizing measure frontline worker service performance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-frontline-worker-service-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_frontline_worker_service_performance_agent.py` and embedded as the fenced Python below (sha256 a898d30859ceeed8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_frontline_worker_service_performance_agent.py` first:

```bash
python3 scheduled_brief_measure_frontline_worker_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_frontline_worker_service_performance_agent.py   # or on stdin
python3 scheduled_brief_measure_frontline_worker_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure frontline worker service performance Scheduled Email Brief — Schedulable morning-brief email summarizing measure frontline worker service performance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-frontline-worker-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance',
    "version": '2.0.0',
    "display_name": 'Measure frontline worker service performance Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing measure frontline worker service performance for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-measure-frontline-worker-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-frontline-worker-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31c112fc152b5047',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/measure-frontline-worker-service-performance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-measure-frontline-worker-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMeasureFrontlineWorkerServicePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasureFrontlineWorkerServicePerformance'
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
    print(ScheduledBriefMeasureFrontlineWorkerServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
