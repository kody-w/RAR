---
name: "rar-cowork-cookbook-ppt-exec-manage-product-compliance"
description: "Builds a read-only executive PowerPoint deck on product compliance status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_product_compliance", "rar_sha256": "e6d3bc3af2cef1da936f0995ab893b261fa80243df823c821dcae88752a34477", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_product_compliance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_product_compliance_agent.py` and in the RCI capsule.

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

Manage product compliance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on product compliance status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance
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
      "description": "Prior period to trend current compliance figures against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-manage-product-compliance-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_product_compliance_agent.py` and embedded as the fenced Python below (sha256 e6d3bc3af2cef1da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_product_compliance_agent.py` first:

```bash
python3 ppt_exec_manage_product_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_product_compliance_agent.py   # or on stdin
python3 ppt_exec_manage_product_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product compliance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on product compliance status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_product_compliance',
    "version": '3.0.3',
    "display_name": 'Manage product compliance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on product compliance status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-product-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-product-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '439bdbffdadea203',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-compliance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-manage-product-compliance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend current compliance figures against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-manage-product-compliance-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage product compliance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage product compliance for a 15-minute monthly review. Produce 'ppt-exec-manage-product-compliance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage product compliance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on product compliance status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on product compliance for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-manage-product-compliance-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend current compliance figures against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready compliance review deck for a short monthly review, sourced from D365 ERP data without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageProductCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProductCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend current compliance figures against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-manage-product-compliance-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecManageProductCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
