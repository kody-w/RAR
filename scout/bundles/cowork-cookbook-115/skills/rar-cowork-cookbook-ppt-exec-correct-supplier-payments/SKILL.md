---
name: "rar-cowork-cookbook-ppt-exec-correct-supplier-payments"
description: "Builds a read-only executive PowerPoint deck on correct supplier payments from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_supplier_payments", "rar_sha256": "12eaee1db350f7a4b62ee7e6d232d503e9b79ca0763f1f19e81b1e145c36cf64", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_correct_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_correct_supplier_payments_agent.py` and in the RCI capsule.

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

Correct supplier payments Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on correct supplier payments from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-correct-supplier-payments-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart (monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_correct_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 12eaee1db350f7a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_correct_supplier_payments_agent.py` first:

```bash
python3 ppt_exec_correct_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_correct_supplier_payments_agent.py   # or on stdin
python3 ppt_exec_correct_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct supplier payments Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on correct supplier payments from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_correct_supplier_payments',
    "version": '3.0.3',
    "display_name": 'Correct supplier payments Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on correct supplier payments from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-correct-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c7e188dd374152bc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/correct-supplier-payments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-correct-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'meeting_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-correct-supplier-payments-2026-05-24.pptx.', 'review_period': 'Reporting period and comparison prior period for the trend chart (monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for correct supplier payments reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on correct supplier payments for a 15-minute monthly review. Produce 'ppt-exec-correct-supplier-payments-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads correct supplier payments data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on correct supplier payments from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on correct supplier payments for USMF from D365, with speaker notes.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-correct-supplier-payments-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart (monthly review).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready supplier payments deck for a short monthly review, sourced from D365 F&SCM without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecCorrectSupplierPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCorrectSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-correct-supplier-payments-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart (monthly review).', 'type': 'string'}},
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
    print(PptExecCorrectSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
