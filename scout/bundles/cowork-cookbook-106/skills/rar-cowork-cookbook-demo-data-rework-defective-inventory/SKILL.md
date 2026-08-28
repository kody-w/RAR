---
name: "rar-cowork-cookbook-demo-data-rework-defective-inventory"
description: "Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_rework_defective_inventory", "rar_sha256": "a91de47e91bb2b83c49656218d8659a473c03273c4ff46b1545dc2bcff1a41ac", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_rework_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_rework_defective_inventory_agent.py` and in the RCI capsule.

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

Rework defective inventory Demo Data Generator — Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_rework_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 a91de47e91bb2b83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_rework_defective_inventory_agent.py` first:

```bash
python3 demo_data_rework_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_rework_defective_inventory_agent.py   # or on stdin
python3 demo_data_rework_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rework defective inventory Demo Data Generator — Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_rework_defective_inventory',
    "version": '2.0.1',
    "display_name": 'Rework defective inventory Demo Data Generator',
    "description": 'Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-rework-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '134b32f75bd85902',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/rework-defective-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-rework-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataReworkDefectiveInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReworkDefectiveInventory'
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
    print(DemoDataReworkDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
