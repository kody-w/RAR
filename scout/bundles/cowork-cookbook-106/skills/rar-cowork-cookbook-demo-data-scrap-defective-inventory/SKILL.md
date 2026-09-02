---
name: "rar-cowork-cookbook-demo-data-scrap-defective-inventory"
description: "Generates and creates realistic demo records for scrap defective inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_defective_inventory", "rar_sha256": "07142e634446113d2f2c43246d5cf6c67faaf367f819000ed2a8cb3fe536c1cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_scrap_defective_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-scrap-defective-inventory:c176d13e818437853b89cb02abfd706c51ccaf1747de0dbf797a7ed753cbd686", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_scrap_defective_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_scrap_defective_inventory_agent.py` is
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

Scrap defective inventory Demo Data Generator — Generates and creates realistic demo records for scrap defective inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_scrap_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 07142e634446113d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_scrap_defective_inventory_agent.py` first:

```bash
python3 demo_data_scrap_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_scrap_defective_inventory_agent.py   # or on stdin
python3 demo_data_scrap_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective inventory Demo Data Generator — Generates and creates realistic demo records for scrap defective inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_scrap_defective_inventory',
    "version": '2.0.0',
    "display_name": 'Scrap defective inventory Demo Data Generator',
    "description": 'Generates and creates realistic demo records for scrap defective inventory in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-scrap-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e58608219c02380e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/scrap-defective-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-scrap-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataScrapDefectiveInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataScrapDefectiveInventory'
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
    print(DemoDataScrapDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
