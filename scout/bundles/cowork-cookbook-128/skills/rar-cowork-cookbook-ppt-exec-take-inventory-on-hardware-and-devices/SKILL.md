---
name: "rar-cowork-cookbook-ppt-exec-take-inventory-on-hardware-and-devices"
description: "Generates an executive-ready PowerPoint deck on take inventory on hardware and devices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices", "rar_sha256": "2eb00bc67b4a5812e324ecc05ae0a34a48b18ef77fa7db94743c51ffce1a9afe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
