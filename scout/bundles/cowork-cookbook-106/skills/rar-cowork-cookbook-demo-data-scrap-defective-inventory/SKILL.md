---
name: "rar-cowork-cookbook-demo-data-scrap-defective-inventory"
description: "Generates and creates realistic demo records for scrap defective inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_defective_inventory", "rar_sha256": "5dec43e863a690f5b6c4c5ee0c9867d1090d7cb52babec9c4d891c1a0c7830e9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_scrap_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 5dec43e863a690f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_scrap_defective_inventory_agent.py` first:

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
    "version": '2.0.1',
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
