---
name: "rar-cowork-cookbook-demo-data-allocate-goods"
description: "Generates and creates realistic demo records for allocate goods in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_allocate_goods", "rar_sha256": "9fb6409d56c5f7f7ecb3fa046e0f486bd2c2d23c25ad1da9abc2765989f59383", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_allocate_goods`. The original RAPP
agent is preserved byte-for-byte in `demo_data_allocate_goods_agent.py` and in the RCI capsule.

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

Allocate goods Demo Data Generator — Generates and creates realistic demo records for allocate goods in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-allocate-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_allocate_goods_agent.py` and embedded as the fenced Python below (sha256 9fb6409d56c5f7f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_allocate_goods_agent.py` first:

```bash
python3 demo_data_allocate_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_allocate_goods_agent.py   # or on stdin
python3 demo_data_allocate_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate goods Demo Data Generator — Generates and creates realistic demo records for allocate goods in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-allocate-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_allocate_goods',
    "version": '2.0.1',
    "display_name": 'Allocate goods Demo Data Generator',
    "description": 'Generates and creates realistic demo records for allocate goods in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-allocate-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-allocate-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f7fd3b78567e5cfe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/allocate-goods'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-allocate-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAllocateGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAllocateGoods'
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
    print(DemoDataAllocateGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
