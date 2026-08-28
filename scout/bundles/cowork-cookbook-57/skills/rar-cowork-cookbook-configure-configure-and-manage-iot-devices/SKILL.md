---
name: "rar-cowork-cookbook-configure-configure-and-manage-iot-devices"
description: "Applies a bulk configuration change to configure and manage IoT devices from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_iot_devices", "rar_sha256": "d086ef4185012ea0346272970f35cd2b8875e025b57ebfc690a3ecaad6f0cee2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_and_manage_iot_devices`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_and_manage_iot_devices_agent.py` and in the RCI capsule.

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

Configure and manage IoT devices Configuration Bulk Setup — Applies a bulk configuration change to configure and manage IoT devices from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-iot-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_manage_iot_devices_agent.py` and embedded as the fenced Python below (sha256 d086ef4185012ea0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_manage_iot_devices_agent.py` first:

```bash
python3 configure_configure_and_manage_iot_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_and_manage_iot_devices_agent.py   # or on stdin
python3 configure_configure_and_manage_iot_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage IoT devices Configuration Bulk Setup — Applies a bulk configuration change to configure and manage IoT devices from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-iot-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_and_manage_iot_devices',
    "version": '2.0.1',
    "display_name": 'Configure and manage IoT devices Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to configure and manage IoT devices from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-configure-and-manage-iot-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-and-manage-iot-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '330648d9575b348b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-iot-devices'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-and-manage-iot-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureConfigureAndManageIotDevices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureAndManageIotDevices'
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
    print(ConfigureConfigureAndManageIotDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
