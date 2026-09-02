---
name: "rar-cowork-cookbook-dashboard-predict-customer-payments"
description: "Produces a self-contained interactive HTML dashboard for predict customer payments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_predict_customer_payments", "rar_sha256": "6fcda90ed5326f68a2e48cb5adbf091164624820629716f6cf3d1127935b021e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_predict_customer_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-predict-customer-payments:5a5699b48b225f3408d87a9e4a11495854a20ae21ad65ff09ead68fd4846a5cc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_predict_customer_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_predict_customer_payments_agent.py` is
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
