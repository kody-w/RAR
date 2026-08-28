---
name: "rar-cowork-cookbook-configure-research-new-products"
description: "Applies a bulk configuration change to research new products from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_research_new_products", "rar_sha256": "49d78734e4eed1a23dc403b0db0f91f71f770c3fbec98bd4bd8ca757af2d8445", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_research_new_products_agent.py` and embedded as the fenced Python below (sha256 49d78734e4eed1a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_research_new_products_agent.py` first:

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
    "version": '2.0.0',
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
