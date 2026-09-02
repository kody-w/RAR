---
name: "rar-cowork-cookbook-scheduled-brief-measure-frontline-worker-service-performance"
description: "Schedulable morning-brief email summarizing measure frontline worker service performance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance", "rar_sha256": "a898d30859ceeed8f849eeabe150196f88d7c31c702bc7736afd864133f86e44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_measure_frontline_worker_service_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-measure-frontline-worker-service-performance:78d66b75cf8d26919b04775c071ac2489d26b98efd0edb3596b0c51ea82a36f8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_measure_frontline_worker_service_performance_agent.py` is
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
