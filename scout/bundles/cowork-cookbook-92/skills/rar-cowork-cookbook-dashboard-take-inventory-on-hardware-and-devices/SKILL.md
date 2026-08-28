---
name: "rar-cowork-cookbook-dashboard-take-inventory-on-hardware-and-devices"
description: "Produces a self-contained interactive HTML dashboard for take inventory on hardware and devices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices", "rar_sha256": "472d91ce7834bebb031c0b821fd4e2e4b03675a3df108ae98e93ac86cd09e5ea", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_take_inventory_on_hardware_and_devices_agent.py` and embedded as the fenced Python below (sha256 472d91ce7834bebb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_take_inventory_on_hardware_and_devices_agent.py` first:

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
    "version": '2.0.0',
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
