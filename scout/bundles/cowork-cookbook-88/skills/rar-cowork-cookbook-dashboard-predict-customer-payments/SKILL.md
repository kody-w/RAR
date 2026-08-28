---
name: "rar-cowork-cookbook-dashboard-predict-customer-payments"
description: "Produces a self-contained interactive HTML dashboard for predict customer payments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_predict_customer_payments", "rar_sha256": "0543c03b25b25299675827a51ca01793e62678c748027fcef531f02436dfc0b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_predict_customer_payments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_predict_customer_payments_agent.py` and in the RCI capsule.

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

Predict customer payments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for predict customer payments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-predict-customer-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_predict_customer_payments_agent.py` and embedded as the fenced Python below (sha256 0543c03b25b25299…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_predict_customer_payments_agent.py` first:

```bash
python3 dashboard_predict_customer_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_predict_customer_payments_agent.py   # or on stdin
python3 dashboard_predict_customer_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Predict customer payments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for predict customer payments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-predict-customer-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_predict_customer_payments',
    "version": '2.0.1',
    "display_name": 'Predict customer payments Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for predict customer payments - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-predict-customer-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-predict-customer-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '007c97015c66532a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/predict-customer-payments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-predict-customer-payments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardPredictCustomerPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPredictCustomerPayments'
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
    print(DashboardPredictCustomerPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
