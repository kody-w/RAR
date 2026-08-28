---
name: "rar-cowork-cookbook-teams-update-swarm-on-case-with-team"
description: "Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_swarm_on_case_with_team", "rar_sha256": "3845c14a451d68f3582e297ded6f82e3c82fcafb3fa15c149e4a1ca681063a0b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_swarm_on_case_with_team`. The original RAPP
agent is preserved byte-for-byte in `teams_update_swarm_on_case_with_team_agent.py` and in the RCI capsule.

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

Swarm on case with team Teams Channel Update — Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_swarm_on_case_with_team_agent.py` and embedded as the fenced Python below (sha256 3845c14a451d68f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_swarm_on_case_with_team_agent.py` first:

```bash
python3 teams_update_swarm_on_case_with_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_swarm_on_case_with_team_agent.py   # or on stdin
python3 teams_update_swarm_on_case_with_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Swarm on case with team Teams Channel Update — Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_swarm_on_case_with_team',
    "version": '2.0.1',
    "display_name": 'Swarm on case with team Teams Channel Update',
    "description": 'Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-swarm-on-case-with-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b9fdb93d32c404c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/swarm-on-case-with-team'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-swarm-on-case-with-team', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateSwarmOnCaseWithTeam(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSwarmOnCaseWithTeam'
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
    print(TeamsUpdateSwarmOnCaseWithTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
