---
name: "rar-cowork-cookbook-bulk-update-reimburse-workers-for-expenses"
description: "Applies a bulk field update across reimburse workers for expenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reimburse_workers_for_expenses", "rar_sha256": "77f0dbd20b75923ef1fd4538ddeabb583e053e3ca32cb0c08d63b61b19d95b6a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_reimburse_workers_for_expenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-reimburse-workers-for-expenses:e5959f88f7129b60808d913d021517d0538efca5eae2f844621b5fff788ed116", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_reimburse_workers_for_expenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_reimburse_workers_for_expenses_agent.py` is
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

Reimburse workers for expenses Bulk Field Update — Applies a bulk field update across reimburse workers for expenses records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reimburse-workers-for-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reimburse_workers_for_expenses_agent.py` and embedded as the fenced Python below (sha256 77f0dbd20b75923e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reimburse_workers_for_expenses_agent.py` first:

```bash
python3 bulk_update_reimburse_workers_for_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reimburse_workers_for_expenses_agent.py   # or on stdin
python3 bulk_update_reimburse_workers_for_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reimburse workers for expenses Bulk Field Update — Applies a bulk field update across reimburse workers for expenses records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reimburse-workers-for-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reimburse_workers_for_expenses',
    "version": '2.0.0',
    "display_name": 'Reimburse workers for expenses Bulk Field Update',
    "description": 'Applies a bulk field update across reimburse workers for expenses records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-reimburse-workers-for-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reimburse-workers-for-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '70150b38d739c429',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/reimburse-workers-for-expenses'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-reimburse-workers-for-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateReimburseWorkersForExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReimburseWorkersForExpenses'
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
    print(BulkUpdateReimburseWorkersForExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
