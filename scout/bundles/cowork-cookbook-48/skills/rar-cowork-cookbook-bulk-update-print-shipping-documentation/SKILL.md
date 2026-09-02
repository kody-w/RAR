---
name: "rar-cowork-cookbook-bulk-update-print-shipping-documentation"
description: "Applies a bulk field update across print shipping documentation records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_print_shipping_documentation", "rar_sha256": "76d6edb90dbc4076065ed406ea8635ff9186c693f77b58c35972d8fb395a00c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_print_shipping_documentation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-print-shipping-documentation:cbf40cbb0f291a0ca77a6320147b830219cd42e9f4140b323190d71c36c0b96b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_print_shipping_documentation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_print_shipping_documentation_agent.py` is
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
