---
name: "rar-cowork-cookbook-bulk-update-transfer-budgets"
description: "Applies a bulk field update across transfer budgets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_transfer_budgets", "rar_sha256": "ca0d31a957498cf5b0095f70f0bfe3b98223ea796418df8c07e4a310c843d137", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_transfer_budgets_agent.py` and embedded as the fenced Python below (sha256 ca0d31a957498cf5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_transfer_budgets_agent.py` first:

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
    "version": '2.0.0',
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
