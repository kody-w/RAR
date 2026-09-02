---
name: "rar-cowork-cookbook-scheduled-brief-swarm-on-case-with-team"
description: "Schedulable morning-brief email summarizing swarm on case with team for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_swarm_on_case_with_team", "rar_sha256": "46105a577d044bacae7960c4d39d9c51a5d9ba9776ae27b6ae3baae29a641b00", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_swarm_on_case_with_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-swarm-on-case-with-team:df81f0007057e410868cd3bb4ec9117c2cb21600568314fb91dd9b1ba7c92200", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_swarm_on_case_with_team`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_swarm_on_case_with_team_agent.py` is
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

Swarm on case with team Scheduled Email Brief — Schedulable morning-brief email summarizing swarm on case with team for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-swarm-on-case-with-team
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_swarm_on_case_with_team_agent.py` and embedded as the fenced Python below (sha256 46105a577d044bac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_swarm_on_case_with_team_agent.py` first:

```bash
python3 scheduled_brief_swarm_on_case_with_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_swarm_on_case_with_team_agent.py   # or on stdin
python3 scheduled_brief_swarm_on_case_with_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Swarm on case with team Scheduled Email Brief — Schedulable morning-brief email summarizing swarm on case with team for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-swarm-on-case-with-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_swarm_on_case_with_team',
    "version": '2.0.0',
    "display_name": 'Swarm on case with team Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing swarm on case with team for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-swarm-on-case-with-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-swarm-on-case-with-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c6ca9c00e0a2092',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/swarm-on-case-with-team'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-swarm-on-case-with-team', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefSwarmOnCaseWithTeam(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSwarmOnCaseWithTeam'
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
    print(ScheduledBriefSwarmOnCaseWithTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
