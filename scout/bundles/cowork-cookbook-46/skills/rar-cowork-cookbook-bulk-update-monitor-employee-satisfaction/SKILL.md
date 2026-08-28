---
name: "rar-cowork-cookbook-bulk-update-monitor-employee-satisfaction"
description: "Applies a bulk field update across monitor employee satisfaction records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_employee_satisfaction", "rar_sha256": "636cf2a9affed0f3b66075f3ca5113ba71c26fe5345756cb0ce33439c73f64e2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_employee_satisfaction`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_employee_satisfaction_agent.py` and in the RCI capsule.

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

Monitor employee satisfaction Bulk Field Update — Applies a bulk field update across monitor employee satisfaction records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-employee-satisfaction
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_employee_satisfaction_agent.py` and embedded as the fenced Python below (sha256 636cf2a9affed0f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_employee_satisfaction_agent.py` first:

```bash
python3 bulk_update_monitor_employee_satisfaction_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_employee_satisfaction_agent.py   # or on stdin
python3 bulk_update_monitor_employee_satisfaction_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor employee satisfaction Bulk Field Update — Applies a bulk field update across monitor employee satisfaction records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-employee-satisfaction
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_employee_satisfaction',
    "version": '2.0.1',
    "display_name": 'Monitor employee satisfaction Bulk Field Update',
    "description": 'Applies a bulk field update across monitor employee satisfaction records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-employee-satisfaction',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-employee-satisfaction',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd6c9531a8da18b41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-employee-satisfaction'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-monitor-employee-satisfaction', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateMonitorEmployeeSatisfaction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorEmployeeSatisfaction'
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
    print(BulkUpdateMonitorEmployeeSatisfaction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
