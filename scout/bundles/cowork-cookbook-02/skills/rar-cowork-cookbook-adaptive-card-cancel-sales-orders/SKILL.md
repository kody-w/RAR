---
name: "rar-cowork-cookbook-adaptive-card-cancel-sales-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cancel_sales_orders", "rar_sha256": "3a1b4c23c8dd54e4ea00fa5c4f22a6b260965b0180c2c9e9516a348a70eb8542", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_cancel_sales_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-cancel-sales-orders:8f13cc4421f836905ab41b3ffff8a637060b1ab3e3ef78272554d89da6f44836", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_cancel_sales_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_cancel_sales_orders_agent.py` is
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
