---
name: "rar-cowork-cookbook-dashboard-take-inventory-on-hardware-and-devices"
description: "Produces a self-contained interactive HTML dashboard for take inventory on hardware and devices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices", "rar_sha256": "d09270541166a179af3ee3b3a00f7618f57280c456832bf123698b8bff79a9d1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices`. The original RAPP
agent is preserved byte-for-byte in `dashboard_take_inventory_on_hardware_and_devices_agent.py` and in the RCI capsule.

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

Take inventory on hardware and devices Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for take inventory on hardware and devices - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-take-inventory-on-hardware-and-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_take_inventory_on_hardware_and_devices_agent.py` and embedded as the fenced Python below (sha256 d09270541166a179…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_take_inventory_on_hardware_and_devices_agent.py` first:

```bash
python3 dashboard_take_inventory_on_hardware_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_take_inventory_on_hardware_and_devices_agent.py   # or on stdin
python3 dashboard_take_inventory_on_hardware_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on hardware and devices Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for take inventory on hardware and devices - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-take-inventory-on-hardware-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices',
    "version": '2.0.1',
    "display_name": 'Take inventory on hardware and devices Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for take inventory on hardware and devices - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-take-inventory-on-hardware-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-take-inventory-on-hardware-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b411c88df52fd55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-hardware-and-devices'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-take-inventory-on-hardware-and-devices', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardTakeInventoryOnHardwareAndDevices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardTakeInventoryOnHardwareAndDevices'
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
    print(DashboardTakeInventoryOnHardwareAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
