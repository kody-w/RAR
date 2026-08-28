---
name: "rar-cowork-cookbook-ppt-exec-predict-customer-payments"
description: "Generates an executive-ready PowerPoint deck on predict customer payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_predict_customer_payments", "rar_sha256": "f2969904c3ed5dcea5ffb91e20b469818272f920a83209b756ea118c4519fbf6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_predict_customer_payments_agent.py` and embedded as the fenced Python below (sha256 f2969904c3ed5dce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_predict_customer_payments_agent.py` first:

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
    "version": '2.0.1',
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
