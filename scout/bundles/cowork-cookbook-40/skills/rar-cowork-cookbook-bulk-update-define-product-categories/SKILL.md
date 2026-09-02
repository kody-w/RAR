---
name: "rar-cowork-cookbook-bulk-update-define-product-categories"
description: "Applies a bulk field update across define product categories records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_product_categories", "rar_sha256": "402473a1f2ba9679b286a4ea1f5893df0a547f47ffb49840e031bfa081873bb5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_product_categories_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-product-categories:d85fef815d085f50619a8a3192f9a1ea5ed0becb3cb869121cbb8d87b57c6765", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_product_categories`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_product_categories_agent.py` is
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
