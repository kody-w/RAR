---
name: "rar-cowork-cookbook-teams-update-measure-frontline-worker-service-performance"
description: "Drafts a Teams channel post on measure frontline worker service performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_measure_frontline_worker_service_performance", "rar_sha256": "3cff8310166325fc90e325811565a0d6dd797291d51532d4e91478e6f69f5bf2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_measure_frontline_worker_service_performance_agent.py` and embedded as the fenced Python below (sha256 3cff8310166325fc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_measure_frontline_worker_service_performance_agent.py` first:

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
    "version": '2.0.0',
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
