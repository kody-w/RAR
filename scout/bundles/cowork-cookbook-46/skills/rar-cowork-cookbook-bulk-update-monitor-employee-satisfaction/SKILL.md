---
name: "rar-cowork-cookbook-bulk-update-monitor-employee-satisfaction"
description: "Applies a bulk field update across monitor employee satisfaction records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_employee_satisfaction", "rar_sha256": "0f87cefc7045a1332064ec1ecd6dce06a014db8e41a9794c41fe286a61919656", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_employee_satisfaction_agent.py` and embedded as the fenced Python below (sha256 0f87cefc7045a133…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_employee_satisfaction_agent.py` first:

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
    "version": '2.0.0',
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
