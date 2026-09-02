---
name: "rar-cowork-cookbook-teams-update-conduct-training"
description: "Drafts a Teams channel post on conduct training status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_training", "rar_sha256": "1ee9172de5d0b0999062629fe05f7e2fb0336092ca2d42e616e292f45fffa0cc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_conduct_training_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-conduct-training:556d159ff49f414d0e62e37a5db44dc8928e77730e7a995e87ef8d562be63665", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_conduct_training`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_conduct_training_agent.py` is
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
