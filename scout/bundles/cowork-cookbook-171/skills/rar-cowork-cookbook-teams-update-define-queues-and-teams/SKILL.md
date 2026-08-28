---
name: "rar-cowork-cookbook-teams-update-define-queues-and-teams"
description: "Drafts a Teams channel post on define queues and teams status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_queues_and_teams", "rar_sha256": "3ab3f04dcb04a39c7466cc8ff5a20b6e3835085810b02a1f9f83d5173cf8e7ea", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_queues_and_teams_agent.py` and embedded as the fenced Python below (sha256 3ab3f04dcb04a39c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_queues_and_teams_agent.py` first:

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
    "version": '2.0.0',
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
