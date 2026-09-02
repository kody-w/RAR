---
name: "rar-cowork-cookbook-bulk-update-process-allocations"
description: "Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_allocations", "rar_sha256": "05d28e75662209767fd8fca24cc7c021e868cae65108f4fe460ff66bb486b3ed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_process_allocations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-process-allocations:9cc49262b9c3223f0718fd580736c31e591ede288eeaefe9d15a236f1648f201", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_process_allocations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_process_allocations_agent.py` is
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

Process allocations Bulk Field Update — Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-allocations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_process_allocations_agent.py` and embedded as the fenced Python below (sha256 05d28e7566220976…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_process_allocations_agent.py` first:

```bash
python3 bulk_update_process_allocations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_process_allocations_agent.py   # or on stdin
python3 bulk_update_process_allocations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process allocations Bulk Field Update — Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-allocations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_process_allocations',
    "version": '2.0.0',
    "display_name": 'Process allocations Bulk Field Update',
    "description": 'Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-process-allocations',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-process-allocations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34f883f5cc672caf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/process-allocations'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-process-allocations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateProcessAllocations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateProcessAllocations'
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
    print(BulkUpdateProcessAllocations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
