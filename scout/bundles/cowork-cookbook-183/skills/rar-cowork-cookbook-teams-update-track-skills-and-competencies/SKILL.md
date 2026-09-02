---
name: "rar-cowork-cookbook-teams-update-track-skills-and-competencies"
description: "Drafts a Teams channel post on track skills and competencies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_skills_and_competencies", "rar_sha256": "026a0f8f79fd0e3bfbb18de63ecdc47bc7860bb25c71ec030b0b67083b5b1e64", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_track_skills_and_competencies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-track-skills-and-competencies:a82e5123e4123ca029beedea487809c420790f562cb15775675bf7c40fd9f288", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_track_skills_and_competencies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_track_skills_and_competencies_agent.py` is
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
