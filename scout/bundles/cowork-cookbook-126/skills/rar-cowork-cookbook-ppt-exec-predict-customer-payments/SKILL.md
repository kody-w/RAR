---
name: "rar-cowork-cookbook-ppt-exec-predict-customer-payments"
description: "Generates an executive-ready PowerPoint deck on predict customer payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_predict_customer_payments", "rar_sha256": "bdc31c71c410aaa1bd118c6f571be2ebb9fa3cac1c479326b005978c7cb66c93", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_predict_customer_payments`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_predict_customer_payments_agent.py` and in the RCI capsule.

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

Predict customer payments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on predict customer payments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-predict-customer-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_predict_customer_payments_agent.py` and embedded as the fenced Python below (sha256 bdc31c71c410aaa1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_predict_customer_payments_agent.py` first:

```bash
python3 ppt_exec_predict_customer_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_predict_customer_payments_agent.py   # or on stdin
python3 ppt_exec_predict_customer_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Predict customer payments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on predict customer payments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-predict-customer-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_predict_customer_payments',
    "version": '2.0.0',
    "display_name": 'Predict customer payments Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on predict customer payments status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-predict-customer-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-predict-customer-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '92902b7f1b25a3ef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/predict-customer-payments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-predict-customer-payments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecPredictCustomerPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPredictCustomerPayments'
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
    print(PptExecPredictCustomerPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
