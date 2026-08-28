---
name: "rar-cowork-cookbook-bulk-update-reserve-budgets"
description: "Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reserve_budgets", "rar_sha256": "08563f1ae686e6ea9a79db069d5f9ff14710ef80b9f847a17541e023275766b8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reserve_budgets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reserve_budgets_agent.py` and in the RCI capsule.

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

Reserve budgets Bulk Field Update — Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reserve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reserve_budgets_agent.py` and embedded as the fenced Python below (sha256 08563f1ae686e6ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reserve_budgets_agent.py` first:

```bash
python3 bulk_update_reserve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reserve_budgets_agent.py   # or on stdin
python3 bulk_update_reserve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reserve budgets Bulk Field Update — Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reserve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reserve_budgets',
    "version": '2.0.1',
    "display_name": 'Reserve budgets Bulk Field Update',
    "description": 'Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-reserve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reserve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b06ea583b0e06b5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/reserve-budgets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-reserve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateReserveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReserveBudgets'
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
    print(BulkUpdateReserveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
