---
name: "rar-cowork-cookbook-bulk-update-reimburse-workers-for-expenses"
description: "Applies a bulk field update across reimburse workers for expenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reimburse_workers_for_expenses", "rar_sha256": "77f0dbd20b75923ef1fd4538ddeabb583e053e3ca32cb0c08d63b61b19d95b6a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reimburse_workers_for_expenses`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reimburse_workers_for_expenses_agent.py` and in the RCI capsule.

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
