---
name: "rar-cowork-cookbook-adaptive-card-manage-service-truck-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_service_truck_inventory", "rar_sha256": "d02066e8a31ba6ff28507b3132d876259972f1376761944d4871f9370409e56e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_service_truck_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-service-truck-inventory:56a75d52519fad688cff584a25d335f61667e0dcd3f2c006c07ad28637453d4e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_service_truck_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_service_truck_inventory_agent.py` is
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

Manage service truck inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 d02066e8a31ba6ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_service_truck_inventory_agent.py` first:

```bash
python3 adaptive_card_manage_service_truck_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_service_truck_inventory_agent.py   # or on stdin
python3 adaptive_card_manage_service_truck_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service truck inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_service_truck_inventory',
    "version": '2.0.0',
    "display_name": 'Manage service truck inventory Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-service-truck-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d8fac37f749fe6a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/manage-service-truck-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-manage-service-truck-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageServiceTruckInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageServiceTruckInventory'
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
    print(AdaptiveCardManageServiceTruckInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
