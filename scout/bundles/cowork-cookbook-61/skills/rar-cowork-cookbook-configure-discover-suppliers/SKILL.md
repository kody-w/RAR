---
name: "rar-cowork-cookbook-configure-discover-suppliers"
description: "Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_discover_suppliers", "rar_sha256": "48775ad2bdf996a92bf0b4d6580d440c6b8c2d711140fe242be3f4284f6ddf33", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_discover_suppliers`. The original RAPP
agent is preserved byte-for-byte in `configure_discover_suppliers_agent.py` and in the RCI capsule.

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

Discover suppliers Configuration Bulk Setup — Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-discover-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_discover_suppliers_agent.py` and embedded as the fenced Python below (sha256 48775ad2bdf996a9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_discover_suppliers_agent.py` first:

```bash
python3 configure_discover_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_discover_suppliers_agent.py   # or on stdin
python3 configure_discover_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Discover suppliers Configuration Bulk Setup — Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-discover-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_discover_suppliers',
    "version": '2.0.1',
    "display_name": 'Discover suppliers Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to discover suppliers from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-discover-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-discover-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cf8ae9b64d22d60f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/discover-suppliers'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-discover-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDiscoverSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDiscoverSuppliers'
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
    print(ConfigureDiscoverSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
