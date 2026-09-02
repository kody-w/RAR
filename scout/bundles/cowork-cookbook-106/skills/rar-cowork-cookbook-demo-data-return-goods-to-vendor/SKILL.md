---
name: "rar-cowork-cookbook-demo-data-return-goods-to-vendor"
description: "Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_return_goods_to_vendor", "rar_sha256": "10493da0b7a7796303585c763d7fa036bda5cc29f8f938eb3d9cc06907fe5ab7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_return_goods_to_vendor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-return-goods-to-vendor:06fb08908b0912fda09db34097bff00911ccd386ea12b6ecc89d3e9e041fdc9b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_return_goods_to_vendor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_return_goods_to_vendor_agent.py` is
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

Return goods to vendor Demo Data Generator — Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_return_goods_to_vendor_agent.py` and embedded as the fenced Python below (sha256 10493da0b7a77963…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_return_goods_to_vendor_agent.py` first:

```bash
python3 demo_data_return_goods_to_vendor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_return_goods_to_vendor_agent.py   # or on stdin
python3 demo_data_return_goods_to_vendor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to vendor Demo Data Generator — Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_return_goods_to_vendor',
    "version": '2.0.0',
    "display_name": 'Return goods to vendor Demo Data Generator',
    "description": 'Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-return-goods-to-vendor',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bdd80779c8ef8c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/return-goods-to-vendor'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-return-goods-to-vendor', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataReturnGoodsToVendor(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReturnGoodsToVendor'
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
    print(DemoDataReturnGoodsToVendor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
