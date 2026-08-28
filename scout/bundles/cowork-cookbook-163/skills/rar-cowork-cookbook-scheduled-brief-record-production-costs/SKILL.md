---
name: "rar-cowork-cookbook-scheduled-brief-record-production-costs"
description: "Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_production_costs", "rar_sha256": "4d148fb950500ae9b24a6926dcc231c33fade7f1fc4868857f6ee39f32041344", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_record_production_costs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_record_production_costs_agent.py` and in the RCI capsule.

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

Record production costs Scheduled Email Brief — Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_production_costs_agent.py` and embedded as the fenced Python below (sha256 4d148fb950500ae9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_production_costs_agent.py` first:

```bash
python3 scheduled_brief_record_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_record_production_costs_agent.py   # or on stdin
python3 scheduled_brief_record_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record production costs Scheduled Email Brief — Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_record_production_costs',
    "version": '2.0.1',
    "display_name": 'Record production costs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-record-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d096694a4c9bc15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/record-production-costs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-record-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefRecordProductionCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRecordProductionCosts'
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
    print(ScheduledBriefRecordProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
