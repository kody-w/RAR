---
name: "rar-cowork-cookbook-demo-data-cancel-sales-orders"
description: "Generates and creates realistic demo records for cancel sales orders in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_cancel_sales_orders", "rar_sha256": "00558cc01d2d7976b8c46b8a17f4038587a5ab9704efc6d18dea3e8b08616d47", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_cancel_sales_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-cancel-sales-orders:af866ea28585638a6ecdf9d50427b0ca53b5f0e1bb8af875f709ec209ec16e17", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_cancel_sales_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_cancel_sales_orders_agent.py` is
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
