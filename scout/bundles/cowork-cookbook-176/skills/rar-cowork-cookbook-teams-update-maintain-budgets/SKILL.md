---
name: "rar-cowork-cookbook-teams-update-maintain-budgets"
description: "Drafts a Teams channel post on maintain budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_maintain_budgets", "rar_sha256": "3da1cf735128989adfa2cf821354ff3f53152e615f12e597428b3b511b95e074", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_maintain_budgets_agent.py` and embedded as the fenced Python below (sha256 3da1cf735128989a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_maintain_budgets_agent.py` first:

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
    "version": '2.0.0',
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
