---
name: "rar-cowork-cookbook-scheduled-brief-plan-operational-allocation-and-investments"
description: "Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments", "rar_sha256": "c0949589daeb33fd7abacce1d57d75e00427ac65bbe7dbb7e87fd8aa22146cad", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_operational_allocation_and_investments_agent.py` and in the RCI capsule.

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

Plan operational allocation and investments Scheduled Email Brief — Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_operational_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 c0949589daeb33fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_operational_allocation_and_investments_agent.py` first:

```bash
python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py   # or on stdin
python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan operational allocation and investments Scheduled Email Brief — Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments',
    "version": '2.0.1',
    "display_name": 'Plan operational allocation and investments Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-operational-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4485c489f7c26daa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-operational-allocation-and-investments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-plan-operational-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPlanOperationalAllocationAndInvestments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanOperationalAllocationAndInvestments'
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
    print(ScheduledBriefPlanOperationalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
