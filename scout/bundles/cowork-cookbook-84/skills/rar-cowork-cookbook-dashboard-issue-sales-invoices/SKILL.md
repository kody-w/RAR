---
name: "rar-cowork-cookbook-dashboard-issue-sales-invoices"
description: "Produces a self-contained interactive HTML dashboard for issue sales invoices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_sales_invoices", "rar_sha256": "5c8570fa6680bcdc3c8a08cc80c7e4531a17211bbe6ddd1dc89e20577de1b385", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_issue_sales_invoices`. The original RAPP
agent is preserved byte-for-byte in `dashboard_issue_sales_invoices_agent.py` and in the RCI capsule.

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
