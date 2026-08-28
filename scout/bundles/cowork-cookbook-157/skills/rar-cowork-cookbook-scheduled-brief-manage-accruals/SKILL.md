---
name: "rar-cowork-cookbook-scheduled-brief-manage-accruals"
description: "Schedulable morning-brief email summarizing manage accruals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_accruals", "rar_sha256": "a855c07e6818848981a8d2e2a1b5ba00741208a35c6577498ad89e9ca74e9408", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_accruals_agent.py` and embedded as the fenced Python below (sha256 a855c07e68188489…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_accruals_agent.py` first:

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
    "version": '2.0.1',
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
