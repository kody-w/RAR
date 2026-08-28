---
name: "rar-cowork-cookbook-scheduled-brief-plan-operational-allocation-and-investments"
description: "Schedulable morning-brief email summarizing plan operational allocation and investments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments", "rar_sha256": "3664b4af97250d1d761cc576d38a070adea574041c5ef6db0eba2bdc38555717", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_operational_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 3664b4af97250d1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_operational_allocation_and_investments_agent.py` first:

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
    "version": '2.0.0',
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
