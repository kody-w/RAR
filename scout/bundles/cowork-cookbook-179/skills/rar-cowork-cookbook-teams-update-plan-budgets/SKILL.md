---
name: "rar-cowork-cookbook-teams-update-plan-budgets"
description: "Drafts a Teams channel post on plan budgets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_budgets", "rar_sha256": "5f53c8fd36b2739e8d4fed4f8ea0ca72087e992ead85c368a855a2e25cb7bc44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
