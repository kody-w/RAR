---
name: "rar-cowork-cookbook-configure-research-new-products"
description: "Applies a bulk configuration change to research new products from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_research_new_products", "rar_sha256": "49d78734e4eed1a23dc403b0db0f91f71f770c3fbec98bd4bd8ca757af2d8445", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_research_new_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-research-new-products:1e799f5f881046ca0915ae5f91f5c64236f887e7e976e0d3683dbe83338b122b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_research_new_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_research_new_products_agent.py` is
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
