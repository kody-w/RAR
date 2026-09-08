---
name: "rar-cowork-cookbook-ppt-exec-process-supplier-invoices"
description: "Builds a read-only executive PowerPoint deck on supplier invoice processing from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_supplier_invoices", "rar_sha256": "b078efeebb101c6e2779904ba5a48b0246c04af8ac1236c3e11d1fe2f27fea1d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_process_supplier_invoices`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_process_supplier_invoices_agent.py` and in the RCI capsule.

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

Process supplier invoices Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on supplier invoice processing from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-supplier-invoices
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-process-supplier-invoices-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length/scope the deck is sized for, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_supplier_invoices_agent.py` and embedded as the fenced Python below (sha256 b078efeebb101c6e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_supplier_invoices_agent.py` first:

```bash
python3 ppt_exec_process_supplier_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_process_supplier_invoices_agent.py   # or on stdin
python3 ppt_exec_process_supplier_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier invoices Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on supplier invoice processing from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-supplier-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_process_supplier_invoices',
    "version": '3.0.3',
    "display_name": 'Process supplier invoices Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on supplier invoice processing from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-process-supplier-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-process-supplier-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '04542a87f742b767',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-process-supplier-invoices', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-process-supplier-invoices-2026-05-24.pptx.', 'review_length': 'Meeting length/scope the deck is sized for, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for process supplier invoices reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on process supplier invoices for a 15-minute monthly review. Produce 'ppt-exec-process-supplier-invoices-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads process supplier invoices data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on supplier invoice processing from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on process supplier invoices for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-process-supplier-invoices-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length/scope the deck is sized for, e.g. a 15-minute monthly review.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing process supplier invoices status from D365 F&SCM for a monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecProcessSupplierInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecProcessSupplierInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-process-supplier-invoices-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length/scope the deck is sized for, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecProcessSupplierInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
