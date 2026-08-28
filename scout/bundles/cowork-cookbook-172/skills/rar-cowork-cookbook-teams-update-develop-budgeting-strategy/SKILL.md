---
name: "rar-cowork-cookbook-teams-update-develop-budgeting-strategy"
description: "Drafts a Teams channel post on develop budgeting strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_budgeting_strategy", "rar_sha256": "c2ffd552aa06087545b28c054bb076ef37c7dc0bf710e06bf268975644e0a9f2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_budgeting_strategy_agent.py` and embedded as the fenced Python below (sha256 c2ffd552aa060875…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_budgeting_strategy_agent.py` first:

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
    "version": '2.0.1',
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
