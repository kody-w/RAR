---
name: "rar-cowork-cookbook-ppt-exec-take-inventory-on-hardware-and-devices"
description: "Generates an executive-ready PowerPoint deck on take inventory on hardware and devices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices", "rar_sha256": "2eb00bc67b4a5812e324ecc05ae0a34a48b18ef77fa7db94743c51ffce1a9afe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_take_inventory_on_hardware_and_devices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-take-inventory-on-hardware-and-devices:9b28280f666bb737634eb9ad2574013d47098a33571a7cfa6b23a21356e4490b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` is
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

Take inventory on hardware and devices Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on take inventory on hardware and devices status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-take-inventory-on-hardware-and-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` and embedded as the fenced Python below (sha256 2eb00bc67b4a5812…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` first:

```bash
python3 ppt_exec_take_inventory_on_hardware_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_take_inventory_on_hardware_and_devices_agent.py   # or on stdin
python3 ppt_exec_take_inventory_on_hardware_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on hardware and devices Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on take inventory on hardware and devices status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-take-inventory-on-hardware-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices',
    "version": '2.0.0',
    "display_name": 'Take inventory on hardware and devices Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on take inventory on hardware and devices status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-take-inventory-on-hardware-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-take-inventory-on-hardware-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16d366ef798f0a88',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-hardware-and-devices'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-take-inventory-on-hardware-and-devices', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecTakeInventoryOnHardwareAndDevices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTakeInventoryOnHardwareAndDevices'
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
    print(PptExecTakeInventoryOnHardwareAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
