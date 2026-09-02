---
name: "rar-cowork-cookbook-scheduled-brief-plan-fixed-assets"
description: "Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_fixed_assets", "rar_sha256": "6ebafb10e1e9c98668296c8bcfcc643161a9e3df293d10ce4c01da6b3570dedb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_plan_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-plan-fixed-assets:73670475e0eb574c2da93819268e8b3441b5399964921b646b5da6d3bfbb42cd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_plan_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_plan_fixed_assets_agent.py` is
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

Plan fixed assets Scheduled Email Brief — Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 6ebafb10e1e9c986…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_fixed_assets_agent.py` first:

```bash
python3 scheduled_brief_plan_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_fixed_assets_agent.py   # or on stdin
python3 scheduled_brief_plan_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan fixed assets Scheduled Email Brief — Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Plan fixed assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing plan fixed assets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07817134cfef3a41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-fixed-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-plan-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefPlanFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanFixedAssets'
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
    print(ScheduledBriefPlanFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
