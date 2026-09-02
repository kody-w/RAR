---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-iot-devices"
description: "Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_iot_devices", "rar_sha256": "2a69eff6344abd6c08c74a12ad82c286c9f9a92794e6f24867ebfed2421dbdcc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_configure_and_manage_iot_devices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-configure-and-manage-iot-devices:181b78cc92f1e04b5a4188b34c86f7b57abaeca61f2edd86a8a2946f1302a37d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_configure_and_manage_iot_devices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_configure_and_manage_iot_devices_agent.py` is
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
