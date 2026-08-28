---
name: "rar-cowork-cookbook-ppt-exec-take-inventory-on-hardware-and-devices"
description: "Generates an executive-ready PowerPoint deck on take inventory on hardware and devices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices", "rar_sha256": "73fc3b0f51a8710ef30a6e9e406f57bd743040cf2592199c425498606b1eabe0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` and embedded as the fenced Python below (sha256 73fc3b0f51a8710e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` first:

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
    "version": '2.0.1',
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
