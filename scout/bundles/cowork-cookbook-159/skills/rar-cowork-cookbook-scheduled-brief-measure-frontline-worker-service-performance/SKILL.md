---
name: "rar-cowork-cookbook-scheduled-brief-measure-frontline-worker-service-performance"
description: "Schedulable morning-brief email summarizing measure frontline worker service performance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_frontline_worker_service_performance", "rar_sha256": "beb47417648c995b851abbb32f0f1f19b55c820957fa607e073c75c9fdf0c772", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_frontline_worker_service_performance_agent.py` and embedded as the fenced Python below (sha256 beb47417648c995b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_frontline_worker_service_performance_agent.py` first:

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
    "version": '2.0.1',
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
