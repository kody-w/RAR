---
name: "rar-cowork-cookbook-bulk-update-process-allocations"
description: "Applies a bulk field update across process allocations records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_allocations", "rar_sha256": "05d28e75662209767fd8fca24cc7c021e868cae65108f4fe460ff66bb486b3ed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_process_allocations`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_process_allocations_agent.py` and in the RCI capsule.

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
