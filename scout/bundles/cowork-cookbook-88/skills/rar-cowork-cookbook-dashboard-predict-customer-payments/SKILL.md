---
name: "rar-cowork-cookbook-dashboard-predict-customer-payments"
description: "Produces a self-contained interactive HTML dashboard for predict customer payments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_predict_customer_payments", "rar_sha256": "6fcda90ed5326f68a2e48cb5adbf091164624820629716f6cf3d1127935b021e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_predict_customer_payments_agent.py` and embedded as the fenced Python below (sha256 6fcda90ed5326f68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_predict_customer_payments_agent.py` first:

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
    "version": '2.0.0',
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
