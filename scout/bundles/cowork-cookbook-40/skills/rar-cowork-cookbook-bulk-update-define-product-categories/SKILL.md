---
name: "rar-cowork-cookbook-bulk-update-define-product-categories"
description: "Applies a bulk field update across define product categories records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_product_categories", "rar_sha256": "402473a1f2ba9679b286a4ea1f5893df0a547f47ffb49840e031bfa081873bb5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_product_categories_agent.py` and embedded as the fenced Python below (sha256 402473a1f2ba9679…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_product_categories_agent.py` first:

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
    "version": '2.0.0',
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
