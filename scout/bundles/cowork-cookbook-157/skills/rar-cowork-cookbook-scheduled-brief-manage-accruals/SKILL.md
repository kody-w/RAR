---
name: "rar-cowork-cookbook-scheduled-brief-manage-accruals"
description: "Schedulable morning-brief email summarizing manage accruals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_accruals", "rar_sha256": "283d3c0428dbb5f8b9e881c46c79c8f93723d7445051059f7b1a2f5c4a47a95c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_accruals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-accruals:98af929870dd21cd1396b69282f70eaa989175007f629efe1f27ef4c21881942", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_accruals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_accruals_agent.py` is
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

Manage accruals Scheduled Email Brief — Schedulable morning-brief email summarizing manage accruals for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_accruals_agent.py` and embedded as the fenced Python below (sha256 283d3c0428dbb5f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_accruals_agent.py` first:

```bash
python3 scheduled_brief_manage_accruals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_accruals_agent.py   # or on stdin
python3 scheduled_brief_manage_accruals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage accruals Scheduled Email Brief — Schedulable morning-brief email summarizing manage accruals for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_accruals',
    "version": '2.0.0',
    "display_name": 'Manage accruals Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage accruals for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-manage-accruals',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6a505bf6cd703e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-accruals'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-manage-accruals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefManageAccruals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageAccruals'
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
    print(ScheduledBriefManageAccruals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
