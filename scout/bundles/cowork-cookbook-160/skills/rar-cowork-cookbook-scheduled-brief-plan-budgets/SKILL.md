---
name: "rar-cowork-cookbook-scheduled-brief-plan-budgets"
description: "Schedulable morning-brief email summarizing plan budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_budgets", "rar_sha256": "b124b6ff9f11623ad9059ad9ffcccc97b38b8328287bfe46cd9adc71b7e09715", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_plan_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-plan-budgets:7cf17b89c7130dcdbe4c3a1507851995be867f13faec801b1dbefad206c9022d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_plan_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_plan_budgets_agent.py` is
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
