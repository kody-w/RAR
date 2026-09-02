---
name: "rar-cowork-cookbook-dashboard-issue-blanket-purchase-orders"
description: "Produces a self-contained interactive HTML dashboard for issue blanket purchase orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_blanket_purchase_orders", "rar_sha256": "6fee3f76309f66b62d63c8cf176079cbb75700c07d402fad7bfd8a3c13be7936", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_issue_blanket_purchase_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-issue-blanket-purchase-orders:1efd90ef052de29afde04c15e247b2f7147b21b572015fe6879bb103a2f2d742", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_issue_blanket_purchase_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_issue_blanket_purchase_orders_agent.py` is
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
