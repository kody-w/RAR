---
name: "rar-cowork-cookbook-teams-update-develop-budgeting-strategy"
description: "Drafts a Teams channel post on develop budgeting strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_budgeting_strategy", "rar_sha256": "8030182948229002594a64974992869d5db2f640d07d3b2628dbf721f9c2e025", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_budgeting_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-budgeting-strategy:a9a11a66800f51bbb549422e1595b0e2f68afdf9a7cf9005acff7dc5bd770d57", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_budgeting_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_budgeting_strategy_agent.py` is
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
