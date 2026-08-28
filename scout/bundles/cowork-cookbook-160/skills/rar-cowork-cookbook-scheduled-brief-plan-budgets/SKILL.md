---
name: "rar-cowork-cookbook-scheduled-brief-plan-budgets"
description: "Schedulable morning-brief email summarizing plan budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_budgets", "rar_sha256": "001cedc1b34c06913db6dc7a7893eb7d23da6a87564f598c07f4877edeb4c113", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_budgets_agent.py` and embedded as the fenced Python below (sha256 001cedc1b34c0691…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_budgets_agent.py` first:

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
    "version": '2.0.1',
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
