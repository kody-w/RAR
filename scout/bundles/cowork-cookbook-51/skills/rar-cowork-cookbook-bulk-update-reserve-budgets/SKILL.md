---
name: "rar-cowork-cookbook-bulk-update-reserve-budgets"
description: "Applies a bulk field update across reserve budgets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reserve_budgets", "rar_sha256": "9c16124a42edcf23e728fbb5c1b3833089a2836ec9e779aaff2958b2ed5765fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reserve_budgets_agent.py` and embedded as the fenced Python below (sha256 9c16124a42edcf23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reserve_budgets_agent.py` first:

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
    "version": '2.0.0',
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
