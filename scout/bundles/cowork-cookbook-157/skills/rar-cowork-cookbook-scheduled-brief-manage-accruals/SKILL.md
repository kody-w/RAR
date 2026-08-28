---
name: "rar-cowork-cookbook-scheduled-brief-manage-accruals"
description: "Schedulable morning-brief email summarizing manage accruals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_accruals", "rar_sha256": "283d3c0428dbb5f8b9e881c46c79c8f93723d7445051059f7b1a2f5c4a47a95c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_accruals`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_accruals_agent.py` and in the RCI capsule.

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
