---
name: "rar-cowork-cookbook-bulk-update-print-shipping-documentation"
description: "Applies a bulk field update across print shipping documentation records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_print_shipping_documentation", "rar_sha256": "52b98e274cd80a33d7132f1b2762c73af9621a927241d7e5d15f711f5f40e9a3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_print_shipping_documentation_agent.py` and embedded as the fenced Python below (sha256 52b98e274cd80a33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_print_shipping_documentation_agent.py` first:

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
    "version": '2.0.1',
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
