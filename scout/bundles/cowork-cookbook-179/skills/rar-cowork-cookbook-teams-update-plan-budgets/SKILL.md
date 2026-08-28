---
name: "rar-cowork-cookbook-teams-update-plan-budgets"
description: "Drafts a Teams channel post on plan budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_budgets", "rar_sha256": "9222039555121cca763d71105ec970cc27e3a276a1c79774799ca6fd1416a4f7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_plan_budgets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_plan_budgets_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_budgets_agent.py` and embedded as the fenced Python below (sha256 9222039555121cca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_budgets_agent.py` first:

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
    "version": '2.0.1',
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
