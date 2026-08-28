---
name: "rar-cowork-cookbook-teams-update-define-queues-and-teams"
description: "Drafts a Teams channel post on define queues and teams status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_queues_and_teams", "rar_sha256": "3544b6631610f8cd77dd9d92fe207328fa6a4a4e8aff2d43e13399073492502b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_queues_and_teams`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_queues_and_teams_agent.py` and in the RCI capsule.

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

Define queues and teams Teams Channel Update — Drafts a Teams channel post on define queues and teams status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_queues_and_teams_agent.py` and embedded as the fenced Python below (sha256 3544b6631610f8cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_queues_and_teams_agent.py` first:

```bash
python3 teams_update_define_queues_and_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_queues_and_teams_agent.py   # or on stdin
python3 teams_update_define_queues_and_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define queues and teams Teams Channel Update — Drafts a Teams channel post on define queues and teams status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_queues_and_teams',
    "version": '2.0.1',
    "display_name": 'Define queues and teams Teams Channel Update',
    "description": 'Drafts a Teams channel post on define queues and teams status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-queues-and-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '54e49094fd394388',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-queues-and-teams'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-define-queues-and-teams', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDefineQueuesAndTeams(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineQueuesAndTeams'
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
    print(TeamsUpdateDefineQueuesAndTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
