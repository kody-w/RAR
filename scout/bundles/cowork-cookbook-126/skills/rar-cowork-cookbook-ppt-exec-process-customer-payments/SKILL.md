---
name: "rar-cowork-cookbook-ppt-exec-process-customer-payments"
description: "Builds a read-only executive PowerPoint deck on customer payment processing from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_customer_payments", "rar_sha256": "8517b82465e70cdaff7daf044eda09e23de5d0a83e2f988634da708fce83021d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
