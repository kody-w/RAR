---
name: "rar-cowork-cookbook-dashboard-contract-suppliers-for-goods"
description: "Produces a self-contained interactive HTML dashboard for contract suppliers for goods - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_contract_suppliers_for_goods", "rar_sha256": "2630268cb5ef019db68e764b913b2b46889f9d7bbcae51658737c2eaa35f9252", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_contract_suppliers_for_goods_agent.py` and embedded as the fenced Python below (sha256 2630268cb5ef019d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_contract_suppliers_for_goods_agent.py` first:

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
    "version": '2.0.0',
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
