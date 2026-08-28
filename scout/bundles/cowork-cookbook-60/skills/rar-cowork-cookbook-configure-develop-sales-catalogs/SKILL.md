---
name: "rar-cowork-cookbook-configure-develop-sales-catalogs"
description: "Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_sales_catalogs", "rar_sha256": "bb08210cbd50f85c53ff10ed10d828cca2a83fd077ee6909a3ac39cad575370c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_sales_catalogs`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_sales_catalogs_agent.py` and in the RCI capsule.

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

Develop sales catalogs Configuration Bulk Setup — Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_sales_catalogs_agent.py` and embedded as the fenced Python below (sha256 bb08210cbd50f85c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_sales_catalogs_agent.py` first:

```bash
python3 configure_develop_sales_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_sales_catalogs_agent.py   # or on stdin
python3 configure_develop_sales_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales catalogs Configuration Bulk Setup — Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_sales_catalogs',
    "version": '2.0.1',
    "display_name": 'Develop sales catalogs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop sales catalogs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-sales-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-sales-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a413df5a0fdc726b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-catalogs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-develop-sales-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDevelopSalesCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopSalesCatalogs'
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
    print(ConfigureDevelopSalesCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
