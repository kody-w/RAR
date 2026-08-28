---
name: "rar-cowork-cookbook-configure-define-product-categories"
description: "Applies a bulk configuration change to define product categories from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_product_categories", "rar_sha256": "2c463845c8d32048eef8e725939b6d88e89bac1cb6a03984b480d48172a46828", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_product_categories`. The original RAPP
agent is preserved byte-for-byte in `configure_define_product_categories_agent.py` and in the RCI capsule.

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
