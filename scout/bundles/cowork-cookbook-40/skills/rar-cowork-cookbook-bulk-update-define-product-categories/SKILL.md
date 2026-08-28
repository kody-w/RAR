---
name: "rar-cowork-cookbook-bulk-update-define-product-categories"
description: "Applies a bulk field update across define product categories records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_product_categories", "rar_sha256": "c12ea9c23371357b65d0c409e2cd2a4fb8bc17f571b2992c43f9b64c3827e298", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_product_categories`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_product_categories_agent.py` and in the RCI capsule.

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

Define product categories Bulk Field Update — Applies a bulk field update across define product categories records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-product-categories
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_product_categories_agent.py` and embedded as the fenced Python below (sha256 c12ea9c23371357b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_product_categories_agent.py` first:

```bash
python3 bulk_update_define_product_categories_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_product_categories_agent.py   # or on stdin
python3 bulk_update_define_product_categories_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product categories Bulk Field Update — Applies a bulk field update across define product categories records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-product-categories
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_product_categories',
    "version": '2.0.1',
    "display_name": 'Define product categories Bulk Field Update',
    "description": 'Applies a bulk field update across define product categories records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-product-categories',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-product-categories',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5808af6dc833a0e8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-categories'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-define-product-categories', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineProductCategories(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineProductCategories'
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
    print(BulkUpdateDefineProductCategories().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
