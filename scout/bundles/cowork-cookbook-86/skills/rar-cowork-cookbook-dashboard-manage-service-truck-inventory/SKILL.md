---
name: "rar-cowork-cookbook-dashboard-manage-service-truck-inventory"
description: "Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_service_truck_inventory", "rar_sha256": "f812a7127b078c4ed0c8a82d337e7dfd5298ff2a5652d588d4e24b95f4a980ef", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_service_truck_inventory`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_service_truck_inventory_agent.py` and in the RCI capsule.

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

Manage service truck inventory Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 f812a7127b078c4e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_service_truck_inventory_agent.py` first:

```bash
python3 dashboard_manage_service_truck_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_service_truck_inventory_agent.py   # or on stdin
python3 dashboard_manage_service_truck_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service truck inventory Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_service_truck_inventory',
    "version": '2.0.1',
    "display_name": 'Manage service truck inventory Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-service-truck-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34dba2330dd432c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/manage-service-truck-inventory'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-manage-service-truck-inventory', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageServiceTruckInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageServiceTruckInventory'
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
    print(DashboardManageServiceTruckInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
