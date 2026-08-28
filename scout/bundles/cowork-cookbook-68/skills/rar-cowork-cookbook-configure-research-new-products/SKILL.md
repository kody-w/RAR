---
name: "rar-cowork-cookbook-configure-research-new-products"
description: "Applies a bulk configuration change to research new products from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_research_new_products", "rar_sha256": "f8378fef10fff0152fca91db8b144509e00c514c6a4eff15b77f5f9566ab0244", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_research_new_products`. The original RAPP
agent is preserved byte-for-byte in `configure_research_new_products_agent.py` and in the RCI capsule.

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

Research new products Configuration Bulk Setup — Applies a bulk configuration change to research new products from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-research-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_research_new_products_agent.py` and embedded as the fenced Python below (sha256 f8378fef10fff015…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_research_new_products_agent.py` first:

```bash
python3 configure_research_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_research_new_products_agent.py   # or on stdin
python3 configure_research_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Research new products Configuration Bulk Setup — Applies a bulk configuration change to research new products from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-research-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_research_new_products',
    "version": '2.0.1',
    "display_name": 'Research new products Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to research new products from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-research-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-research-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e265543cf0c63d7c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/research-new-products'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-research-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureResearchNewProducts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureResearchNewProducts'
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
    print(ConfigureResearchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
