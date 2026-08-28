---
name: "rar-cowork-cookbook-dashboard-issue-blanket-purchase-orders"
description: "Produces a self-contained interactive HTML dashboard for issue blanket purchase orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_blanket_purchase_orders", "rar_sha256": "ce359344ddf7bfb281def660501d77b3579004643886426f1d97784fe45fdf94", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_issue_blanket_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `dashboard_issue_blanket_purchase_orders_agent.py` and in the RCI capsule.

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

Issue blanket purchase orders Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for issue blanket purchase orders - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_blanket_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 ce359344ddf7bfb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_blanket_purchase_orders_agent.py` first:

```bash
python3 dashboard_issue_blanket_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_issue_blanket_purchase_orders_agent.py   # or on stdin
python3 dashboard_issue_blanket_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue blanket purchase orders Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for issue blanket purchase orders - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_issue_blanket_purchase_orders',
    "version": '2.0.1',
    "display_name": 'Issue blanket purchase orders Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for issue blanket purchase orders - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-issue-blanket-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '56741a3faaeaa2b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-blanket-purchase-orders'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-issue-blanket-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIssueBlanketPurchaseOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIssueBlanketPurchaseOrders'
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
    print(DashboardIssueBlanketPurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
