---
name: "rar-cowork-cookbook-dashboard-enter-sales-orders"
description: "Produces a self-contained interactive HTML dashboard for enter sales orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_enter_sales_orders", "rar_sha256": "e776a97835896d3405994ee3644601b221041713bb1de46b554ce24b5e5b730d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_enter_sales_orders_agent.py` and embedded as the fenced Python below (sha256 e776a97835896d34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_enter_sales_orders_agent.py` first:

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
    "version": '2.0.1',
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
