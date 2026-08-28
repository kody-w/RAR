---
name: "rar-cowork-cookbook-teams-update-measure-frontline-worker-service-performance"
description: "Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_frontline_worker_service_performance", "rar_sha256": "b922476c6f84b1b70c906a64d381ed5fe1191eae92887ab80777e447624ad4de", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_measure_frontline_worker_service_performance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_measure_frontline_worker_service_performance_agent.py` and in the RCI capsule.

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

Measure frontline worker service performance Teams Channel Update — Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_frontline_worker_service_performance_agent.py` and embedded as the fenced Python below (sha256 b922476c6f84b1b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_frontline_worker_service_performance_agent.py` first:

```bash
python3 teams_update_measure_frontline_worker_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_measure_frontline_worker_service_performance_agent.py   # or on stdin
python3 teams_update_measure_frontline_worker_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure frontline worker service performance Teams Channel Update — Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_measure_frontline_worker_service_performance',
    "version": '2.0.1',
    "display_name": 'Measure frontline worker service performance Teams Channel Update',
    "description": 'Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-measure-frontline-worker-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-measure-frontline-worker-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d5ee7c0d142cc81',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/measure-frontline-worker-service-performance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-measure-frontline-worker-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateMeasureFrontlineWorkerServicePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMeasureFrontlineWorkerServicePerformance'
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
    print(TeamsUpdateMeasureFrontlineWorkerServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
