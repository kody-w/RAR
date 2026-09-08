---
name: "rar-cowork-cookbook-report-develop-service-pricing-strategy"
description: "Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_service_pricing_strategy", "rar_sha256": "8bf730aac3bd9611ec16be50c340578447d5496913bd4b1b96b08fc3840618ee", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_service_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_service_pricing_strategy_agent.py` and in the RCI capsule.

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

Develop service pricing strategy Summary Report — Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy
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
      "description": "Dynamics 365 legal entity to report against (default USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-develop-service-pricing-strategy-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_service_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 8bf730aac3bd9611…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_service_pricing_strategy_agent.py` first:

```bash
python3 report_develop_service_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_service_pricing_strategy_agent.py   # or on stdin
python3 report_develop_service_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service pricing strategy Summary Report — Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_service_pricing_strategy',
    "version": '3.0.3',
    "display_name": 'Develop service pricing strategy Summary Report',
    "description": 'Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-service-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '91774cf69a923a15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-pricing-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-develop-service-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report against (default USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-develop-service-pricing-strategy-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop service pricing strategy stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop service pricing strategy for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-service-pricing-strategy-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop service pricing strategy records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only service pricing strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build the develop service pricing strategy summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'Dynamics 365 legal entity to report against (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-develop-service-pricing-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of develop service pricing strategy activity with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopServicePricingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopServicePricingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-develop-service-pricing-strategy-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportDevelopServicePricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1HfF9G2H5mXWYh8URENAiEQAolBCJwVaSYxiEnMyM//vQ+SMtOuclVXdfSnvnbmleCcffa41t4Jv765XRuX9dunNz10i4XgZlkSh/XCLYLFuhzK+gp+lVcP/Fn4ZdHWide1Zd28fXgLwsavk6pNygJsZ7skC5qFu6hDN/hYFtm0aMK6T/xwUdWJnxTRomlrtw0jcKPLc7eewNKqrNvFpS7zBTcVbp74zQJfkovN/9TX+8WPWRi52SIs2qSdFqa+3/y0uJT1oo3DRV42Ldjvg5uLCnwOg0UV1kkZfFgEYZb0YQ2uuECfYsGPfpgtZlMeVgxJGy/0pwYfFlzYukn24WGvUVYosmjiMGybd2BgOLp5lYXN26ef//rhLQGf3z79+uZnbgMuvWkP5bmwD7Oy0p+mHp6W6i9DgYzMLSKwuJqAlwvwHSgJTMjBpSC8LF7ffmzC7PJh8Z//eR3cOmp++vS5WLx+Pr/N/2ld8bC6Ld2Hqb5buV6SAbe8L5hscKcG+KLt6mIOAHAz0OH9ufO7pLJa/GW+9+PzkPcobH/8/FYCFdw5hJ/ffloA335+q7v58/sspfrxp/esHML6x5++y2k6Lw39dhYGtH7/8vr+EgsWfl+aXBZf9AO/fp0FwpVUIRD+O/vmn6fqL3Evl3x5Lv6xrD4s/lzybM9fgL7PNPSA3D8XC3wAdr69p2VS/Pg6oy77sHALP/zxp38k1o9D/5olTfsvyf35KTgGuQ+89XLJTx8e4fvrAnrZ9k3mPz62Agnz71gCln897puj/pHsR2T/RnSWFGHzLZZ/Ku7PNkB/Wfz8D237Zxs+LC6f37hnhbpeFn5a/PpIkZ9/CL5f/OGvvwHR/0cxetnV/kPCl9wtkkvYtF++/PxD87j8w19//qGrQBaHbv6lq7M/k/lnfn2c8wcPvlb9+Me94HyzuBblUCy+1dDi17L6H/Vv74uTmyXB9+vNp8XvK3H+gRazEV8Pfbrgd9XYAF1/58ef3n4DAFQAazr/cRvgx3/8x2Kf+HXZlJd2oftlB/CwA1CZh7PyRpw0C/D/jBo1wKi6SYBjX+tA/s8RnjUuL4tf/pf/APqP/gvo4Scufwme2PblheNfXjj+5SuO//K+MID4sk6ipABArTGHw+fCjWZMBkdXdTjvBHDlTW34EVT1x/nDIikWv/yLJ3x5CHuvpl8eAJ08UVBbizMCNl0Wvs+2WnFYvCzzAd6HY+h34Jys9IFSlwQg+Afgg6bMeoCgs1+aa5JliyABGAO4bHrIBr77NAv75ZdfPLeJPxdPyMYXT5JrYLDgmzqLjx+BdZcsieL2cxH6cbn44dffflj89+Kf7XoIn884AAZ5RQZoKOmqsgCV1uVgGQgaCDOAkUdkfv3t5WMgpgCsDOKYXJLwuRlk6jUMvjpc3zIfMXK58ELgaODkfHbwzLpJ+74QL4tv+r5Yd2aKeCbRIKzCIggLfwJSXWDON08WZbtoQDo2F0CUXRM+Tv3Fq92Hijkoebf9ZbFfHwAvlRn4a1bzsQhsLosEuP9bOjyvAyH1D82C/SrifaHMubmo3Nqt4tp9nXFxn3EBfPR1OxDuLopw+FzMPBzOrnoUytM9YBHwjP8K6cc55qBbARRfBM3Xsx9r3Jk9jQeL1p+L5lUEbj2HwgekAA6NuiSYqeG/XinVxGWXBQ//hc/e4xWF4BWVRw6++oB/3PO8Oo7Fs21YfO4wBCUW/791TbMrGEHQeIExeG7BK4ZmP0M0N4/zsc9+c1btqRQox+/dzFfE+grcn4ssAflWT//1XPkI7GvNEwy7WWON0R7yQVaBEM1yH0k/J3Fdz+Xifi6+MgRQevGAQxB3gBCggubE/XrgfPerpjGAgfn7927hkSR1MJsNEntRdV4Gku4ShoHn+leg1RzFr6EFFRDORTzEiR//wao5NiCOQP4CKJGAUgQs8v4NtZ93v6r+h43Ppmje8mgYO1C39UMA0COcFZwDMocKqNc+e3Vg56eHEGBGXrWz7R6oHGDp8yII+a1LmqSdUfLp17ACQP1x/v20dL4ajhUoFuAsUBJVB7z7KKI5P3PQ8gAdQAKBmsqTArQAwCkvJzwEuvmMCABxXz3qU+Lj8sug8FF5M3d93TgbMu+Z24FnqrvF9HvgMP4sTYC8fF7xOPdvM+3babPsGTwbAIDgxK93n33D+5P6n73F4qvcT383DP34781LDzI3/5gAnxZx21bNJxh+EvBX/n0H0AU/dW1eXPzxxZQfX+jw8YUOH7+iwx/EPy3/tPj3VPyDiFeJfFqg78g7Mt+SXyn2+gEeWX9k7Y/EfPdzoYXf8RUcX+Ygx+b4TYD8v5Hh1yWAEaMaoBRY/CTHZubUAdD4gw1AMD4Xv8/5ueYA2RTRnKNN+TsseHQFIP+fsftGWuBW0YKzgxnSonAe5h4V0oRvn4ouyz68AdgM/+UhbqanfE7vZh4AQSEB0GyT8PHtgRZjO3/840CsPj642fsLLZvfp+CLVGZS/V2lPE0FJvrgBADJ4PxmJkFg6nz4XGVuA9IWZOxsUjtVsw3PeW/uEB/I/+WJ/H+v0B+44g8kMTP3k1Tc6FFgix/BdOp2Wfvkjz897Fuv+vcnWaAxmIUG5aeZIz+8sAf8BvPFh8W3UWFmnefw9hi3iw7MxT/PY8rs88eW+QPYA3592/TtXx688O2vf6bXA6C+zOnxDPLfaqfMwAOAefb437Ac0BmcG3Q+8H74Hr0v/sXq+4gh2PIjQn7EiPcxa8Y/ddiTaf9en8PviXhW4Un0yR20IK8wNPPlf0rgC7cHOfZAy1e/086c1f6JJkCVB+YD5pzd/T2O371ZPibAh9KZ2z7/weLXN1ACLshJ91UErxECLAcQ+bGZmyUYoAU4EHx/1jW49387XLzENLELulogZ+VdKBxxXR/3AnqJoqGPLr2QRHycQEhqRRBUQBL0kkbBfcJDPXrpIauLj68IZImuwhDIe4LEl7kxTGbVSJq6IDSNXQgUQwLgaowIgtVytfRJCkNc2nNJj6Rd7/vWa1IEL3uf9s3O/DbnzH55mf3rm7ckwMot0YjM82cN0yi4SHkde4aoZRCd3DVmoa3apGGDjLp3X2tstLapSdA8eecKItIhdw11kLLWDeXOMltMPOTCpVJWpCScpKwJDU++eF7MRp54XR246UyhoxiS1FklT+f9lbiX1gmqTLFqsmmzy67SOdRY8RR4/onslKsAbSw6yzp3Ayk+DAP6zfSb2jIxL5dKWay9ke5ZxHMvhdOXk3G/JIHU8MJ4uq2C/HwmonN/b+BQR4TmNGwah5VK+9ZCKrWi7S62di65Uxzd20iBvV2K2SRzzphLhmrfUtNOrrWwvKZ5yKpMwfsrOOZEC8UyqDNTQ8eFNqnP3sAn/pRIx9UxTcWe7+4aAfHbsnXcLX3u4Goig76g6BXUUeTtnEJki3sUjo9c1G3dk3wsrxunVlRf4PbNTsfXItNYu5tTQLzjZ3GByaKiyKgrb9WGViL1vKucbs24pn3i9Q6DLn1+niKzut5z7UTY7Zk9pkXnyLYhrAxJKKvgKAjsxS1Pzk1UGaTfe614g85gAlPu2zBCLz480XyZH48SfRTGatsKVojHoZyLp+RmmYguivKKN3YOe8pvurRRM/28o0+dQDUxflzDtoAxjHobJLhm1xKlUc2dGu+H1Mpsy7J0qYkJVZMyvsn9ithvdHfShGvM9i5T+rVZrrFxmFKDgSe7dhVVLjecXRZX8XCh7d0N2d3MwCpS0ZMpJ4Wa1qvEy3ScHK6pBESWRf1YYGe2LqOcHnj+wnPllF37TJCGTj0GK5iPIgTZNsdRFUOVb7G6aG/tsFEHy2CuoSaPBqRyrGHsgxi5WjDfxEjNInvXNpXmdhRajsFTqc3Q027cVtbaOlu30ahVL1zWxv44FM4a36pbwkrV2Cx2pysN3wyBZi4F31MD30+VctQOG6XlJmG0V0LexUuOPJ8OqUnxXXIdDxKpHiXCwYoYynMii088tLeIVRpNUroelMcfdlDQZe6dTXgzcopdWQJkJ+UFYuAVi/d3J68MmsVyP5Vo+gATvoy3PWnW63EQp7U+BV7O6pXsthazDoZszGJnSYgXJWr9G6uxyT4l1xxd79uC2fWNHlXlycf97a71WeS6oySxCOxVUTvcmJMmm7bStT4ehRukM9d2G2/K+qaIHHu45D50qVdURog5uWyZ7BBjvZ2k/ukck1fMSZ3c4rZ4k6xYwtn1Kgrb9PEe9LdRrTIPTPet0TmWhKvFlVpm9vIkVdySO3D0/T6pWXNP7XuLLLfjtdqlsr5Wrt3K6uSttfTGW1XFI12gGAnx7oA4GYycNBCNPYvVrWrvPR7me3Rz0/iyFW0dGVl46WSsfrmZFiHIfaugV59q6S6p9CgdnN0xOvUBzWqZR1T8aakNSeE3AHhXjTEJlehjeLvr3UKsi+2qY8RuvTIlCedyzs6YPOwYfo/JhemTmY+ETp6Z6JXv+Wit8ehSLnDOKQiH3ZQb7QavoPsRJ273XZWSRI0pwUERh9Da0TCDQhtCHQihoErzEqpBSmcoUSYWxuiIuq3PYqGuGCbp9iO+plbs7lpaNOcjfK6vQOa11rTaoXiTq1wYqu0Y2bfVnrsH+LXSqBZ3+tHXTOfI2XBLEfTdaP2psJeao1HGwHVDl1LSZIUdgUubFURIhIQgaQLTV0tIfNJ0D+k2RIdglG+CUrH3a0ANhZDfqq4/6o2lGpuAQnArZtpw4AIacl31ru/odDfZGUHXOCPmuwhFNp3PLUUmP9YpG6InwSn58ojYiULB4S3wSBHKp15itrnFmzRgv7FAeXLayVvN2IUn9KSTSLCclIiUSDFihxGjrqtYznGFqeRNQN/5RiWyxD3ZjH7tm0uF6uj6tvbC066Pwr2/27FT36CZCw1hnUUnq2fw5pbgnX61jzdDc4ZOqgzcOFCrZWeQOXwouNoaDIiTK5TPhOt5EE1cv2vLDZep+yjZ2d1hC3FjbQdod48md7ryGxq+rOv6ThwylIa25zu9lA8RoV2suhuu9Uqqij6PbaZZA+bCYoaLyKt5dJGCuFWOvHHs0d8KS25lj+jGcMhx9A3f9CRVIZrpKqfK5k7UoyCXh2IXVxZz8e2BQ3KCc7ToKPMHHoonjths1KDRjArbWxtLQBKWXK0JPWgBcdJqmtZTyp72p9TBTfcI16Z/gyjZdjrt1lqsBZ0RayO0S9TfnvuQ50nueL2t6dNW2XceXMaZ5HTglL3G0mur53L1EnmdkY7n9o5EJJtK4tVVqyjFrtr9itn22MHW2KEizm/W/GkFj01Q3vl15q2GlFQTGV4jpd5g6QpjHXXdQ3LgeyDIO5IjPPx05jbHzWR0x4Yoz7vA4FX7XAs0vmrMIDtuDWUthnFCuiJvrgXZOCZBK03uTSxgFOoiXuab7W7dbA5Xdq1mtcQNYY946x26lNR1YvgCXg0X1mBlaT/6CX8HXjZvud0pYyk2wHK2i8ZMj9p8B51v/miPnr85trYejVUmpf2uSzYcU+92sc9Pt7HrsGDH8oehXgWqwh+7s9IM5yaX/SV8Tko3n4jdXV+Fte0IU9mCIWoIE5Mkaz0lDUk5TpsljxU7BCqR4LA0MyAoOoqnZWFqhaxgxShG5+7Q0PcTv9lPepwo2MYdTuI1w0RIW+a7KQctW17sON5JIordsOnZT90TrOz1ggdgt9zDkH73NYYet96+tNOhAcH0BF2ddhKpyTg65cjZWR0snr2v8AEX7t4GgTacJmqTnOuQFcMlU10jGGFusXTMK+hyMCBytR8HD7ZtvXD3ObyLu6OTeBLtgY23wnQxvmQlMWcLPtKradjQUBIzlYto+nqV6Fd10CJTNM6CwnMO2a8C3xRwi8PFa8IsMY9ZbxNctlyRA2zt8RUAEn1k9FVVH+9njOFYQliJO1s7LjkJrxSxdWSjLIQVFRRDwgjtlVQFekt4CBpGamkValy1RuHpy8xd81G65iufNg93Fi9Fyt+kQX3L8U3KXbQDBsNgajnF3aSw7Vpa2rJgTEVLQvkqNbaytoqvEEFuJM29wtPRI4WVBeEn0BuVAOmdwUDzs5Gtp6u0Pgn3hBF1STITG2HcDHH8fr28JseR3eZjs+H4saC8u+yE2DG8e0K2PQv3TKyQ2uSieH1yYGmzdkQEkYZ4fTOP9cRwMjOqkpqzmRXJ97MUX4qcaB1he7r1tgkpU3wZ3KTP7P1JAQnBXCJNPPCj5u0NZlXlhsBco0QVvSFqCfa8Pe9KieXj3W6K175ewFmCtwLeCylLQNCWgwm7v5c+THM1Bw/IzRuq+HxYViYhW+Ltcjnh5E63HBM7UMt7pJ2ZjX8+4JxX55l0uY37XTGozepKapleqCl9dcZ7dmv1rqvFNelsEzrep8womMZxRKvsKI2guFHbY8k4zsKV2csuzfdxlYhLNAYMxBPJMnJidwcmPl4YhqvW6foOkR0+B6m2GRslkPp1ucduR1/as814ohSz105H6V6usguyU3xqfbSocvIpAVBbaaMrOydC5ig59+6iRVu80O2W3xWCW5/Ie3bArGuUWrC9pXTCzLakiZshZRABGDXG0tOnQT+etq59vIilONCQTGnDKrxE57YHvVknDqUVh+V6zxVBPFSuOBzWrDvkTSMSJiQzRxFbVnwkI0kwyawvlstDFxwdb8NozBg1PtaLVy5ZqwceVWSsOx6Mi+36hy3KEcq4XHtnRV0OjefDDuXA6CEWC+jitR2R6pkhndYtWnXdZaMSnaRndpsr9abfkzmBCPnO94+5JLK4cDxmRZfdNmbfQRKTtFju2CvIJfctdkGcylgd4h2rrDyKInIoofWzyV2PTLouGfKOl7VgKCXWULiZBOwykVeRIvMxc77pa0fXUnE6BqbNTrdqBzGH7tTBu+hGmD6CURJpwCm6HeIko4TMFrh4wgVHOYsiXZ4iwSAY3oFj0z+wDgAL61RkrlMlt/REXeO+9jPQQtyNZq/VV46Nfb+TuGzI72De8m4r7UIvU9NxaNi8Z1baHaDaY49GEIWeDCIdXWVJ6BUiX93Zlc7pWGIS1R1H1t4U13dMXIIhYGseM2S3wjYWKQNiHrsz42i6UhDGjmh96lAwnGnJAAQAVcNLbDVSW92o0W7yLNbm5C5g4Nt5s0+3q2vaG1BcImBki0LTGHYjaAxkPDkGZ8gXb1RnLxmQaTdhB8XKuRIYIwghdacTOUjEdbk1nE4erR1krJXmnG+E0T2Auf0gsCI0Wkm7Js6HiUHuuaCfblau50lAZXVzThmsHG5xVcoVIyXcHu/VAIQ+yG0zyClUCWJ0bd0rCr+GNykWxjkwIUq2ShTonu4ejeXlsPUwQSjp+FzC5Xl1oPsbfVxhQo7Y9RCj4anXtvcgbJvVZcmEGeghrebgKSOuJK617c9Fc9lsT8geEZF7EZb06TIim6qb0hrX4CjdnaxTmK/VNixzgr0PcLAqyi5W88LfQJhbgk70wODUJjlZNC5fgrPbJIxfaerSipOWa5ijhq03e+NEsNrKOJ46Igeqp0s07OjEd1cW3JwSjQnwk1es1ohxUNIO316cjsP99NCsWzASYLVS77ERITI2goRDqWAcTyCMrto+hF0OMHrH4ahHU1ldq7KCwrAMU+ejYgtrpRd7b1BXldVFOrZJzI6Uzub+wDUW5NRbSKvo/QGl4PK4VmHNvZ9WRkLSR49d2US6FDiEnXQhjUNTvdDSVYlLtHLzLDf6wPTW5Dr3QhptFIHexPd6ZXQTLoU2QXBiusnxlEXCM703i02a1107cTklHRVW1G/pAS/awAnDfHUcg60twxBbtbglgHY0vKZaSB7T0FgZm5rvl213aqACDz2ltDYDSq2umqm2t/N2h/XXTIb6QzliMKu1++YqXJlJ5M8ToQo4XjOtelchKXHWd9ez1PJ4MvFu7+yt0ALU6RY5JqPH+/1WMEjXnwDyCEofpKf+ymX9Vhx4eE/trjiPr44bpD0kbN8k0pkPhZN435bbqoI1ArAKGYu82tjD4Xyuk7HdHSc0cHzKy4064dQAYrBmB/qmNdYYHFa6I09RJkCd0eXAYK7k2mE90XukZGT3WlymBuRzikyHgF4RwnDZCfrEjltHIPuoVc41odjo5UqRAgslROBgqG7DVMV1XureY66FmL53zWR73t4rVJo26FbDRctLpFoD7m865+osG7QIdrtGPuC947LUupdKsvCw7Z5ucBQFvV4aKuEFXfLXXNxT8Y3zuLPRsx3GSpZFbHHjLnk8eQmnkHD3Gn0w9E6h7KUzSPdznnp24Ukmj5VbGcGsYCk72yOBV340nLhm5xjJ0mXjJe3J3J1FGFND1xmhF62Gc0wTXWCN1rPjcBMbJaaIJKXE/nbSZImj3Gmv9/7AkhFWN7JJpwReG3kVOJXiolASFmoYLpe3PHViPIcO1FnpzBC/xMd7DV+6tDgYxala49ttISwPOXYQRwfTlP4UnMvGGKeVgRW1G8US0hWBKkU0lI+ARu+uRY2JZIMKEk2MUUKpuoXLjgx6lUCWNca7yg7FbsUglqpkNGrEh6hLL9uEvm5XU4w3oZFG1F0GY8LRjzNHI7lbfDhh49bi7I2Rm3f8hqdhCimwvF5OjHHOUF0myNJM7/6WuMSHvXxHmTjloOPOM0zI2YPOurpXqm3mWhvQjkNu7F7Q4J3IQNtDkyVUcWGlJrx21xPWm9Q9iKxTZyrX8JxWezKFlVN4VwgKoVtGjTofITamvxYNMxDlxlvxioIMyz1+pLdOpdPwdRuPlA+bUhRqQSuQkk/GR7/2rBZ3L67WViGXbdFakyPKubN6L+cthrqur5N97WmVvaQs6NQmWSAOltqEWZpPMgErNSeUXipzdnBZT3uBlttDfjhYvkes9U4jNYu8iTk8gobDlYdblF+JQ+VNOA4gH4Js4dqi+ybr9WLtsjv5SEvzIDO46nWTrNBk5Dzslmc6xJOhdRFvDoKh5HZb5yN9wy0Tvy0LFeXybEvkmokTO488Tciho04KiR3Sw844nDGjjPZXtckALWpHioilDUs5Rgwdlmc8gytGlKDL1T4zOc2QrjQatYBTl0qvA7UH2eGFVxitTDRbHZLJupF0XHjFtXPL5bjcXUzz3KmqDd3ixkETwsl1UehuiYei7ZTBN9nLndUkYoc7V6EpWoY+Kksw4G/Jvjb2piq5tdO0AlrfKB+B3CXFZF2gJRwV88O0xnHejvjliOjHC2ZDgLKGHe9F2IVy1BbzMVcNB9vZDtwogt6uhramrzhYh5DMgdQQdNPsTzacEAiHTkwJ1+4OyuFUV2k0WLfVqbhYdXi9ICgF5tP9dIYxud9lhtPftxFZY8I9Mg9E59CMoqjbWqs76DiV4a50s5uc3w3KOFIBrFviydMoLqVrMq1Rt7V3F+5i5xBqeWnY3fXziTvsd6szbDSyR+Y8zl96mOoNY1+kiFWcw+0StJKBx52oPkQCydql44FYKoImMuztdF+iyKAZjMavTqZ13C4v52BbDdRyB3AgVFqJMUZsU0w5GD+5fVy7VtJfmi15VCSHQ5YBKVIZe2mRsO3unK15bQgv0WUjDg09chc83fQBcV26MXHYbZ2jihYJaIWKYGPIfYSv7+qUmZo53Jmqmm4c7NVY321wGFbgdaVBFGM6IxQcRxrRndO+or3qIvS76IJ3zn6gWVQ/iQ29NwiKOiBedrm5Ta6tGYb5y9uHt+8P6t7+3bfC5gcz/8+eDz0f5Xx91ePxIDJ0g0+Psz7925r99cNb7SdAr+cTsSbroteDo795HvbxX3zEOAuZnq9dfX3i/HyS3brR/IbyW1IEHVg8fWnK7PHaB9jhdc38OmMzv/Hqg9+/f676PHcW+zKmLb+8XgJ6m182nN/mCIMEHP76Gr0eE354C15Pkr/gS/JLWFezta8XBoCR+Dvyjr/99r8B9DDbq1suAAA= -->
