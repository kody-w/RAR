---
name: "rar-cowork-cookbook-bulk-update-perform-ledger-settlements"
description: "Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_ledger_settlements", "rar_sha256": "e3ff1c3faf789a46bb8e65964fb2f8634d1d860c49c8a33cc20f826611a8a1da", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_perform_ledger_settlements`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_perform_ledger_settlements_agent.py` and in the RCI capsule.

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

Perform ledger settlements Bulk Field Update — Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_ledger_settlements_agent.py` and embedded as the fenced Python below (sha256 e3ff1c3faf789a46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_ledger_settlements_agent.py` first:

```bash
python3 bulk_update_perform_ledger_settlements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_perform_ledger_settlements_agent.py   # or on stdin
python3 bulk_update_perform_ledger_settlements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform ledger settlements Bulk Field Update — Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_perform_ledger_settlements',
    "version": '2.0.0',
    "display_name": 'Perform ledger settlements Bulk Field Update',
    "description": 'Applies a bulk field update across perform ledger settlements records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-perform-ledger-settlements',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-perform-ledger-settlements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '08d800f10b0d47bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/perform-ledger-settlements'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-perform-ledger-settlements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePerformLedgerSettlements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePerformLedgerSettlements'
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
    print(BulkUpdatePerformLedgerSettlements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
