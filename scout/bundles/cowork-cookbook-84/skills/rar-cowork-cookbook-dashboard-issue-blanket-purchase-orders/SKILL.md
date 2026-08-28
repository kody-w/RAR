---
name: "rar-cowork-cookbook-dashboard-issue-blanket-purchase-orders"
description: "Produces a self-contained interactive HTML dashboard for issue blanket purchase orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_blanket_purchase_orders", "rar_sha256": "6fee3f76309f66b62d63c8cf176079cbb75700c07d402fad7bfd8a3c13be7936", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_blanket_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 6fee3f76309f66b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_blanket_purchase_orders_agent.py` first:

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
    "version": '2.0.0',
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
