---
name: "rar-cowork-cookbook-teams-update-track-skills-and-competencies"
description: "Drafts a Teams channel post on track skills and competencies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_skills_and_competencies", "rar_sha256": "e49af7dd08c222b11f9f3937f811e047b719e8e02c491d0db5c437a77d1d3b51", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_track_skills_and_competencies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_track_skills_and_competencies_agent.py` and in the RCI capsule.

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

Track skills and competencies Teams Channel Update — Drafts a Teams channel post on track skills and competencies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_track_skills_and_competencies_agent.py` and embedded as the fenced Python below (sha256 e49af7dd08c222b1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_track_skills_and_competencies_agent.py` first:

```bash
python3 teams_update_track_skills_and_competencies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_track_skills_and_competencies_agent.py   # or on stdin
python3 teams_update_track_skills_and_competencies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track skills and competencies Teams Channel Update — Drafts a Teams channel post on track skills and competencies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_track_skills_and_competencies',
    "version": '2.0.1',
    "display_name": 'Track skills and competencies Teams Channel Update',
    "description": 'Drafts a Teams channel post on track skills and competencies status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-track-skills-and-competencies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-track-skills-and-competencies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47fdbd930feb2beb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/track-skills-and-competencies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-track-skills-and-competencies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateTrackSkillsAndCompetencies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTrackSkillsAndCompetencies'
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
    print(TeamsUpdateTrackSkillsAndCompetencies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
