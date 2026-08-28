---
name: "rar-cowork-cookbook-teams-update-correct-project-transactions"
description: "Drafts a Teams channel post on correct project transactions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_project_transactions", "rar_sha256": "9784ecf1c4744a85eac694aeb1b4af190cde1b0ef74b99d9c307615417bad601", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_project_transactions_agent.py` and embedded as the fenced Python below (sha256 9784ecf1c4744a85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_project_transactions_agent.py` first:

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
    "version": '2.0.1',
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
