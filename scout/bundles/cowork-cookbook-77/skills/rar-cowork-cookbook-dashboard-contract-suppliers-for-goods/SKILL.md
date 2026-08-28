---
name: "rar-cowork-cookbook-dashboard-contract-suppliers-for-goods"
description: "Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_contract_suppliers_for_goods", "rar_sha256": "cda80eb5ff5f1fe6b4ecd5475ded23df3c48cd74517c0847bb39aa13b4cc50cf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_contract_suppliers_for_goods`. The original RAPP
agent is preserved byte-for-byte in `dashboard_contract_suppliers_for_goods_agent.py` and in the RCI capsule.

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

Contract suppliers for goods Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_contract_suppliers_for_goods_agent.py` and embedded as the fenced Python below (sha256 cda80eb5ff5f1fe6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_contract_suppliers_for_goods_agent.py` first:

```bash
python3 dashboard_contract_suppliers_for_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_contract_suppliers_for_goods_agent.py   # or on stdin
python3 dashboard_contract_suppliers_for_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for goods Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_contract_suppliers_for_goods',
    "version": '2.0.1',
    "display_name": 'Contract suppliers for goods Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-contract-suppliers-for-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-contract-suppliers-for-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e4bbb195a700154',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-goods'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-contract-suppliers-for-goods', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardContractSuppliersForGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardContractSuppliersForGoods'
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
    print(DashboardContractSuppliersForGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
