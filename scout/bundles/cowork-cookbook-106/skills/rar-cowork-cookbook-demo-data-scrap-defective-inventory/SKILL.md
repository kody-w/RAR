---
name: "rar-cowork-cookbook-demo-data-scrap-defective-inventory"
description: "Generates and creates realistic demo records for scrap defective inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_defective_inventory", "rar_sha256": "07142e634446113d2f2c43246d5cf6c67faaf367f819000ed2a8cb3fe536c1cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_scrap_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_scrap_defective_inventory_agent.py` and in the RCI capsule.

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
