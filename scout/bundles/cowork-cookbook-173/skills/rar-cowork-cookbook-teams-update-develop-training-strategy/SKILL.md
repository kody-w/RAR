---
name: "rar-cowork-cookbook-teams-update-develop-training-strategy"
description: "Drafts a Teams channel post on develop training strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_training_strategy", "rar_sha256": "e4c84b9a0e58164dbf7d9f150db26348e398edb040adfe987cacf82bc3e7a887", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_training_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_training_strategy_agent.py` and in the RCI capsule.

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
