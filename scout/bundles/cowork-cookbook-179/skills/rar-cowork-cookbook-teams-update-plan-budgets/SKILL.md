---
name: "rar-cowork-cookbook-teams-update-plan-budgets"
description: "Drafts a Teams channel post on plan budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_budgets", "rar_sha256": "5f53c8fd36b2739e8d4fed4f8ea0ca72087e992ead85c368a855a2e25cb7bc44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_plan_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-plan-budgets:0a2cd2cdb8ad073b794225bc2ddce978e69613364d9a68997bba65d6b41e1b1f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_plan_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_plan_budgets_agent.py` is
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

Plan budgets Teams Channel Update — Drafts a Teams channel post on plan budgets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_budgets_agent.py` and embedded as the fenced Python below (sha256 5f53c8fd36b2739e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_budgets_agent.py` first:

```bash
python3 teams_update_plan_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_plan_budgets_agent.py   # or on stdin
python3 teams_update_plan_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan budgets Teams Channel Update — Drafts a Teams channel post on plan budgets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_plan_budgets',
    "version": '2.0.0',
    "display_name": 'Plan budgets Teams Channel Update',
    "description": 'Drafts a Teams channel post on plan budgets status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-plan-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-plan-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c094e1f3915e3f11',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/plan-budgets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-plan-budgets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdatePlanBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePlanBudgets'
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
    print(TeamsUpdatePlanBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
