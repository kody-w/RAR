---
name: "rar-cowork-cookbook-teams-update-conduct-succession-planning"
description: "Drafts a Teams channel post on conduct succession planning status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_succession_planning", "rar_sha256": "188f4afd9c154ddb631d53ee4d0ec7ddfc8e90b0ae1c3eb3d833a7d8c700cbaf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
