---
name: "rar-cowork-cookbook-d365-inventory-to-deliver"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Inventory to deliver end-to-end process - covers 7 L2 areas and 41 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver", "rar_sha256": "b42227a268dab7dec0408ade50664448211ec33cfde2be32024f432733bd77f7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_inventory_to_deliver_agent.py` and embedded as the fenced Python below (sha256 b42227a268dab7de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_inventory_to_deliver_agent.py` first:

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
    "version": '2.0.1',
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
