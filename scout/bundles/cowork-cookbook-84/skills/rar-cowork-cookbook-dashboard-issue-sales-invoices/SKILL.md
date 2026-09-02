---
name: "rar-cowork-cookbook-dashboard-issue-sales-invoices"
description: "Produces a self-contained interactive HTML dashboard for issue sales invoices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_sales_invoices", "rar_sha256": "5c8570fa6680bcdc3c8a08cc80c7e4531a17211bbe6ddd1dc89e20577de1b385", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_issue_sales_invoices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-issue-sales-invoices:8af61ea9d3e98c17ef203e43c5de8668c84b241d6b4aa29d7559a6498159b2f7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_issue_sales_invoices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_issue_sales_invoices_agent.py` is
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

Issue sales invoices Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for issue sales invoices - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-sales-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_sales_invoices_agent.py` and embedded as the fenced Python below (sha256 5c8570fa6680bcdc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_sales_invoices_agent.py` first:

```bash
python3 dashboard_issue_sales_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_issue_sales_invoices_agent.py   # or on stdin
python3 dashboard_issue_sales_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue sales invoices Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for issue sales invoices - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-sales-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_issue_sales_invoices',
    "version": '2.0.0',
    "display_name": 'Issue sales invoices Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for issue sales invoices - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-issue-sales-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-issue-sales-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f8bd090ba29ae9c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/issue-sales-invoices'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-issue-sales-invoices', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardIssueSalesInvoices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIssueSalesInvoices'
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
    print(DashboardIssueSalesInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
