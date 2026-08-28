---
name: "rar-cowork-cookbook-teams-update-swarm-on-case-with-team"
description: "Drafts a Teams channel post on swarm on case with team status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_swarm_on_case_with_team", "rar_sha256": "9b796e6103b200d7cced9bbbc02cd25b315c0c22dbd5c5ec82d870ff150449a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_swarm_on_case_with_team_agent.py` and embedded as the fenced Python below (sha256 9b796e6103b200d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_swarm_on_case_with_team_agent.py` first:

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
    "version": '2.0.0',
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
