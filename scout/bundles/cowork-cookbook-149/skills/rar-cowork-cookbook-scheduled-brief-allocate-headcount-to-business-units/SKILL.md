---
name: "rar-cowork-cookbook-scheduled-brief-allocate-headcount-to-business-units"
description: "Schedulable morning-brief email summarizing allocate headcount to business units for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units", "rar_sha256": "31f73e9688d58a0d5d19e1d49dc631c78e6b75ecb5bb602f30bb907c58258f8f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_allocate_headcount_to_business_units_agent.py` and in the RCI capsule.

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

Allocate headcount to business units Scheduled Email Brief — Schedulable morning-brief email summarizing allocate headcount to business units for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-allocate-headcount-to-business-units
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_allocate_headcount_to_business_units_agent.py` and embedded as the fenced Python below (sha256 31f73e9688d58a0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_allocate_headcount_to_business_units_agent.py` first:

```bash
python3 scheduled_brief_allocate_headcount_to_business_units_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_allocate_headcount_to_business_units_agent.py   # or on stdin
python3 scheduled_brief_allocate_headcount_to_business_units_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate headcount to business units Scheduled Email Brief — Schedulable morning-brief email summarizing allocate headcount to business units for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-allocate-headcount-to-business-units
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units',
    "version": '2.0.1',
    "display_name": 'Allocate headcount to business units Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing allocate headcount to business units for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-allocate-headcount-to-business-units',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-allocate-headcount-to-business-units',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b0cafc641bb82117',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/allocate-headcount-to-business-units'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-allocate-headcount-to-business-units', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefAllocateHeadcountToBusinessUnits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAllocateHeadcountToBusinessUnits'
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
    print(ScheduledBriefAllocateHeadcountToBusinessUnits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
