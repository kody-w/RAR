---
name: "rar-cowork-cookbook-configure-define-product-categories"
description: "Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_product_categories", "rar_sha256": "2c463845c8d32048eef8e725939b6d88e89bac1cb6a03984b480d48172a46828", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_product_categories_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-product-categories:a32a7d350e55f6f985b95139873c2a17e0ebfae72029e5d762b27fd4cdaaa70d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_product_categories`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_product_categories_agent.py` is
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

Define product categories Configuration Bulk Setup — Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-product-categories
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_product_categories_agent.py` and embedded as the fenced Python below (sha256 2c463845c8d32048…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_product_categories_agent.py` first:

```bash
python3 configure_define_product_categories_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_product_categories_agent.py   # or on stdin
python3 configure_define_product_categories_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product categories Configuration Bulk Setup — Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-product-categories
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_product_categories',
    "version": '2.0.0',
    "display_name": 'Define product categories Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-product-categories',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-product-categories',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f226c24cb3c350a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-categories'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-define-product-categories', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefineProductCategories(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineProductCategories'
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
    print(ConfigureDefineProductCategories().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
