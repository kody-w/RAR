---
name: "rar-cowork-cookbook-configure-configure-and-manage-iot-devices"
description: "Applies a bulk configuration change to configure and manage IoT devices from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_iot_devices", "rar_sha256": "4ac9df29276dbd5a234799a4e86ba7f355acb5313616564b91c34e1b85e40a4c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_manage_iot_devices_agent.py` and embedded as the fenced Python below (sha256 4ac9df29276dbd5a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_manage_iot_devices_agent.py` first:

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
    "version": '2.0.0',
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
