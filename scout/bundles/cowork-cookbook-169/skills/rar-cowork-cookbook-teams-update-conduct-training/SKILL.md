---
name: "rar-cowork-cookbook-teams-update-conduct-training"
description: "Drafts a Teams channel post on conduct training status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_training", "rar_sha256": "1ee9172de5d0b0999062629fe05f7e2fb0336092ca2d42e616e292f45fffa0cc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_training_agent.py` and embedded as the fenced Python below (sha256 1ee9172de5d0b099…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_training_agent.py` first:

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
    "version": '2.0.0',
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
