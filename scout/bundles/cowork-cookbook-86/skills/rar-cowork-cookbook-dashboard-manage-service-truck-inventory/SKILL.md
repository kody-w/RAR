---
name: "rar-cowork-cookbook-dashboard-manage-service-truck-inventory"
description: "Produces a self-contained interactive HTML dashboard for manage service truck inventory - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_service_truck_inventory", "rar_sha256": "87a1fc6dc850ac840fa891b988f370569167fb3dd101c1ecac0a33b839823003", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_service_truck_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-service-truck-inventory:5016bbdabc74279c6946d43577a5030645c5461ddb0257305ee03ae012824aa6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_service_truck_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_service_truck_inventory_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 87a1fc6dc850ac84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_service_truck_inventory_agent.py` first:

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
    "version": '2.0.0',
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
