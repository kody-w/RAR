---
name: "rar-cowork-cookbook-dashboard-issue-sales-invoices"
description: "Produces a self-contained interactive HTML dashboard for issue sales invoices - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_sales_invoices", "rar_sha256": "200156932aa0c1e67e21806ebfdff38dd0bb7eb8fba40fb1687e034d1141e464", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_sales_invoices_agent.py` and embedded as the fenced Python below (sha256 200156932aa0c1e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_sales_invoices_agent.py` first:

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
    "version": '2.0.1',
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
