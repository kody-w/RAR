---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-iot-devices"
description: "Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_iot_devices", "rar_sha256": "2a69eff6344abd6c08c74a12ad82c286c9f9a92794e6f24867ebfed2421dbdcc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_manage_iot_devices`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_manage_iot_devices_agent.py` and in the RCI capsule.

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

Configure and manage IoT devices Bulk Field Update — Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_manage_iot_devices_agent.py` and embedded as the fenced Python below (sha256 2a69eff6344abd6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_manage_iot_devices_agent.py` first:

```bash
python3 bulk_update_configure_and_manage_iot_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_manage_iot_devices_agent.py   # or on stdin
python3 bulk_update_configure_and_manage_iot_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage IoT devices Bulk Field Update — Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_manage_iot_devices',
    "version": '2.0.0',
    "display_name": 'Configure and manage IoT devices Bulk Field Update',
    "description": 'Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-configure-and-manage-iot-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ababc757752c640',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-iot-devices'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-manage-iot-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConfigureAndManageIotDevices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndManageIotDevices'
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
    print(BulkUpdateConfigureAndManageIotDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
