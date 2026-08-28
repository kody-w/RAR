---
name: "rar-cowork-cookbook-configure-take-inventory-on-software-licenses"
description: "Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_take_inventory_on_software_licenses", "rar_sha256": "2d42da4f2b4f70e2e3ab8f8493dfcf62023c0aa50b00922639ec86d44f1f97ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_take_inventory_on_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `configure_take_inventory_on_software_licenses_agent.py` and in the RCI capsule.

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

Take inventory on software licenses Configuration Bulk Setup — Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_take_inventory_on_software_licenses_agent.py` and embedded as the fenced Python below (sha256 2d42da4f2b4f70e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_take_inventory_on_software_licenses_agent.py` first:

```bash
python3 configure_take_inventory_on_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_take_inventory_on_software_licenses_agent.py   # or on stdin
python3 configure_take_inventory_on_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on software licenses Configuration Bulk Setup — Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_take_inventory_on_software_licenses',
    "version": '2.0.0',
    "display_name": 'Take inventory on software licenses Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-take-inventory-on-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3fdc1cecb5ad3716',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-software-licenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-take-inventory-on-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureTakeInventoryOnSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTakeInventoryOnSoftwareLicenses'
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
    print(ConfigureTakeInventoryOnSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
