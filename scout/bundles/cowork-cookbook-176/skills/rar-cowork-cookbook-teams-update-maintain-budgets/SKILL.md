---
name: "rar-cowork-cookbook-teams-update-maintain-budgets"
description: "Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_maintain_budgets", "rar_sha256": "23becb172d55c40cfd3025c20eba1bd1faf66accacd9ff1a1db2a58b2547c94a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_maintain_budgets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_maintain_budgets_agent.py` and in the RCI capsule.

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

Maintain budgets Teams Channel Update — Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-maintain-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_maintain_budgets_agent.py` and embedded as the fenced Python below (sha256 23becb172d55c40c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_maintain_budgets_agent.py` first:

```bash
python3 teams_update_maintain_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_maintain_budgets_agent.py   # or on stdin
python3 teams_update_maintain_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain budgets Teams Channel Update — Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-maintain-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_maintain_budgets',
    "version": '2.0.1',
    "display_name": 'Maintain budgets Teams Channel Update',
    "description": 'Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-maintain-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-maintain-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2bbc80abd783a3bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/maintain-budgets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-maintain-budgets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateMaintainBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMaintainBudgets'
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
    print(TeamsUpdateMaintainBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
