---
name: "rar-cowork-cookbook-teams-update-develop-training-strategy"
description: "Drafts a Teams channel post on develop training strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_training_strategy", "rar_sha256": "e4c84b9a0e58164dbf7d9f150db26348e398edb040adfe987cacf82bc3e7a887", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_training_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-training-strategy:2d06c28fdf2d7c96625489a7858549839cae4afec4adb77f4965dcadb81acec2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_training_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_training_strategy_agent.py` is
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

Develop training strategy Teams Channel Update — Drafts a Teams channel post on develop training strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-training-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_training_strategy_agent.py` and embedded as the fenced Python below (sha256 e4c84b9a0e58164d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_training_strategy_agent.py` first:

```bash
python3 teams_update_develop_training_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_training_strategy_agent.py   # or on stdin
python3 teams_update_develop_training_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training strategy Teams Channel Update — Drafts a Teams channel post on develop training strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-training-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_training_strategy',
    "version": '2.0.0',
    "display_name": 'Develop training strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop training strategy status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-develop-training-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-training-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '85ec6f3f213c76cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-develop-training-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopTrainingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopTrainingStrategy'
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
    print(TeamsUpdateDevelopTrainingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
