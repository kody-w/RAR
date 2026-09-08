---
name: "rar-cowork-cookbook-ppt-exec-process-customer-payments"
description: "Builds a read-only executive PowerPoint deck on customer payment processing from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_customer_payments", "rar_sha256": "8517b82465e70cdaff7daf044eda09e23de5d0a83e2f988634da708fce83021d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_process_customer_payments`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_process_customer_payments_agent.py` and in the RCI capsule.

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

Process customer payments Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on customer payment processing from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-customer-payments
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-process-customer-payments-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_customer_payments_agent.py` and embedded as the fenced Python below (sha256 8517b82465e70cda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_customer_payments_agent.py` first:

```bash
python3 ppt_exec_process_customer_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_process_customer_payments_agent.py   # or on stdin
python3 ppt_exec_process_customer_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer payments Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on customer payment processing from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-customer-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_process_customer_payments',
    "version": '3.0.3',
    "display_name": 'Process customer payments Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on customer payment processing from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-process-customer-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-process-customer-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '305f33b44e40ab86',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-payments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-process-customer-payments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period used for the trend chart comparison.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-process-customer-payments-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for process customer payments reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on process customer payments for a 15-minute monthly review. Produce 'ppt-exec-process-customer-payments-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads process customer payments data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on customer payment processing from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint deck on process customer payments for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-process-customer-payments-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period used for the trend chart comparison.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready deck on process customer payments status for a short monthly review, sourced from Dynamics 365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecProcessCustomerPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecProcessCustomerPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period used for the trend chart comparison.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-process-customer-payments-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecProcessCustomerPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
