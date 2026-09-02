---
name: "rar-cowork-cookbook-bulk-update-transfer-budgets"
description: "Applies a bulk field update across transfer budgets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_transfer_budgets", "rar_sha256": "ca0d31a957498cf5b0095f70f0bfe3b98223ea796418df8c07e4a310c843d137", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_transfer_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-transfer-budgets:36500bf0482ffb34facd997285cbb4108991e1c9f20421db94660194a3153d75", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_transfer_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_transfer_budgets_agent.py` is
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
