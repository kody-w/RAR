---
name: "rar-cowork-cookbook-ppt-exec-contract-suppliers-for-goods"
description: "Generates an executive-ready PowerPoint deck on contract suppliers for goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_contract_suppliers_for_goods", "rar_sha256": "28acd711c614a83a23bbacf4cc84ebd2ee86d7d6e6a4222e568a8636f354b116", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_contract_suppliers_for_goods_agent.py` and embedded as the fenced Python below (sha256 28acd711c614a83a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_contract_suppliers_for_goods_agent.py` first:

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
    "version": '2.0.1',
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
