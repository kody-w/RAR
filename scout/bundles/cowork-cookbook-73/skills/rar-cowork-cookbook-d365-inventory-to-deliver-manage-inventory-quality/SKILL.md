---
name: "rar-cowork-cookbook-d365-inventory-to-deliver-manage-inventory-quality"
description: "A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality", "rar_sha256": "2f7282738c39b285078bb21f0a908f2fb9d378767024a561873d22978e2a88cd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_inventory_to_deliver_manage_inventory_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-inventory-to-deliver-manage-inventory-quality:2ddd134f7fba9ec58f86eae7706d65724152f8a75f50202a6da5682b271c3092", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_inventory_to_deliver_manage_inventory_quality_agent.py` is
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

D365 Manage inventory quality Expert — A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_inventory_to_deliver_manage_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 2f7282738c39b285…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_inventory_to_deliver_manage_inventory_quality_agent.py` first:

```bash
python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py   # or on stdin
python3 d365_inventory_to_deliver_manage_inventory_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage inventory quality Expert — A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality',
    "version": '2.0.0',
    "display_name": 'D365 Manage inventory quality Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-inventory-to-deliver-manage-inventory-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-inventory-to-deliver-manage-inventory-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc77cdea1b313a26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'inventory-to-deliver/d365-inventory-to-deliver-manage-inventory-quality', 'uses_skills': {'custom': ['d365-inventory-to-deliver-manage-inventory-quality'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365InventoryToDeliverManageInventoryQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365InventoryToDeliverManageInventoryQuality'
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
    print(D365InventoryToDeliverManageInventoryQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
