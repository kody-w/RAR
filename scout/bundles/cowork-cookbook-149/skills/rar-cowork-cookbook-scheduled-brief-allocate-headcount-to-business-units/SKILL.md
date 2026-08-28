---
name: "rar-cowork-cookbook-scheduled-brief-allocate-headcount-to-business-units"
description: "Schedulable morning-brief email summarizing allocate headcount to business units for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units", "rar_sha256": "8e09ea93771ff22ffcb6dc772f45606d840647b62d3579be66931a85fd193ebd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_allocate_headcount_to_business_units_agent.py` and embedded as the fenced Python below (sha256 8e09ea93771ff22f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_allocate_headcount_to_business_units_agent.py` first:

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
    "version": '2.0.0',
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
