---
name: "rar-cowork-cookbook-teams-update-conduct-training"
description: "Drafts a Teams channel post on conduct training status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_training", "rar_sha256": "0dfeb95db2d8f397148c24bf34e49e0d795de859e73672d28a62b16da2d7de19", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_training`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_training_agent.py` and in the RCI capsule.

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

Conduct training Teams Channel Update — Drafts a Teams channel post on conduct training status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-training
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_training_agent.py` and embedded as the fenced Python below (sha256 0dfeb95db2d8f397…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_training_agent.py` first:

```bash
python3 teams_update_conduct_training_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_training_agent.py   # or on stdin
python3 teams_update_conduct_training_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct training Teams Channel Update — Drafts a Teams channel post on conduct training status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-training
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_training',
    "version": '2.0.1',
    "display_name": 'Conduct training Teams Channel Update',
    "description": 'Drafts a Teams channel post on conduct training status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-conduct-training',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-training',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2f6d5ba5ce57c94d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/conduct-training'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-conduct-training', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateConductTraining(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductTraining'
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
    print(TeamsUpdateConductTraining().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
