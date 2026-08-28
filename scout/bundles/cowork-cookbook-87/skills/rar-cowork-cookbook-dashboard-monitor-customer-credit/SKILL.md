---
name: "rar-cowork-cookbook-dashboard-monitor-customer-credit"
description: "Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_customer_credit", "rar_sha256": "eb1a73a7ea4a970734099ff72f630f3c1be33c323121c88d5c1d9213a452cd23", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_customer_credit`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_customer_credit_agent.py` and in the RCI capsule.

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

Monitor customer credit Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_customer_credit_agent.py` and embedded as the fenced Python below (sha256 eb1a73a7ea4a9707…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_customer_credit_agent.py` first:

```bash
python3 dashboard_monitor_customer_credit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_customer_credit_agent.py   # or on stdin
python3 dashboard_monitor_customer_credit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor customer credit Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_customer_credit',
    "version": '2.0.0',
    "display_name": 'Monitor customer credit Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-monitor-customer-credit',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-customer-credit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a9f3cd4efdab12f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/monitor-customer-credit'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-monitor-customer-credit', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardMonitorCustomerCredit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorCustomerCredit'
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
    print(DashboardMonitorCustomerCredit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
