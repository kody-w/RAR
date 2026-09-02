---
name: "rar-cowork-cookbook-scheduled-brief-record-production-costs"
description: "Schedulable morning-brief email summarizing record production costs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_production_costs", "rar_sha256": "550b088a1fea0dc4eaa365a55da4502ea282d14a430811be4cacbe5d29fd93fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_record_production_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-record-production-costs:45f76086aa073ec96b3e527df2ede02f655f436452200234da83aff3f31693f8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_record_production_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_record_production_costs_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_production_costs_agent.py` and embedded as the fenced Python below (sha256 550b088a1fea0dc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_production_costs_agent.py` first:

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
    "version": '2.0.0',
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
