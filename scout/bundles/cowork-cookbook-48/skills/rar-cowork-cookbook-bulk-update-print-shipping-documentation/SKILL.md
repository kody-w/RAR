---
name: "rar-cowork-cookbook-bulk-update-print-shipping-documentation"
description: "Applies a bulk field update across print shipping documentation records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_print_shipping_documentation", "rar_sha256": "76d6edb90dbc4076065ed406ea8635ff9186c693f77b58c35972d8fb395a00c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_print_shipping_documentation`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_print_shipping_documentation_agent.py` and in the RCI capsule.

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

Print shipping documentation Bulk Field Update — Applies a bulk field update across print shipping documentation records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_print_shipping_documentation_agent.py` and embedded as the fenced Python below (sha256 76d6edb90dbc4076…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_print_shipping_documentation_agent.py` first:

```bash
python3 bulk_update_print_shipping_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_print_shipping_documentation_agent.py   # or on stdin
python3 bulk_update_print_shipping_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Print shipping documentation Bulk Field Update — Applies a bulk field update across print shipping documentation records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_print_shipping_documentation',
    "version": '2.0.0',
    "display_name": 'Print shipping documentation Bulk Field Update',
    "description": 'Applies a bulk field update across print shipping documentation records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-print-shipping-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-print-shipping-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1102735674802649',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/print-shipping-documentation'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-print-shipping-documentation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePrintShippingDocumentation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePrintShippingDocumentation'
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
    print(BulkUpdatePrintShippingDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
