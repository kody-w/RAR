---
name: "rar-cowork-cookbook-teams-update-conduct-succession-planning"
description: "Drafts a Teams channel post on conduct succession planning status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_succession_planning", "rar_sha256": "34b97c8d159752825643546670c33d6af027d01213cb7c564333b22f37f50e89", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_succession_planning`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_succession_planning_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_succession_planning_agent.py` and embedded as the fenced Python below (sha256 34b97c8d15975282…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_succession_planning_agent.py` first:

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
    "version": '2.0.1',
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
