---
name: "rar-cowork-cookbook-ppt-exec-contract-suppliers-for-goods"
description: "Generates an executive-ready PowerPoint deck on contract suppliers for goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_contract_suppliers_for_goods", "rar_sha256": "4cf6407baed4800b1a5f82d19262e52f7d3ddeaba9a1c4acd46b0a1bc63f26c0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_contract_suppliers_for_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_contract_suppliers_for_goods_agent.py` and in the RCI capsule.

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

Contract suppliers for goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on contract suppliers for goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-contract-suppliers-for-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_contract_suppliers_for_goods_agent.py` and embedded as the fenced Python below (sha256 4cf6407baed4800b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_contract_suppliers_for_goods_agent.py` first:

```bash
python3 ppt_exec_contract_suppliers_for_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_contract_suppliers_for_goods_agent.py   # or on stdin
python3 ppt_exec_contract_suppliers_for_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for goods Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on contract suppliers for goods status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-contract-suppliers-for-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_contract_suppliers_for_goods',
    "version": '2.0.0',
    "display_name": 'Contract suppliers for goods Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on contract suppliers for goods status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-contract-suppliers-for-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-contract-suppliers-for-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39bde8544b351623',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-contract-suppliers-for-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecContractSuppliersForGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecContractSuppliersForGoods'
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
    print(PptExecContractSuppliersForGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
