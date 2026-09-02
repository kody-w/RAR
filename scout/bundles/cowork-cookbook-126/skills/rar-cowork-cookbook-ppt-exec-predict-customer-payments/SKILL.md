---
name: "rar-cowork-cookbook-ppt-exec-predict-customer-payments"
description: "Generates an executive-ready PowerPoint deck on predict customer payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_predict_customer_payments", "rar_sha256": "bdc31c71c410aaa1bd118c6f571be2ebb9fa3cac1c479326b005978c7cb66c93", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_predict_customer_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-predict-customer-payments:60ca9a1e78d87ca53aca07ff7a34c93c7b46968db7dc1946abc6374dec1cbf91", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_predict_customer_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_predict_customer_payments_agent.py` is
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
