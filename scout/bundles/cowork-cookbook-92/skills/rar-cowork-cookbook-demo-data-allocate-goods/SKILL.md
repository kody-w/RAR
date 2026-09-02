---
name: "rar-cowork-cookbook-demo-data-allocate-goods"
description: "Generates and creates realistic demo records for allocate goods in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_allocate_goods", "rar_sha256": "6fc3313ecc8fbf8035a0e7f3549158709251065f885ad6f86bcc78c70b6c6fbe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_allocate_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-allocate-goods:e67f386c6f0a06c0b44b047444a5fcf8bffca5cc4879ee92efa05d0d4f5f91bb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_allocate_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_allocate_goods_agent.py` is
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
