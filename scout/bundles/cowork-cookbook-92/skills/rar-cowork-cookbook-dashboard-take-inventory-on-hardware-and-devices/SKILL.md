---
name: "rar-cowork-cookbook-dashboard-take-inventory-on-hardware-and-devices"
description: "Produces a self-contained interactive HTML dashboard for take inventory on hardware and devices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices", "rar_sha256": "472d91ce7834bebb031c0b821fd4e2e4b03675a3df108ae98e93ac86cd09e5ea", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_take_inventory_on_hardware_and_devices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-take-inventory-on-hardware-and-devices:db49a2c8af15e23f2df1b300284ac5a189337f0daf805975c07bf3f2066a5faa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_take_inventory_on_hardware_and_devices_agent.py` is
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
