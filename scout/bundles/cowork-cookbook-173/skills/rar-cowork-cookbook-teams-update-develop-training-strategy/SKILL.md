---
name: "rar-cowork-cookbook-teams-update-develop-training-strategy"
description: "Drafts a Teams channel post on develop training strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_training_strategy", "rar_sha256": "35f805afbcd8e6b88738944559f37538322fb70f54ffde9cd548e493fdc84590", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_training_strategy_agent.py` and embedded as the fenced Python below (sha256 35f805afbcd8e6b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_training_strategy_agent.py` first:

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
    "version": '2.0.1',
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
