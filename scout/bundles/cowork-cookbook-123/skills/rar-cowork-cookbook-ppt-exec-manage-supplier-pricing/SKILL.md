---
name: "rar-cowork-cookbook-ppt-exec-manage-supplier-pricing"
description: "Builds a read-only executive PowerPoint deck on supplier pricing status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_supplier_pricing", "rar_sha256": "99d3fcb278b493d729bbc14f472611c3d38821f363e7818ae4c51ab1a1048de2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_supplier_pricing`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_supplier_pricing_agent.py` and in the RCI capsule.

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

Manage supplier pricing Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on supplier pricing status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-supplier-pricing
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
      "description": "Prior period to compare against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-manage-supplier-pricing-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/cadence of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_supplier_pricing_agent.py` and embedded as the fenced Python below (sha256 99d3fcb278b493d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_supplier_pricing_agent.py` first:

```bash
python3 ppt_exec_manage_supplier_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_supplier_pricing_agent.py   # or on stdin
python3 ppt_exec_manage_supplier_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier pricing Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on supplier pricing status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-supplier-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_supplier_pricing',
    "version": '3.0.3',
    "display_name": 'Manage supplier pricing Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on supplier pricing status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-manage-supplier-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-supplier-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cbe3d5e4607919e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-pricing'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-manage-supplier-pricing', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-supplier-pricing-2026-05-24.pptx.', 'review_length': 'Length/cadence of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage supplier pricing reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage supplier pricing for a 15-minute monthly review. Produce 'ppt-exec-manage-supplier-pricing-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage supplier pricing data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on supplier pricing status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on supplier pricing from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-supplier-pricing-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/cadence of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready supplier pricing review deck from D365 ERP data for a monthly or periodic status meeting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageSupplierPricing(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageSupplierPricing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-supplier-pricing-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/cadence of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecManageSupplierPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
