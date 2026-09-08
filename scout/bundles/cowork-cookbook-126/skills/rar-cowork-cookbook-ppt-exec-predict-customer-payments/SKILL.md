---
name: "rar-cowork-cookbook-ppt-exec-predict-customer-payments"
description: "Builds a read-only executive PowerPoint deck on customer payment predictions from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_predict_customer_payments", "rar_sha256": "f02e1d6dd02f609b102d59a67f62c47ffb15e33ecbe57a6445d89e475f967629", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

Predict customer payments Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on customer payment predictions from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "comparison_period": {
      "description": "Prior period used for the trend chart comparison.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "output_filename": {
      "description": "Target .pptx filename, e.g. ppt-exec-predict-customer-payments-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_predict_customer_payments_agent.py` and embedded as the fenced Python below (sha256 f02e1d6dd02f609b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_predict_customer_payments_agent.py` first:

```bash
python3 ppt_exec_predict_customer_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_predict_customer_payments_agent.py   # or on stdin
python3 ppt_exec_predict_customer_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Predict customer payments Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on customer payment predictions from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Predict customer payments Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on customer payment predictions from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93a01129db8e7cdc',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period used for the trend chart comparison.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-predict-customer-payments-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for predict customer payments reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on predict customer payments for a 15-minute monthly review. Produce 'ppt-exec-predict-customer-payments-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads predict customer payments data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on customer payment predictions from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build the executive PowerPoint on predicted customer payments for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-predict-customer-payments-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period used for the trend chart comparison.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready customer payment prediction deck for a short monthly review, sourced from Dynamics 365 F&SCM via the Cowork ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPredictCustomerPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPredictCustomerPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period used for the trend chart comparison.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-predict-customer-payments-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
