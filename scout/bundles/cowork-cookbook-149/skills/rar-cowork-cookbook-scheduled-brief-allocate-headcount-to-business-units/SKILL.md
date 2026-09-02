---
name: "rar-cowork-cookbook-scheduled-brief-allocate-headcount-to-business-units"
description: "Schedulable morning-brief email summarizing allocate headcount to business units for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units", "rar_sha256": "8e09ea93771ff22ffcb6dc772f45606d840647b62d3579be66931a85fd193ebd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_allocate_headcount_to_business_units_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-allocate-headcount-to-business-units:a3d94eea0fd01ae70eea29f52bda89b174e47827d71ebf85e79453bbbba231fb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_allocate_headcount_to_business_units_agent.py` is
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
