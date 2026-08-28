---
name: "rar-cowork-cookbook-teams-update-develop-subcontracting-strategy"
description: "Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_subcontracting_strategy", "rar_sha256": "9e55b5626e116973d8ca80993813e86ccd62674d2c4905d2888e402c06da235b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_subcontracting_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_subcontracting_strategy_agent.py` and in the RCI capsule.

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

Develop subcontracting strategy Teams Channel Update — Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_subcontracting_strategy_agent.py` and embedded as the fenced Python below (sha256 9e55b5626e116973…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_subcontracting_strategy_agent.py` first:

```bash
python3 teams_update_develop_subcontracting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_subcontracting_strategy_agent.py   # or on stdin
python3 teams_update_develop_subcontracting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop subcontracting strategy Teams Channel Update — Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_subcontracting_strategy',
    "version": '2.0.1',
    "display_name": 'Develop subcontracting strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-subcontracting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a964139b06681734',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-subcontracting-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-develop-subcontracting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopSubcontractingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopSubcontractingStrategy'
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
    print(TeamsUpdateDevelopSubcontractingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
