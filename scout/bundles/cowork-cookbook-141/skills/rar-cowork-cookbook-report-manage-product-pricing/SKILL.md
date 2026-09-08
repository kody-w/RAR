---
name: "rar-cowork-cookbook-report-manage-product-pricing"
description: "Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_product_pricing", "rar_sha256": "1517df6c56461c18b1b27a1b2f658388f4e79e6be2c8d8e8dcef8869ed8c405f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_product_pricing`. The original RAPP
agent is preserved byte-for-byte in `report_manage_product_pricing_agent.py` and in the RCI capsule.

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

Manage product pricing Summary Report — Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-product-pricing
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (default USMF).",
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
      "description": "Excel workbook filename, e.g. report-manage-product-pricing-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_product_pricing_agent.py` and embedded as the fenced Python below (sha256 1517df6c56461c18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_product_pricing_agent.py` first:

```bash
python3 report_manage_product_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_product_pricing_agent.py   # or on stdin
python3 report_manage_product_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product pricing Summary Report — Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-product-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_product_pricing',
    "version": '3.0.3',
    "display_name": 'Manage product pricing Summary Report',
    "description": 'Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-product-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-product-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa446f868c12f37c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-pricing'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-manage-product-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (default USMF).', 'output_filename': 'Excel workbook filename, e.g. report-manage-product-pricing-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage product pricing stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage product pricing for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-product-pricing-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage product pricing records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a product pricing summary report for USMF from the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook filename, e.g. report-manage-product-pricing-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-change summary of manage product pricing activity in D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageProductPricing(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProductPricing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-manage-product-pricing-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageProductPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916Z9PbVpbmX+G+U7W2h9KLnDTVVUsQAMEEEIkkaHXJyDkQGfD4v+8FScmh3Z7uqv20tCWSwL3nnvg85wj8+c1qm7Co3j69aZ6VLzZWmkahVy2s3F2si76oEvBWJDb4s3CKvKkiu22Kqn778OZ6tVNFZRMVOdjOtlHq1gtrUXmW+7HI03FRVoXbOg14j5woDxZ1m2VWNYIVZVE1C78qsgU35lYWOfUCI4mF8L+19XHxfeoFVrrw8iZqxoWhHYUfFn5RLZrQW2RF3YD9Dri5KMFnz12UXhUV7oeF66VR51XgigXUyBf84HjpYrbgoXwfNeFCe2rwYcF5jRWlHx5m6kWJwIs69Lymfgd2eYOVlalXv3368e8f3iLw+e3Tz29OatXg0pv6UP5o5VbgnZ4Gnp72ga2pBd4+vZUj8GkOvgPdgOYZuOR6/uL17fvaS/0Pi//8z6S3qqD+4dPnfPF6fX6b/1Pb/GFsU1gPCx2rtOwoBd54X6zS3hpr4IKmrfLZ3TUISR68P3f+KqkoF3+b733/POQ98JrvP78VQAVrDtjntx8WwKWf36p2/vw+Sym//+E9LXqv+v6HX+XUrR17IIZAGND6/cvr+0ssWPjr0shffNFO/Pp1FohSVHpA+G/sm19P1V/iXi758lz8fVF+WPy55NmevwF9n0lnA7l/Lhb4AOx8e4+LKP/+dUZVdF5u5Y73/Q//TKwTek6SRnXzL8n98Sk4BJkOvPVyyQ8fHuH7+2L5su2bzH9+bAkS5t+xBCz/etw3R/0z2Y/I/kF0GuVe/S2WfyruzzYs/7b48Z/a9lcbPiz8z2/cszAtO/U+LX5+pMiP37m/Xvzu778A0f+jGK1oK+ch4Utm5ZHv1c2XLz9+Vz8uf/f3H79rS5DFnpV9aav0z2T+mV8f5/zOg69V3/9+LzjfyJO86PPFtxpa/FyU/6v65X1xttLI/fV6/Wnx20qcX8vFbMTXQ58u+E011kDX3/jxh7dfAO7kwBoALvNtgB//8R+LY+RURV34zUJzihbAYAsQMvNm5fUwqhfg/xk1Kg/4tY6AY1/rQP7PEZ41LvzFT//HecD6R+cF69ATjmenAkj78gLtLy/Q/ul9oQOhRRUFUQ5QWV2dTp/nhQCAwYFl5dVe1QGQssfG+whq+eP8YRHli5/+Uu6Xh4j3cvzpgcHRE/HU9XZGu7pNvffZrkvo5S8rHADp3uA5LZCeFg5QxY8ASH8A9tZF2gG0nH1QJ1GaLtwI4AlgqfEhG/jp0yzsp59+sq06/Jw/4RlbPOmrhsCCb+osPn4ENvlpFITN59xzwmLx3c+/fLf478Vf7XoIn884AZJ4RQFouNNkaQGqqs3AMhAgEFIAGY8o/PzLy7NATA74FsQs8iPvuRlkZeK5X92siauPKEEubA+4F7g2m90682nUvC+2/uKbvi9inVkhnHnS9Uovd73cGYFUC5jzzZN50SxqkHq1D7iwrb3HqT/ZlfVQMQPlbTU/LY7rE+CgIgV/zWo+FoHNRR4B939Lgud1IKT6rl6wX0W8L6Q5DxelVVllWFmvM3zrGRfAPV+3A+HWIvf6z/lMtd7sqkdRPN0DFgHPOK+QfpxjDvoQwOK5W389+7HGmplSfzBm9TmvXwlvVXMoHEAA4NCgjdyZBv7rlVJ1WLSp+/Cf92wvXlFwX1F55OCT6v+hmXm1EotnP7D43KIwgi/+P+mCZrtXm43Kb1Y6zy14SVfNZzzmHnA+9tk2zqo9lQK192ub8hWKviLy5zyNQHJV4389Vz6i+FrzRLl21lhdqQ/5IIVAPGa5jwyfM7aq5tqwPudfoR8ovXjgHAgygANQLnOWfj1wvvtV0xDU/Pz91zbgkRGVO5sNsnhRtnYKMsz3PNe2nARoNQfva0RBuntzxfZh5IS/s2qODYgjkL8ASkSg7gA9vH+D4+fdr6r/buOz25m3PDrBFhRp9RAA9PBmBeeAzKEC6jXPlhvY+ekhBJiRlc1suw3KBFj6vAhCfm+jOmpmSHz61SsBFn+c35+Wzle9oQSVAZwF8r9sgXcfFTOnZQZ6GaADSCBQQFmUA24HTnk54SHQyubyB/D6aj6fEh+XXwZ5jzKbSenrxtmQec/M889Ut/Lxtyih/1maAHnZvOJx7h8z7dtps+wZKWuAduDEr3efDcH7k9OfTcPiq9xP/zDTfP/vjT0PljZ+nwCfFmHTlPUnCHoy61difQc4BT11rV8k+/FJhh9fmPDxhQm/E/q099Pi31PsdyJehfFpgbzD7/B86/BKrNcL+GH9kTU/4vPdz7nq/Qqh4PgiA5k1R20ErP6N774uAaQXVACbwOIn/9UzbfaAqR+AD0LwOf9tps+VBvgkD+bMrIvfIMCD+EHWPyP2jZfArbwBZ7szkAXePJI96qL23j7lbZp+eANg6f1Po9hMPNmcy/U8vQGHA4RsIu/xzQa6JS6o1i8uyNW8fvZYP/9houW+3Xvk1rdNsxktwAJQ94BhraqZKesDUL/xgmKGVbAYNCUl2PjowsAWr/owewiQkVWWwJi5HGa7mrGcDXnOcHPX9wCtoflHZeTHByt9f4F2/dtKeBHZTOS/Kdin74GyDrAdMAPQr551A76f3TIXu1UnD+P+VJcHAX15EtCfeGemqt9x1NwlPDkNwOH3YOC12rR5Mtefyv/W/v6j8AvoP2Z5bvFppuIPL9QD72BkAa7+On3MfPecBx+De96CUfvHefKZE+CxZf4A9oC3b5u+/dOF7b39/c/0ekDjlzlFn4n2R+3+wKlfF35YeO/B++IvK/0jCqPkR5j4iOLvQ1oPf+qYJ5f/47mn31L97J5nKxFNoKN5ubueL/9li7CwOpA+/yQBweEPHgFsPDvy1wj96qfiMS4+1Eyt5vmvGz+/gUqzQIJZr1p7zRtgOYDdj/XcbUEAi8CB4PsTNcC9f28SeW2uQws0w2A3QiCU65MOQeIk4iC0jdgoZYG/fJKgMZr2cY9iPNL2UId2aY92Hc+naZLxXNrBYcIH8p7A82XuJ6NZoVmbOUgAu7xfb4NL7suSp+azm74NPrPFL4MAsJA4WCni9Xb1fK0hBgEXKbtlr0uKdIOztUYvSCPXpXPRU6k+lkd+datcRbNtM+YRQbiDvKS2SWpddWliVyK6PWUbv5RoYrc579LMyUiPRDFtvbLNhD5x45VCpi2tDx0tFJlzR/j07qrCzcaRvSAj7Z5GMyLtQqk77+ys9OPrCcLLPDXIOChC1SISiUd1T3T6O7WenFiqUsu1Hbs8EIIlhn5cjyPER8zSyan+UiBRc9MGw2jLcUfhjA8h0UG4lYf6LvFNC+85Hhr4VsXtdq/ub2NumDpvpWaHOESeRH1ixrkIb88RWcMdMmakdcHh9rqhdVgtybshl0RwXete2eQcSx7MvWBcoIzrGfl6kGjGP+UYBQkKDUEAd5cMTavmIURTDb7vx33slnrR39JcCZUy35UmVW6uuJoi50vKcpwbctXNpBCxbNn9AFdSr3Db3X2PitjErFA9nUpVvp3OpcZ4qbZ2CKQMj7jc6Cd1L2iGKTRhXLgSP2xSPHLT9BIxoj2g/gZJa5JzYVrA02OQnCMNk7ZMNa6Oy+pmDVx93t4vddXz8ahiaaRrN5DsFsUjhiVmzG2prX1FRIPDcc8efKFPeSm10RIhCCxsdee0l9MjrDiXKrIiTZMNWtT6wiwwQ1kV1ng4HBl7e68dnoB7DkLJMdE1Jr3bgkAPLAndRS3UiPPRFsezlMLtrdN26FIV78UpU6qd2uzv07rYMhf4HhG7o6PVMR64G4Ms6fsgS8ModqAF3h10pcWHyFFgd3e0Ih+9w8XxoOgmHw87ee8PdZ1KxwE93GTX29248sIWFjwW1nAJGstgu41+rdr7ORK1OqGbtS3sa6LBL9btIq6r7RUvR2iduMghIbQ6L+nyaMPq0tlD3UqD5ERiedpo4dPWFuLeOpNHxT/ZTW3nZipfLvrGn4y9t5FKwi/D9obbqpnZjleV6bgLLYJgLAKFNEls3Qhn4jucs8uadU4nxV+uoJ6ooUsi99Aos8myHSnSc3H5GsVIcPd2TqLUokaG2kat81vUqpKQyW192Nxabc1dyWHCA1rEowa++pXF7ZcrRIiuKkeUma7gZzvTxl1c13Bh+TBmb4ctGpkssktKK+r3bTJIW9V0DWvdaau6OAYOi3usvN+1LKXsqj7Cjuy6O+S9U6apgd7yMEQoHjp64z7v3S46G05lWM75vo3X1nrfZ6t7uytuSHMzAv5UHI0TdjptESSp3V6IuzujJCvmombspd5DyZ4L3Mw5ppONgpakIkp3vF44dDivckMxYjQ4C5v4ZHKaG7X7fq9u19F2exGWezVnO6q4oFR62FpKfcZz5ZZslLXn7rF7xtPbQbgkZtW1TBgjNlzyZ2u1ZtmoOoVBdzDMeCAn3YdvuOWgd9kng4S1rQDZVhh3hfxzkHntanPsqeS+Ki90ScKNlZy2wma1XKv8kTzkmODmvb1ODqJaiXQ7KVe8neTEJvASlkx+k+DnUypPgZ6vW7FxVmeO3O4xmR7k0XUm9WAHoS2GvL2afGcbsJfMgMKzt8o1+GCFraZQ5S24ENfyvGxsBhVPbCcKotnziNxyBEoNWgLB1HGilEQVjHG8iOFSdnzMOJaom6SOA9OsubUTYqSDbN8Kld4JzdBe/QxTOm8NSZSlu0FIbyjZjPXA2W0HT8AmrI2Ks0fqvaO2E3vDTlclVuz2HgkrZgvv7muCC1LUybdhjvVJvU1sQW3NTbMxkuS66o+xNib2Zkdfcp7triRy7nxiA6PYmdfut606Vutec9okI13FTrd9bhCRcXcwlu6sYr9XiCTZSLnpJmcHtU12a1JdayLhwNfXfbVamecmZnZ3QzkfS5fSrSU7DX1RbKKwR4SKEsjmoghCv8Yb54KhRn5YbeyDLGDyXrzcID8/j77cTQRN+cftMtAuvlqei/S047K7bq/6gmHDeGfUlOOdIGoVhxhMrTmpuCuKkRNLz/WrjuoJFVqHOHPJIXjZiLd0hyXItjsdufFs8/zqWEfnjp2c7ib0RZ/umUub9VGxYWn4FMTWJkNjnHM443odZX8om+Z82R15lcu56/bWCbpes/ek7Llyb27g/krvWWPjKaXArUN4A1luKlfXokODY9FzuoyW2emsbXbePnQYNXJrdRDIQanv1Uo147BjM446NmNKCJXk7AzK824HzqPvI5678GqjsRowbVPiRIw6MXwsbiEsL/VgW5jKsNtj4150KInc0fKO1NjmCDIlJHpO3fblEc7WZnfGImmQhnWfSv4JVjD4HK+0kjP7bagyxxWXhhfWhGTCKuG0K6tD0Cr2Dhh6uAlXMj1rkbYbeY5fE/CV0DXeU3MIugvrlXFIh0BHsqJhxr4MwoMybRXljkgDr/gjhNahNuxLuDiAwMo1QIk+9H0Rl/SdQRsVXyfVOrYMEYdxNeO27hYzmAPZbEv0kIECuckrmr3iK90YY6vvbveEto4axu4Om1V5vAzqroI7d+fu01KxDkGKX1wEnQj9EoLKybhK5Q9pb9LSeADMUApEtSnvrVbjZ9FablSnHO3A4lZmLHsWWU78cMHokA8lYqS67CjGaLrrjwIObw1vhcWxdL1afhKxtrmcMNk4GNNuv9lC5pngdFK9bINQMbT9WSRSMh0PjLrp1ayOgqFrB2a73Cw5gHo6w4gHAuYnceU7lyw+bfD6wHWKMfFdU7K+fzrf1KopU2cScjYIWzdDKQLfZ30Q8Zx8tm9Y2glIzRYum2RuIOx6v7Np4ridegoTzDG+HS/EPTiZVrSXOCrSlTsPW6jde7siC/J1opQbk2fkLDZTBcVHj4nWgdSDAuN1XWC0ziROMOvAooAIXKadAucsJQGn+ulB4lbEOYmNI0SNAX3jK9KijxMY7MzTCr2x03ov9qrMSKFY7SyXx6HMPqK8skIAS+NIAXFOxtyPDqv5QieRjn3NjVQnNAB/2pnuFEjgh7Czg+O1cQ2SsHsR1pmOwUo0NW0nV+xb5GbGEDMF5fmlXMDDCPvb26mV1T3oQWQ6EeQhOm86V1PuBOrnk7xeJiPhFJoR7rX8qm7Z9W1nJTofTOebeOfXVymi9tcNIQlCvg7XdHxh03EVDf7lcOBgqLhSZO2pXWqx12aNmQGsyGZK6716CAeZXVkxVSe9cT5dWUQy9DQqnNg8eay9CyY3cvrSosK2jS/XGkXvk3W6kcmeON/5o7KSm0u6Tseer7eWtfZKVVunxU3BnUBgbDZxnIymkZ2za9rtwNTxEu3OU8HCF7TmCt5b7fHUGVLdUNt7HRdrWM1DAE3lucZqhHdKf7k8XAKOYBiZU1PmKF7h3vc9Aoq29anbauVU5OPFBkjD3I4yzEGil9U3Cw0Gyrssjf0yHDWp2UB3YqshdlSi5rRsshKTCpLEMbrF8RJdhjLGnsvLcSuN0hSw7h5OmTPaa7RZUd5yibTxgTHOB6SpaCYo174q6Uyv39a2NxzonDV4lqPXabJZp8dEc0EnkbmCmsAaFYdBk90Uc5MRZsT3WZd08l05dI6+rszNFbNVdUlx9Al0DlTPaYOKa4YsMReC66MzKB7HpFvPyiouLnYwUgswC+aoncKofIox2QpN62y8HSp5A7Bus+P38E5CEbW3eMA20X4ba8ulB+kB7i3DGnF3G8FRQz/QSmWPozBSEZtqlYLSHFtaXWfZLRhD+qSsixXWWxlmXYWjjFma6Z3ua6e/BlwSMHIoIuGKOYdLdMINC4e6zZLSb2OWSqqWSl4l2r4GstRpr1tp8mxYt0xNQM+SbeJ9mE6D1J71GGAXQonRLViWNuFe5OvNSgT9NtR0oaAFIYwXiaL7kz+0zBHJBmGVKsVKR+l7j0Xphi1bjDmI57Eg7TVDhhG3LQGSZ0aUqgl+p4e1qloUzveAgrg2p4JdrNt3rJHv1/sK43Z71Gr7I8fFmYha+Eq0Fcc46i0HT5VWblt+4hBJqk4yPMbr+CiVymVZOghUoJfcNqO82NprmGijlRQWqQyT/b1M6SPJuEnES7oi+Q0u891dRY7FesQuVr/u4zBFTqdjX7vupd/b1AmlJXSLl3d2GbA9w53uWaM0Z+FuW5QTYzguMxG0bprtpsJXVClOiCINFkYanF/HDEq0mwu1Ngn/0kHiLgtx0sFkCg7d1Wp7r+IrQsadbjkrjfVLSMncM7btrsJ2s7ai61r1TU0vEBXRkJ1Kniyp9/HyVN9YZtCvEWpaQcdWiQkHSRjku3E1dMaK2A+TdyROtxqLJ9M0huDo4yJ+TfUDNQj71RAtEUspWVCMnWojKT7dQf9TOKhocbK1nW4Tl6uZkIMKjn3TXUvNheb6UwKjuonsMXY5qo0U+FdMsXQd9xXIRg9DxUSZ1Zl55NyXYnA5QVHbXF1n5ZmSm+6W2BUMaDtCEyvVr/JiynpXwcxMagiEwDaMJjjrqLEGHUK9LAhhMP+OaoXtcCXeX5Gzl6VyVyDX3O/P1XXl8w0/mQffE0hFEE/YJURrSSoxm+GdnT2NO8QghS60GQ0Bo2qBgZF5HHXISOR7dNliumHtd8feBupza/3MpJItiHAtpnpwwlKHkjfRodlBaToGI81KMQrd6iXwCwHS7Gq5LSdOt4DhBdM6DTl+QJUpa3jhfjqsXBKDGHqA8MNk3qc6pCcHgiKIlsSDFw6QFR5IJuki3PJ4QnHIBEe3NC0PNyGtnXKXw8PQQzSnnJekeCaR0d6fSPFgryUOO/o9b0Ty6BuMvRz1U3VSW+4sVfR0XJqb/XQ1KhqzFc8N9mCSbWEpZC4Obk/iptg59nFDmyGFM7v9nZBsqtCTwcFu69VKG67M6LVtCx1Ah0/J0dDgLL8Evf8uSXzNLE/8ncVNiFe9w6nN7bhKyzN2P3hn15HkaccjYkUK7NgcCHnfXXWydusedgPDSOAgU1dRq7M9uqSdswsmw4HTt5poWxiyXrdZGU67KEYnpLqe6Xan3DeWY+CbVELDesCHmqK9mgZzKU5s2JyIbw5Kh37ktOcSVxAmUPd4Zku4zZs5mInDzO3527lK1sGtn3R48pbt3uQR5nAmkmJlwA6PW8N441GWRtlVhsUmyrFoX/pgLNVk23MUWay19HbG1HuW7vxrYjMXjsVpb2kTXRey5GG6jpeYkEZ38ti1v7kGy6HtJHw6ijQXLA/VPekhGBWdcDNluG7Rqu/BBCeTp/B+n/K95cWtEk28e4lTkbs503aChaLNDNfG4h7XsHjkPfs6qVjdWKJQVIWM6nvCpnFbCneGcoO05ZHmvPi4oRzDNa/K1QP50ejCQOyg7jDmIyndaaSJ6XSFSd6NKQsfDg0djZwNdb5hRZP5lO2m0YEz5GOSLsWiyK4F49TeEXNWoJuRr8bFkzDzuB5ZiDkwJ1ff3yNzEoOpdogza1TEbuvbnJAgebjpzBXMUD5GHzYcaSEVTckkmgNOu2BTfrqa8FU81dPUk6k7xSiZ7bXb0jsEYVxgkAXIRUWg7i7c9RT2Haq6IHnDWHDn+JfrDQvMK7Ifk/sSMUYodL100h26OezI+J5CK6oPVXNFkFnoVtggTwxofSs50Y5yilTiZlfJ6amR7aUnrUndJQlIpNEYE1Az7qHxEEiD4pTpjUPYe+hf2kG8cuZOzS6QdBc7P5Z30GFc9qvYEuBJJIhCiSi7FsJx7VyxaLPORDoxxrCgKWi/2RRH2L17xIaA3fOYut5giaUo5nwCCcllQzjVKUpQTLPGO4zuG6ztpxV8R0dJD+mchs+UcC2OS5Q/YqtdcUgxaVDHdcIFu8TtkSVgQDugNiLuRMe6cq/704QzNR0QuRfZWjfeiWkdEBe0sWt4Ccf2CIv7LjYibLdcgwbHwya12dMwnlLuBa3M4bzs6IMt7C0wIbgKdBCl7Dqg9mXTKHDmb3AbFRNcIH3rKnteTV7PR4CHCGtnRVxBmx20K6b1fb3Ri2XabSG32VEUkVgadh7HC7N3dgWPNzGcsx5prwoSzFL2heWllrxb5wOup8SNDstcNLHE8VpbRCuH0P3KcilDtgwojA5tV07Q/n4NmZFq+l2AT8t0EqYTWcRb7iBstjlohb2VrgaWZOItxVDQCCVFvulU0c41n1ZLMBkWotj7th1RZ9nSKN/Ozgyl4c0+OYopdAEsf1pmhAuXk4wZ8lAtI9lTB90g9IZbAc5cDaqC0MfK6qSl4U1r2+2vtZ6xo+22idNUGHYmruQaI/ikiVeSsL5NUlXJ4S2l0HT0T86mibOTclK2m9YzwlUpBN3lGFks6WIjvpJFtaLlvWJLUjvVAwtHcVyMxvLUVr10A5hdlS3Sd8VA7OVb0YZUKtDiPvZqZwedU9HX8ynNPbzbeWg1tTepnzoYoYrcuTkdRF+9nIwmHz2tQM5eOqX2ANRTq73lnuTq4tZpqtRnFVDFBUFz9D6M5BJvj66tQlzMVMRUSVZj7n0OMi/L4UrFVgsAyeZO0p6+Qnp9sImMx3i/AwPTpB/FbHnpzp5P3ig7dfszdWdQUiuu4uj3pGXGisIZ1bW3yj7LVtEOvxd1cILJjjzpAZacXX7JWJbG53F78tIjs4HF2xpNQoGFnNOYeNq4ucFUdMYOa5osJN/PNnCMHQgIoRhTH25kvIHazdUjBxuG4947X8bArXyBZKY9frjoHrvkLw2yLyIiRFkOII3IDhfJdw4QtbSXnB5II1tMMZPqJ1i9dYamsmbp875nEm3rwT0TIitkU9NHCyfFrrfZ/iTUJAGYc/W3tw9vvz6Ae/vXfko2P7L5f/Z06PmQ5+tPRh6PFT3L/fQ469O/qM/fP7xVTjRr83j2Vadt8HqQ9IcnXx//8qHhvHV8/i7r6+Ph53PwxgrmXym/Rbnb1k01fqmL9PFTEbDDbuv5t431rJ0D3n/7RPR52vM5aBTkX5riS+U1UTU/9Iry+fcfnhtZzdevweshIFj/+p3SF4wkvnhVOVv4+rEBMAx7h9+xt1/+L3wqWx1ULgAA -->
