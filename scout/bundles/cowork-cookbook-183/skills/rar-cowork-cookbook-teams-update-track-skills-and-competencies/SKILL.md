---
name: "rar-cowork-cookbook-teams-update-track-skills-and-competencies"
description: "Drafts a Teams channel post on track skills and competencies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_skills_and_competencies", "rar_sha256": "026a0f8f79fd0e3bfbb18de63ecdc47bc7860bb25c71ec030b0b67083b5b1e64", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_track_skills_and_competencies_agent.py` and embedded as the fenced Python below (sha256 026a0f8f79fd0e3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_track_skills_and_competencies_agent.py` first:

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
    "version": '2.0.0',
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
