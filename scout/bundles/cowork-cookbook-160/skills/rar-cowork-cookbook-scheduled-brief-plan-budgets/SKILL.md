---
name: "rar-cowork-cookbook-scheduled-brief-plan-budgets"
description: "Schedulable morning-brief email summarizing plan budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_budgets", "rar_sha256": "b124b6ff9f11623ad9059ad9ffcccc97b38b8328287bfe46cd9adc71b7e09715", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_budgets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_budgets_agent.py` and in the RCI capsule.

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

Plan budgets Scheduled Email Brief — Schedulable morning-brief email summarizing plan budgets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_budgets_agent.py` and embedded as the fenced Python below (sha256 b124b6ff9f11623a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_budgets_agent.py` first:

```bash
python3 scheduled_brief_plan_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_budgets_agent.py   # or on stdin
python3 scheduled_brief_plan_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan budgets Scheduled Email Brief — Schedulable morning-brief email summarizing plan budgets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_budgets',
    "version": '2.0.0',
    "display_name": 'Plan budgets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan budgets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a295b896051d617d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/plan-budgets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-plan-budgets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefPlanBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanBudgets'
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
    print(ScheduledBriefPlanBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
