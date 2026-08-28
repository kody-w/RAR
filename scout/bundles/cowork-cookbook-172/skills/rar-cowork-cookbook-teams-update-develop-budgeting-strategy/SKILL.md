---
name: "rar-cowork-cookbook-teams-update-develop-budgeting-strategy"
description: "Drafts a Teams channel post on develop budgeting strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_budgeting_strategy", "rar_sha256": "8030182948229002594a64974992869d5db2f640d07d3b2628dbf721f9c2e025", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_budgeting_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_budgeting_strategy_agent.py` and in the RCI capsule.

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

Develop budgeting strategy Teams Channel Update — Drafts a Teams channel post on develop budgeting strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-budgeting-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_budgeting_strategy_agent.py` and embedded as the fenced Python below (sha256 8030182948229002…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_budgeting_strategy_agent.py` first:

```bash
python3 teams_update_develop_budgeting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_budgeting_strategy_agent.py   # or on stdin
python3 teams_update_develop_budgeting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgeting strategy Teams Channel Update — Drafts a Teams channel post on develop budgeting strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-budgeting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_budgeting_strategy',
    "version": '2.0.0',
    "display_name": 'Develop budgeting strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop budgeting strategy status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-develop-budgeting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-budgeting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '58a95e33dad65f03',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-budgeting-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-develop-budgeting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateDevelopBudgetingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopBudgetingStrategy'
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
    print(TeamsUpdateDevelopBudgetingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
