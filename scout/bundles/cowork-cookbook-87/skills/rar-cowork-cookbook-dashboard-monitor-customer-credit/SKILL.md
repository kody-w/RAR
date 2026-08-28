---
name: "rar-cowork-cookbook-dashboard-monitor-customer-credit"
description: "Produces a self-contained interactive HTML dashboard for monitor customer credit - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_customer_credit", "rar_sha256": "20c4c8f8f99dcc9fb95ecdc7d540e6073b57b750163e9a77fc53f78993c181e8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_customer_credit_agent.py` and embedded as the fenced Python below (sha256 20c4c8f8f99dcc9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_customer_credit_agent.py` first:

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
    "version": '2.0.1',
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
