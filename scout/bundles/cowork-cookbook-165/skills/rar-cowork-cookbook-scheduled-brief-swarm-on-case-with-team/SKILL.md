---
name: "rar-cowork-cookbook-scheduled-brief-swarm-on-case-with-team"
description: "Schedulable morning-brief email summarizing swarm on case with team for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_swarm_on_case_with_team", "rar_sha256": "46105a577d044bacae7960c4d39d9c51a5d9ba9776ae27b6ae3baae29a641b00", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_swarm_on_case_with_team`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_swarm_on_case_with_team_agent.py` and in the RCI capsule.

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
