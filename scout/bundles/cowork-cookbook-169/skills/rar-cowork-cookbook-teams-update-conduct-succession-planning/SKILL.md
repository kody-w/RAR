---
name: "rar-cowork-cookbook-teams-update-conduct-succession-planning"
description: "Drafts a Teams channel post on conduct succession planning status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_succession_planning", "rar_sha256": "188f4afd9c154ddb631d53ee4d0ec7ddfc8e90b0ae1c3eb3d833a7d8c700cbaf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_conduct_succession_planning_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-conduct-succession-planning:3805cf1c33c680aadb727a3d8ef768d73bbdc37bafd660d1264bc2762a43ddc3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_conduct_succession_planning`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_conduct_succession_planning_agent.py` is
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

Conduct succession planning Teams Channel Update — Drafts a Teams channel post on conduct succession planning status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-succession-planning
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_succession_planning_agent.py` and embedded as the fenced Python below (sha256 188f4afd9c154ddb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_succession_planning_agent.py` first:

```bash
python3 teams_update_conduct_succession_planning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_succession_planning_agent.py   # or on stdin
python3 teams_update_conduct_succession_planning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct succession planning Teams Channel Update — Drafts a Teams channel post on conduct succession planning status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-succession-planning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_succession_planning',
    "version": '2.0.0',
    "display_name": 'Conduct succession planning Teams Channel Update',
    "description": 'Drafts a Teams channel post on conduct succession planning status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-conduct-succession-planning',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-succession-planning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6bdb0f7c1ee065f9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-succession-planning'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-conduct-succession-planning', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateConductSuccessionPlanning(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductSuccessionPlanning'
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
    print(TeamsUpdateConductSuccessionPlanning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
