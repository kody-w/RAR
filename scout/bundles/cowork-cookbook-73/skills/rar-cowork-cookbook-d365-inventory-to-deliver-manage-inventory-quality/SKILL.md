---
name: "rar-cowork-cookbook-d365-inventory-to-deliver-manage-inventory-quality"
description: "A Dynamics 365 F&SCM expert scoped to the Manage inventory quality area (a level-2 subdomain of Inventory to deliver) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality", "rar_sha256": "2f7282738c39b285078bb21f0a908f2fb9d378767024a561873d22978e2a88cd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_inventory_to_deliver_manage_inventory_quality`. The original RAPP
agent is preserved byte-for-byte in `d365_inventory_to_deliver_manage_inventory_quality_agent.py` and in the RCI capsule.

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
