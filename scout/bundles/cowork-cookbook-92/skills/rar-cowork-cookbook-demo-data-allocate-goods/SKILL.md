---
name: "rar-cowork-cookbook-demo-data-allocate-goods"
description: "Generates and creates realistic demo records for allocate goods in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_allocate_goods", "rar_sha256": "6fc3313ecc8fbf8035a0e7f3549158709251065f885ad6f86bcc78c70b6c6fbe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_allocate_goods_agent.py` and embedded as the fenced Python below (sha256 6fc3313ecc8fbf80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_allocate_goods_agent.py` first:

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
    "version": '2.0.0',
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
