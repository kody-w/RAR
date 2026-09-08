---
name: "rar-cowork-cookbook-ppt-exec-predict-customer-payments"
description: "Builds a read-only executive PowerPoint deck on customer payment predictions from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_predict_customer_payments", "rar_sha256": "f02e1d6dd02f609b102d59a67f62c47ffb15e33ecbe57a6445d89e475f967629", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
