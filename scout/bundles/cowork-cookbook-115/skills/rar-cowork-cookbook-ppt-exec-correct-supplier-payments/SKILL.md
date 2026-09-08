---
name: "rar-cowork-cookbook-ppt-exec-correct-supplier-payments"
description: "Builds a read-only executive PowerPoint deck on correct supplier payments from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_supplier_payments", "rar_sha256": "12eaee1db350f7a4b62ee7e6d232d503e9b79ca0763f1f19e81b1e145c36cf64", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
