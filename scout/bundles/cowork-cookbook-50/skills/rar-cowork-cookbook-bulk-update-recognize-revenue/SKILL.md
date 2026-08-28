---
name: "rar-cowork-cookbook-bulk-update-recognize-revenue"
description: "Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_recognize_revenue", "rar_sha256": "c30f1be7ab60c7560c9bbe32682ce871d06ceba2fa9cbcdd4094fda775a52603", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_recognize_revenue`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_recognize_revenue_agent.py` and in the RCI capsule.

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

Recognize revenue Bulk Field Update — Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-recognize-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_recognize_revenue_agent.py` and embedded as the fenced Python below (sha256 c30f1be7ab60c756…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_recognize_revenue_agent.py` first:

```bash
python3 bulk_update_recognize_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_recognize_revenue_agent.py   # or on stdin
python3 bulk_update_recognize_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize revenue Bulk Field Update — Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-recognize-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_recognize_revenue',
    "version": '2.0.1',
    "display_name": 'Recognize revenue Bulk Field Update',
    "description": 'Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-recognize-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-recognize-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a05d801d8a420018',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/recognize-revenue'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-recognize-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRecognizeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecognizeRevenue'
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
    print(BulkUpdateRecognizeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
