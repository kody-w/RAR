---
name: "rar-cowork-cookbook-ppt-exec-manage-product-compliance"
description: "Builds a read-only executive PowerPoint deck on product compliance status from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_product_compliance", "rar_sha256": "e6d3bc3af2cef1da936f0995ab893b261fa80243df823c821dcae88752a34477", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
