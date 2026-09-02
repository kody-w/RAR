---
name: "rar-cowork-cookbook-bulk-update-monitor-employee-satisfaction"
description: "Applies a bulk field update across monitor employee satisfaction records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_employee_satisfaction", "rar_sha256": "0f87cefc7045a1332064ec1ecd6dce06a014db8e41a9794c41fe286a61919656", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_monitor_employee_satisfaction_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-monitor-employee-satisfaction:759704bffcd66bf4041e3398ca5dc70517b88c286ab5965a3f98f24e3db28bdf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_monitor_employee_satisfaction`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_monitor_employee_satisfaction_agent.py` is
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
