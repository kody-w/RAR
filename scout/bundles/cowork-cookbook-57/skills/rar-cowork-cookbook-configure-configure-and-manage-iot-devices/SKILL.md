---
name: "rar-cowork-cookbook-configure-configure-and-manage-iot-devices"
description: "Applies a bulk configuration change to configure and manage IoT devices from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_iot_devices", "rar_sha256": "4ac9df29276dbd5a234799a4e86ba7f355acb5313616564b91c34e1b85e40a4c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_configure_and_manage_iot_devices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-configure-and-manage-iot-devices:9701488ae784313132e4e9c1889181b6ff1c46506e919f4de2de830dd4029037", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_configure_and_manage_iot_devices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_configure_and_manage_iot_devices_agent.py` is
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
