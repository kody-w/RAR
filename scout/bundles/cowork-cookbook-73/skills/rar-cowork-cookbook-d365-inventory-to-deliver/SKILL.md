---
name: "rar-cowork-cookbook-d365-inventory-to-deliver"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Inventory to deliver end-to-end process - covers 7 L2 areas and 41 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver", "rar_sha256": "ab66b4e2b179484bb8c9e5430eb4ee6eb021b9139db91353d3900c7324196a0b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_inventory_to_deliver`. The original RAPP
agent is preserved byte-for-byte in `d365_inventory_to_deliver_agent.py` and in the RCI capsule.

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

D365 Inventory to deliver Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Inventory to deliver end-to-end process - covers 7 L2 areas and 41 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_inventory_to_deliver_agent.py` and embedded as the fenced Python below (sha256 ab66b4e2b179484b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_inventory_to_deliver_agent.py` first:

```bash
python3 d365_inventory_to_deliver_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_inventory_to_deliver_agent.py   # or on stdin
python3 d365_inventory_to_deliver_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Inventory to deliver Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Inventory to deliver end-to-end process - covers 7 L2 areas and 41 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-inventory-to-deliver
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_inventory_to_deliver',
    "version": '2.0.0',
    "display_name": 'D365 Inventory to deliver Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Inventory to deliver end-to-end process - covers 7 L2 areas and 41 L3 processes from the Microsoft Business Process Catalog.',
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
        "upstream_slug": 'd365-inventory-to-deliver',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-inventory-to-deliver',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '679a3de83ae65cc9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'inventory-to-deliver/d365-inventory-to-deliver', 'uses_skills': {'custom': ['d365-inventory-to-deliver'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365InventoryToDeliver(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365InventoryToDeliver'
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
    print(D365InventoryToDeliver().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
