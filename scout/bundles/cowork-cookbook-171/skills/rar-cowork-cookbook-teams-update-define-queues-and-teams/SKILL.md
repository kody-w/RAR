---
name: "rar-cowork-cookbook-teams-update-define-queues-and-teams"
description: "Drafts a Teams channel post on define queues and teams status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_queues_and_teams", "rar_sha256": "3ab3f04dcb04a39c7466cc8ff5a20b6e3835085810b02a1f9f83d5173cf8e7ea", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_queues_and_teams_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-queues-and-teams:bf292def28b2e17dce51684b6c44c278078850becb991ef9993769093e7ad606", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_queues_and_teams`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_queues_and_teams_agent.py` is
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
