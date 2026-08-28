---
name: "rar-cowork-cookbook-bulk-update-reimburse-workers-for-expenses"
description: "Applies a bulk field update across reimburse workers for expenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reimburse_workers_for_expenses", "rar_sha256": "dd828c1cec9c5907bab5145b686da8a89b92917492a243d4fd6efa07c2dfc01f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reimburse_workers_for_expenses_agent.py` and embedded as the fenced Python below (sha256 dd828c1cec9c5907…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reimburse_workers_for_expenses_agent.py` first:

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
    "version": '2.0.1',
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
