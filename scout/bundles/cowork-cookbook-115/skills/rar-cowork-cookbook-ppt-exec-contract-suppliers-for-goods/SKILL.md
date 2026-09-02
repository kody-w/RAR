---
name: "rar-cowork-cookbook-ppt-exec-contract-suppliers-for-goods"
description: "Generates an executive-ready PowerPoint deck on contract suppliers for goods status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_contract_suppliers_for_goods", "rar_sha256": "4cf6407baed4800b1a5f82d19262e52f7d3ddeaba9a1c4acd46b0a1bc63f26c0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_contract_suppliers_for_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-contract-suppliers-for-goods:240c177d730d15823af71e07314123c342a81f72895cc99257606a90b51e6d3e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_contract_suppliers_for_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_contract_suppliers_for_goods_agent.py` is
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
