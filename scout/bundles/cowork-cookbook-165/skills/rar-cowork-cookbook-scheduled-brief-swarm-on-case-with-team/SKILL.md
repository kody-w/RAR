---
name: "rar-cowork-cookbook-scheduled-brief-swarm-on-case-with-team"
description: "Schedulable morning-brief email summarizing swarm on case with team for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_swarm_on_case_with_team", "rar_sha256": "4a8715c45d02fd085f8f10e047dc8d5da98d319dc32b60bda05a96717fff4253", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_swarm_on_case_with_team_agent.py` and embedded as the fenced Python below (sha256 4a8715c45d02fd08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_swarm_on_case_with_team_agent.py` first:

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
    "version": '2.0.1',
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
