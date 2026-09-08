---
name: "rar-cowork-cookbook-ppt-exec-process-supplier-invoices"
description: "Builds a read-only executive PowerPoint deck on supplier invoice processing from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_supplier_invoices", "rar_sha256": "b078efeebb101c6e2779904ba5a48b0246c04af8ac1236c3e11d1fe2f27fea1d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
