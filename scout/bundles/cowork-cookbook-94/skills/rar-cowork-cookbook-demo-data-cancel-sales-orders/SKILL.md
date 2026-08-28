---
name: "rar-cowork-cookbook-demo-data-cancel-sales-orders"
description: "Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_cancel_sales_orders", "rar_sha256": "00558cc01d2d7976b8c46b8a17f4038587a5ab9704efc6d18dea3e8b08616d47", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_cancel_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `demo_data_cancel_sales_orders_agent.py` and in the RCI capsule.

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

Cancel sales orders Demo Data Generator — Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_cancel_sales_orders_agent.py` and embedded as the fenced Python below (sha256 00558cc01d2d7976…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_cancel_sales_orders_agent.py` first:

```bash
python3 demo_data_cancel_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_cancel_sales_orders_agent.py   # or on stdin
python3 demo_data_cancel_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel sales orders Demo Data Generator — Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_cancel_sales_orders',
    "version": '2.0.0',
    "display_name": 'Cancel sales orders Demo Data Generator',
    "description": 'Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-cancel-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-cancel-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '026333940c4518b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/cancel-sales-orders'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-cancel-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataCancelSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCancelSalesOrders'
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
    print(DemoDataCancelSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
