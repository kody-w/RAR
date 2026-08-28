---
name: "rar-cowork-cookbook-dashboard-enter-sales-orders"
description: "Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_enter_sales_orders", "rar_sha256": "5314af7c06102cac4bb51e6b687364c5fff89cec07b4ceeb438cdfc4fc872f02", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_enter_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `dashboard_enter_sales_orders_agent.py` and in the RCI capsule.

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

Enter sales orders Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-enter-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_enter_sales_orders_agent.py` and embedded as the fenced Python below (sha256 5314af7c06102cac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_enter_sales_orders_agent.py` first:

```bash
python3 dashboard_enter_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_enter_sales_orders_agent.py   # or on stdin
python3 dashboard_enter_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enter sales orders Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-enter-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_enter_sales_orders',
    "version": '2.0.0',
    "display_name": 'Enter sales orders Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-enter-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-enter-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee287bd0c2d0f527',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/enter-sales-orders'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-enter-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardEnterSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEnterSalesOrders'
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
    print(DashboardEnterSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
