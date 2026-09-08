---
name: "rar-cowork-cookbook-ppt-exec-manage-supplier-pricing"
description: "Builds a read-only executive PowerPoint deck on supplier pricing status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_supplier_pricing", "rar_sha256": "99d3fcb278b493d729bbc14f472611c3d38821f363e7818ae4c51ab1a1048de2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
