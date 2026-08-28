---
name: "rar-cowork-cookbook-bulk-update-transfer-budgets"
description: "Applies a bulk field update across transfer budgets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_transfer_budgets", "rar_sha256": "a8b019ef9ddf06694c79c673cf6351bab47596689b24a185ae1eb1c80560803e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_transfer_budgets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_transfer_budgets_agent.py` and in the RCI capsule.

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

Transfer budgets Bulk Field Update — Applies a bulk field update across transfer budgets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-transfer-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_transfer_budgets_agent.py` and embedded as the fenced Python below (sha256 a8b019ef9ddf0669…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_transfer_budgets_agent.py` first:

```bash
python3 bulk_update_transfer_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_transfer_budgets_agent.py   # or on stdin
python3 bulk_update_transfer_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer budgets Bulk Field Update — Applies a bulk field update across transfer budgets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-transfer-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_transfer_budgets',
    "version": '2.0.1',
    "display_name": 'Transfer budgets Bulk Field Update',
    "description": 'Applies a bulk field update across transfer budgets records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-transfer-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-transfer-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1dd97b618b1bad97',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/transfer-budgets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-transfer-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateTransferBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateTransferBudgets'
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
    print(BulkUpdateTransferBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
