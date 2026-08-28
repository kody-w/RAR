---
name: "rar-cowork-cookbook-teams-update-run-events"
description: "Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_run_events", "rar_sha256": "5b9b1a82ea7e1f09a5ddef7062f867d043216c56634400dec47db93bbfa74a8e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_run_events`. The original RAPP
agent is preserved byte-for-byte in `teams_update_run_events_agent.py` and in the RCI capsule.

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

Run events Teams Channel Update — Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-run-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_run_events_agent.py` and embedded as the fenced Python below (sha256 5b9b1a82ea7e1f09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_run_events_agent.py` first:

```bash
python3 teams_update_run_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_run_events_agent.py   # or on stdin
python3 teams_update_run_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run events Teams Channel Update — Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-run-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_run_events',
    "version": '2.0.1',
    "display_name": 'Run events Teams Channel Update',
    "description": 'Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-run-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-run-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '98455c3b0dd428a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-events'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-run-events', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateRunEvents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRunEvents'
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
    print(TeamsUpdateRunEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
