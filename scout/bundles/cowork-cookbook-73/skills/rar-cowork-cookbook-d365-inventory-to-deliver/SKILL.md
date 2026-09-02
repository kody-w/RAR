---
name: "rar-cowork-cookbook-d365-inventory-to-deliver"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Inventory to deliver end-to-end process - covers 7 L2 areas and 41 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_inventory_to_deliver", "rar_sha256": "ab66b4e2b179484bb8c9e5430eb4ee6eb021b9139db91353d3900c7324196a0b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_inventory_to_deliver_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-inventory-to-deliver:bb128aa88f89eb9a231f7269da861cd48757108e41e3b19bcbf89a8413817510", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_inventory_to_deliver`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_inventory_to_deliver_agent.py` is
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
