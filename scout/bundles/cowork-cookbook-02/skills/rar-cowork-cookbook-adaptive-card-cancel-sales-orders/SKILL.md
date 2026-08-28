---
name: "rar-cowork-cookbook-adaptive-card-cancel-sales-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cancel_sales_orders", "rar_sha256": "3a1b4c23c8dd54e4ea00fa5c4f22a6b260965b0180c2c9e9516a348a70eb8542", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_cancel_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_cancel_sales_orders_agent.py` and in the RCI capsule.

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

Cancel sales orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_cancel_sales_orders_agent.py` and embedded as the fenced Python below (sha256 3a1b4c23c8dd54e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_cancel_sales_orders_agent.py` first:

```bash
python3 adaptive_card_cancel_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_cancel_sales_orders_agent.py   # or on stdin
python3 adaptive_card_cancel_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel sales orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_cancel_sales_orders',
    "version": '2.0.0',
    "display_name": 'Cancel sales orders Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-cancel-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f24273d174a6ddd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/cancel-sales-orders'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-cancel-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardCancelSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCancelSalesOrders'
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
    print(AdaptiveCardCancelSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
