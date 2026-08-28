---
name: "rar-cowork-cookbook-teams-update-correct-project-transactions"
description: "Drafts a Teams channel post on correct project transactions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_project_transactions", "rar_sha256": "870ca4752133607290daeeb5239e6e4a6f293fb2bf5fcdbea8b1352c76eb9937", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_correct_project_transactions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_correct_project_transactions_agent.py` and in the RCI capsule.

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
