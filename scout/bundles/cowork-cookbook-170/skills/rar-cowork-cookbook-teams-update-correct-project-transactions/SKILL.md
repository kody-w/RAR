---
name: "rar-cowork-cookbook-teams-update-correct-project-transactions"
description: "Drafts a Teams channel post on correct project transactions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_project_transactions", "rar_sha256": "870ca4752133607290daeeb5239e6e4a6f293fb2bf5fcdbea8b1352c76eb9937", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_correct_project_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-correct-project-transactions:0cb419a6c098f210438b7630e93a603ff918d27698c1af9e8073c7fdb2494926", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_correct_project_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_correct_project_transactions_agent.py` is
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

Correct project transactions Teams Channel Update — Drafts a Teams channel post on correct project transactions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-project-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_project_transactions_agent.py` and embedded as the fenced Python below (sha256 870ca47521336072…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_project_transactions_agent.py` first:

```bash
python3 teams_update_correct_project_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_correct_project_transactions_agent.py   # or on stdin
python3 teams_update_correct_project_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct project transactions Teams Channel Update — Drafts a Teams channel post on correct project transactions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-project-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_correct_project_transactions',
    "version": '2.0.0',
    "display_name": 'Correct project transactions Teams Channel Update',
    "description": 'Drafts a Teams channel post on correct project transactions status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-correct-project-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-correct-project-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2bf290d5f2750867',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/correct-project-transactions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-correct-project-transactions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCorrectProjectTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCorrectProjectTransactions'
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
    print(TeamsUpdateCorrectProjectTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
