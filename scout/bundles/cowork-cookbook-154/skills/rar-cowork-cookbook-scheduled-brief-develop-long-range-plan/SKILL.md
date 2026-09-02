---
name: "rar-cowork-cookbook-scheduled-brief-develop-long-range-plan"
description: "Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_long_range_plan", "rar_sha256": "4bdfcc4e6cce452593d4e76cea53afcd60812783526748092ede881cf928e093", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_long_range_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-long-range-plan:586bd81ad97361a078ed77f766341872d89fecb4638bc9241c7948f96ffc0fc3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_long_range_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_long_range_plan_agent.py` is
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

Develop long-range plan Scheduled Email Brief — Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_long_range_plan_agent.py` and embedded as the fenced Python below (sha256 4bdfcc4e6cce4525…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_long_range_plan_agent.py` first:

```bash
python3 scheduled_brief_develop_long_range_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_long_range_plan_agent.py   # or on stdin
python3 scheduled_brief_develop_long_range_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop long-range plan Scheduled Email Brief — Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_long_range_plan',
    "version": '2.0.0',
    "display_name": 'Develop long-range plan Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-develop-long-range-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e5ed0185cc1fabf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-long-range-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-develop-long-range-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDevelopLongRangePlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopLongRangePlan'
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
    print(ScheduledBriefDevelopLongRangePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
