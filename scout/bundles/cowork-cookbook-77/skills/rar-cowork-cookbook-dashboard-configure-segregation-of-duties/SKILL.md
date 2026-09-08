---
name: "rar-cowork-cookbook-dashboard-configure-segregation-of-duties"
description: "Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_segregation_of_duties", "rar_sha256": "18bbf04672d3a293b386865747f3ec12ab0ec09f043b66ccfc46d0a496915a84", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_segregation_of_duties`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_segregation_of_duties_agent.py` and in the RCI capsule.

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

Configure segregation of duties Interactive HTML Dashboard — Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties
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
    "fiscal_period": {
      "description": "Fiscal period to report on; defaults to the most recent available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-configure-segregation-of-duties-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_segregation_of_duties_agent.py` and embedded as the fenced Python below (sha256 18bbf04672d3a293…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_segregation_of_duties_agent.py` first:

```bash
python3 dashboard_configure_segregation_of_duties_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_segregation_of_duties_agent.py   # or on stdin
python3 dashboard_configure_segregation_of_duties_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure segregation of duties Interactive HTML Dashboard — Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_segregation_of_duties',
    "version": '3.0.3',
    "display_name": 'Configure segregation of duties Interactive HTML Dashboard',
    "description": 'Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-configure-segregation-of-duties',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '25f176502e1c9fd9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/configure-segregation-of-duties'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-segregation-of-duties', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-configure-segregation-of-duties-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of configure segregation of duties with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull configure segregation of duties data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-configure-segregation-of-duties-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing configure segregation of duties.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou', 'example_request': 'Build an interactive HTML dashboard of configure segregation of duties for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-configure-segregation-of-duties-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of configure segregation of duties data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConfigureSegregationOfDuties(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureSegregationOfDuties'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-configure-segregation-of-duties-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConfigureSegregationOfDuties().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a5OjSJblX9HGmG1VDZmBEIhHjrXZghACJBACIQSVbVm8QbzfiJr67+tIEZlZ3dkz3WP7aZUZIQl3vy+/95zrAb+/2F0bFfXLpxfNt/PFzk7TOPLrhZ17i00xFHUC3orEAT8Lt8jbOna6tqiblw8vnt+4dVy2cZGD5UqXps08JYjDrvYXjR/WfmjPo4siWHhdG/vNwrNbexHURbZg77mdxW6zQPH1gvvf2kZaBAXQu0jBqnTh523c3h9mZEXTLmrfBZcWQdy4YLT067jwPjyGG7sHgu1F04Jvdlrk/iLOW7+23Tbu/QV/lg5AbRM5hV17i5+1y27hRnbdNh8WTVG3tpP6i8fvDwuV3oG1XuzawMVfFm2xaCN/UXTAWX+0szL1m5dPv/71w0sMPr98+v3FTe0GXHph3+Vv3v3Xvrl/DNiH80BKauchmF7eQcxz8B34AZzOwCXPDxZv335u/DT4sPj3f08Guw6bXz59zhdvr88v8z+1yx+GtYXdtL63cO3SduIUxOt1QaeDfW9AuNquzp9hqeM8fH2u/CapKBd/mcd+fip5Df32588vBTDhYfPnl18WYDc+v9Td/Pl1llL+/MtrWgx+/fMv3+Q0nXPz3XYWBqx+/fL2/U0smPhtahwsvmjKdvOmC+xoXPpA+Hf+za+n6W/i3kLy5Tn556L8sPix5NmfvwB7n0npALk/FgtiAFa+vN6KOP/5TUdd9H5u567/8y//SKwb+W6Sxk37T8n99Sk48m0PROstJL98eGzfXxfQm29fZf5jtSVImH/FEzD9Xd3XQP0j2Y+d/RvRaZyDWnrfyx+K+9EC6C+LX/+hb//Vgg+L4PML66egUOu5BD8tfn+kyK8/ed8u/vTXP4Do/1aMVnS1+5DwJbPzOPCb9suXX39qHpd/+uuvP3UlyGLfzr50dfojmT+K60PPnyL4NuvnP68F+vU8yYsBgN17DS1+L8r/Vf/xurjYaex9u958WnxfifMLWsxOvCt9huC7amyArd/F8ZeXPwAE5cCbzn0MA/z4t39bSLFbF00RtAvNLToAmR3A0MyfjT9HcbMA/2fUqH0Q1yaeYe85D+T/vMNvQP3b/3EfsP/RfYN9+Ct4fvmK7l++Q/cvRfDlie6/vS7OM17WcRjnAKVVWlE+53Y4AzdQXtZ+49c9ACzn3vofQV1/nD8AxF389k/r+PIQ91ref3uAf/xEQnUjzCjYdKn/OvtrRH7+5p0LWM0ffbcDmtJiJo8gBjj+AcShKVJAEO0cmyaJ03ThxQBnAPQ/eQfE79Ms7LfffnOAeZ/zJ2yjiyftNTCY8NWcxcePwL8gjcOo/Zz7blQsfvr9j58W/7n4r1Y9hM86FMAjb7sDLBS1o7wA1dZlYBrYOLDVAEoeu/P7H29RBmJywNNgL+NgZtZ5McjWxPfeQ67x9MfVGl84Pgg1CHNWAroDXLCI29eFECy+2guUzkMzW0Qz13p+6eeen7t3INUG7nyNZF60gG/buAnuHxZd4z+0/ubU9sPEDJS93f62kDYK4KYinQm0fuMqsLjIAbGmXxPieR0IqX9qFsy7iNeFPOfnorRru4xq+01HYD/3Ze4Q3pYD4fYi94fP+czG/hyqR648wwMmgci4b1v6cd5z0JxkABm85l33Y449M+j5waT157x5KwS7nrfCBcQAlIZd7M308B9vKdVERZd6j/gBS2dJb7vgve3KIwc3/00rJPxtk/K1iVh87lZLBFv8/9xSzRGidzt1u6PPW3axlc+q+dy5ucuc7Xo2prPFsxOPKv3W6LyD2Tumf87TGKRhff+P58zHfr/NeeIkCKAHrFEf8kGygZ2b5T5qYc7tup6DaX/O38kDhGLxQEoQbQAcoLBm698VzqPvlkYgFPP3b43EI3dAaED4QL4vys5JQS4Gvu85tpsAq+q5nt+2OZ/jC/ZziGI3+pNX85aB/APyF8CIGFQoIJjXr4D+HH03/U8Ln/3SvOTRS3agnOuHAGCHPxs4b/MQtwDV7PbZ1AM/Pz2EADeysp19d0CuAU+fF/3ar7q4idsZPJ9x9UuA4B/n96en81V/LEENgWCBSik7EN1Hbc2wk4FuCNgA4AWkUhbnoDsAQXkLwkOgnc1AAYD4rX19SnxcfnPIfxTkTGvvC2dH5jWPpHuUgZ3fv8eT84/SBMjL5hkPvX+baV+1zbJnTG0ALgKN76PPluL12RU8247Fu9xPf3dq+vlfO1g9eF7/cwJ8WkRtWzafYPjJze/U/AoQDX7a2nyj6Y9fEePjd4jxsQg+PhHjTwqevn9a/GtG/knEW5F8WiCvy9flPHR4S7K3F4jJ5iNjfsTm0c+56n8DXqC+yIB98w7eQV/wlSXfpwCqfLrge0/WbGayHQC/P2gCbMfn/Pusn6sOYFEe+g8w+g4NHu0CqIDn7n1lMzCUt0C3N7ebof86n9Jm8xv/5VMOAPjDCwBV/184483Mlc0p3swnRFBMAFkfQ/N5cUaMsZ0//vn0fHx8sNPXBesDdEqb79PwjW9mvv2uWp7OAiddoOHDTAMABECGAmdn5XOl2Q1IXZC1s1PtvZy9eB4H5wbyiftfnrj/9xZx39PCg8kfTQIAov8AFRzYXQpi+Qbn39OJ3QPz52L8odIHE315MtHf62Rn4voTWQEFZTd3Zu8k92Hhv4avC12TuB8q+Noz/710AzQns0Cv+DTz9Ic3oAPv4JzzYfH1yAJi+XaInDX4eQfO57/Ox6V5cx9L5g9gDXj7uujr30Mc/+WvP7LrgYZf5kx85tPfWifPKAdYYI7ng2AfSQvMHQAy+W9u/9M1/nG1XOEfl+uPK+w1arP0x7F6s6lIATv8YDf8Gbef7cZzzlcE/FbAs6mADu7lWwmzhfvsWuEnfsBPJfAPDAAWPCgFEPMc4G879y1+xePsOdsK4t0+/1Ty+wuoLntOiLf6eju8gOkAgT82c4sGAygCCsH3J2iAsf/5seZNUBPZoJsGkhDScYIlhhMrD7VXFOqgJE7iawIjAtR3kZXtLH13SYEpqIPjrhu4GO4tbYzCKWRtkxiQ98SgL3NDGs/GzZaBmHwEMOZ/GwaXvDevnl7MIft6ipq9f3Pu9xcHx8BMHmsE+vnawBTiwBjhjPUVui7J0TK3dWXpxYinkx5keHxA6m6wYh/iED1UndB2hMQ9NaOxxdZ74jKeRCpm11EOqdCanIYSv11WCarJBecQqJhN5bBWCGqyugGbOmYrggbvaqiafciPa7lWhLUutKoYJbqnxYgnHm4SfN9L9T4gSLjXUaw9XzP8em8QliQhGN7uPI7fNSq/2WpQnfSXMrfjVvawDLqdhKbv0SK59pMCuWndXPYWuTWki7M7aSqRHqFtXnhhlZutxPRhcim3R0ms9wfuEEWCjwTDddO39Dro5VsKnPUuibxHLH5NQRQn8bsJFajtpUw7B5JKn4VzLELPCBU7asgFFX5v3PhyZz2t2gmDr9T3tdPnhzUEBShW5TW1hqE1cSEmYDrubBEPSgxKV/tJ2waizGx5rAJyzb7aoVgkJX5BJvB6td0Gh0miVjcS3V7MM0WoqrQXBHcZ9sz91mTE0hcnMWrSQx9fTsTG0G2Noj1HwVJD79xTSMRaplnieK+wcVcO12zNF3cj2GExEyTk5Gn6WRmS5H65MAeG9WgZOljqwJnxJe0UjdVgertJbGrjJhe/nnxV2mWeutYujnlbhYKksjnUJYQ7+DSVu7iUnu9omvH5XjSWJ8muYy3W9J1N8ptRMIuV7o9gGNsFayRbHqRYXycDC+/gc07jVCTwUXy0b9NRU1Rbu12PlZjanlSSvZcqRCZQIg+dd5fTCYsqTVQ2ww3pAxHh40vdBBcWS/zttrOnmyUI+SBBiqpMLbXBeDIIebbcU3sWtwsyHjzmGG54McYiOGtIY7w5vTj140GQ94PHGhnHXvcJU2ujjN3xtXc5Nyp+jvaH+mruj6Nxy8qLJey2hKBj65HitKvenVsNucfEmBKli+XUwByTHIuvWDyZJ4Xjm3O8m0x3V58FiiGpbjV2XpxAfpk3VEZrpESwBarLnWVezsq+gZxLxUWrMJR1wrCzlj2VO/ioqH4wZvtz2Bt8F9w2gU9DgxSiSHVrgjXL34OzRVESbPLscK6wtJeGvCBZwwYLNH5LNN4g8oaqZl1rHd3rhGAWsfNFXtvuCfy07kKDa7SsMOXtys3pPhLT9HC7uXKOB7fkkDily2lJck5PmVTcHQ6Jj5tLbXMSQ3BrjM/SFu18fyN2TH4S1MF1DKGZuCWRlVCmr6w8GiVie9soG60Yjv1k7rPStKv6Gl8u9bhL6xGRismIUltLbV89jgdNOR/IvDHx83nlIfh6Cbl5YlaxzOzRDl7Zy2W5tnZK58mlIsHRPfDxXr5YAXvgRNpTHP9Sc/wG57cT53JRsVZ3jQKynUbhs8xwLL63p/SAWZC93/vTYXR9rUxD3GWUPgVm8DcKvWYp0m0vXehHR0I8MMvusHOx5nKvna2X2/i9PCrQSG5Szk/pOB8h1USaBOLEIybEoPFDxbVQHbt93IjiBWRMQhOejK5X/T2Ucw1BuBCV96OOkvVUlc0aKxQ5uuDmSVMmlqJJlJUPEkqj1zUU9hJktf6uQMrYoNiYkEUBvSSeQrCgaKue3ayZVUHFJ1S2VJ4TVmdeKtJrZ3Re2g/BNJaZLF60kfHgwMIMF9nJWR/5nJrSbTQS3YQ3VJNdaOV8PBz2tugN52ldiZpS4sd4MtoO9bcEfrkHiqxMsUZB02mz2/vbdXza8XIpVOSwV3x5KyAlFzgFY8ZMmkx7fm2MW3dKtza/zvXcFgeD7sV7EK8Cd5Nhsao24VC5tBLotD3cuji8BjsmMYqERlvK7tE62e24lBH5FSttdnFx0O62J25PhQrLHlufykE8+VRvXwRdUNtYWMb7dSqF+81yCJftrYPGm5GboJLZJvSSzg0qqWj8K1TnQo4sd+5+q7PliXS0lLpRq4N4b00h3DUOvDLzg3E0wQ+SM1ssy9EJ787rDFZyDiBoplXuduIzEg+1mzfBFbNHUFs5mdhdt3dOGigufwsidEVsWC8/RSFaY7Zy5WCUQHCJYyH9OozIFVNX7dUrubNqjD505vLNUhzC1VBuio3DoXgjulfTPhj7MBZ3DgApBjrNRdMsB/nqAjbcn5rb6n7g+eNSXQ/Ife8MaJGlF1LEYn9Llr7Yk6d9vrmPJ/1on3W98ne2jWeWUZry0dK4W0FyZnkwt+q515TmCOuscTtyd3fDh5gwEN3dNO6UiRrqdC3Ta9TLR6ZWbpCGpeiqTzqtOJU8DhU2Bx1uZHQXNlmUToh10rYSyBPmsklXIbY+m0mkHrzEt+5ef9ts9skFcs9Swu13ErTfXlkkKSh6WEnOFNQ278ROzKpb1YXVMCiILZ3a2zFzN6Fyi5prFvt5kNX94dyg6D6iy/hKL9PWu8BjCnd0lbAbLDF0/DrYAzPKihKPp22a6AwbF5qBRgdM1fH9Vihtw13LMul7OAa5tJ0nliWbKgixgBs9LZg+H1oKtx95QLtic2CXWLjcbzRcMmmlIA+kKMSXTMx3TqxsN9gJDsfSbtrWJtF9Z2JMBHK5NLVoyjckei17S4XOt2jQTHCCNlCAbvSdVijcKKrdndadjMJq/7y9A45UL4frfmf5Rs8UxkZDPTY02a2ITkYq1VlbxaERbdvtijlI+gT1mt6HUzIu6dgmRsNU+YN8L+FC3RzylWvFsZ9ZjKoe1tG10Cp9D3FrkqZ1biOfQ1WOMyFs9SixkAPALBhWOdHLCqUKe8Akd8wwdQUXTmN+23uygKqGFR/q7FReEcrW9x6l1LtTb0qUNLmr8aow+so1T+GFcmx1bA6Xq+AQWnDZ09uUgKcGcjPOxE0iJr2T2+TYZaMXg1cSwpE8do7HNJNZtZyOnhlRVEQ91EBe47LMoVpllRpaq+apone9btp0ap187uxhnsR4+jJEKYAQ440bVpUrczt9Zd/52tCO09SnBz7ijPNUZ0wiHVh6h0VWyTOYkPoZdkOS9BiTweRlZ1qll25eQsYJaq2QUc8ctj0rFalYYjJd/GGzLDh6c8eq0ttfEWFa7aiOHlsbE6VVhznkAYIhTmdcw2DlVba2AHDVEkDMYpXYrmUfEle5JeEWOuXQiWV1HW/asbxTwfngLm0mzyU+nYxEFDaJV2ScJjJ6XAzqso4S7Cai9uVY5HDqZEtJYiv21h/1eCVQnmvUoeVILCNEl2Jv0ZuqsEHrG9LX02GQd1s727vMdKAHn5GyW+n0NaGLTJCtRo3K4xS3Xek6aZV5T0+byxBi+zyVSFfgIZlJKa9q8n5Zu1tPsxzRteU2UdOz1XL1RV7Gyf7Y11W+jMtDuxqdIK8R0oydfaF4gjCqVUwW1oYd7xLVOXaGNb1+KHZeuTGGw2qi4HMUYl5wVkkyuxFkSPRiiwLBo8FLmXIUA5072zAT7JGmupmOGToItsGRgy2zXidrSEx42U1tq3x9k/AVni9XcdVWPXyIws11ZP3Llrm7gcbcW3yLXzdpCG0IvrBpXNWSQ7Zfs4aIpzfQ2R23MH3DVHUpJzgpRxuuLi674ZBu7iI1ePK11GMat8eLbmzX2Bo7wCrttrp2n9zMuFkHtUO2bg9JpFIk7mZdbSXabphe1rOTdrisbHyaEGownFuzP7rnLSTV1DFjDAz06caAXEvHEgxu4/ReHlcpUkNyfpRZ1ZJsaXfWrQwxKhc5L6dtR7k3ftK73YGVs2UKOEzfG/cju0MY27qIvb29ywx1D8al61BHcbdZjWl22nUb9m5jhmzmsVyJ7ZgdxTwW9Gp/oc0EjYX6vDOYWm0RO5kYZyxXNH8XTwy1Ww77ER2JbdXEGSKofG0RvntbwqXRmAhwzD9Kti7sitqNiW0bClzdQjROnxudk6wgc4RLr68z/e7FOizSa+F48eREPl0q9Nr4Z38bpzCztCJBLG3eH2xr0BLjthZXyp6F3KsXRaTkKxYXlrEqTOhQ5b5mLkNiKafn7EJwLBaexXYblqvNGO1GKWvwErHs26kGHkvJLUIMa1CRSe6V+/HO4exILy/HuzSsAn1/BG0ZPKRpelyNW7xOjVVy6U8NfDjo1MVIKgvGZHiPCPBaUzNZP/tMdTeTvXlIBFGvmVNCBqzdRnHCsfrauuZ+HtUENp2DradEFqDCfSpvyht1PXldrQSKKii81W6M0ejNQqhy54iXDSklIBOsIy7AkxyqZpIaYczZUHIkLHK3Ea9Oe+UMFMVh+hCWmZ9uqmm9CjIAF8SRCC8xym3IE5ddXRwldH/vEZsd4+5uUFQhXjf2zdZfbxtYONXuYDFizuR4VNx0DLQF1QjHabK6ipcmXkumbgugrpe8qu3waKuTo09vt8t22dKW0d51uiDGNYAT8yRJDJm6JokaI0xz5lJQWgNZ2fvKmhxjOdHXKxd11Em88OcBPRVV2tN4Tww956grSi/3q0inJq5xSXHkZXqsLVFEDG24QKu4T6ay3bcuwOuWMIVlFxEyONkM13A4MphrCze/9ZJ0fUD6VtolindfXzLUhzkIZdSrl+LwftkQ9IikKM9oMeW3mxbCoyo/FJonrRpDgo8WT+5oQ7PWvgk2Pd8RiXHNia4BrURRdvP5P2s9HspCGZpc3DXhOLsbEtldTn7sYB2sMwOLXFgZP4m5npLnwtPseF/UtMfbOWiFiLUYQ0RO3VjMoJY1HixdoxeOY9PVMOOIUYr1Dp9Dd44io+tqfYW6Je5kSuqoCLlJhuDmIYbJymMZrcwxVByqJ3IFxo/K/bbBQKN67yf8Cu/yrWu12/ogE1JbK0hfq7cwzy/onj/rilrgXjweJNOMRGUdEqyyFk8mciwH/hio8daNo9YSYiJjsc39zHEC6VodflY8Vu0OZmtY3YU8k9eMsxKLvwIq7PfnykTbTpty1jcxXBVvVqGyBSzDoDLRsuG9u4sfjGl/krcmQoH2rIPg/V71xjwl3CGisJWxOgtq77LLxD6NCT1E8tj48bnPVkS2xvNmHaGjfj3nt0FNTWIl6gGhLpMoQAgq2x2xICn6s26f2G2sKvwNr89Kd28IycFiEctUx57QTXHbG5Zr+Iaf23aejQfkNNWIxpRnr+ClQHJEmCcUkXCOx1NoQSZylXPhivWH1D5uWRfbap1oJ+nBvG2xRrlLTj6yKoedcDFnqb3oXKjhBGBvKcDSMbSTW4OyJs+lZ3OrScuNDdnMYIoQj7pb0PNh+MRPETFI+f6oHU+2nlCQ0Y+YxLMRTtRZRBbDfVQZsakz50Rmq41AKKdTRVVWNE4SEWwGXCz2JEUtK3Z/9m67Ir/CETi9FkVBBYRYE4XgdIdG3aC0akwJz47uKFkEV+yyK7LbFQqxMplp38k7fwnO7gbUnQhbqtOyVpvVSSu5XOYuFiZSt+I4urpnXk9XnyfVFVfhbgIXspzC6qR1MnLxWlMiygPTA85HL2HjpPoaHJJvZ4S5pk4c3Xe7NmB4AeuMwvLZwDZ9NaMreR9xlDONRRrRvqYQIVlpiXlJAg5zJVWlkiuyD/NURRoiU5HOpMmBCIpxd8KhFp8oIY/8g9FABFFO1yDXLui5GdApuFJ1CjL9qjPbqYZdH+1lme6NYSfko4m0kxd05vLSOgR1OUtXnhQdi1pv8CLVk57q8m6CUA2DKr9DWjXsS6iyMaxsaJvkLiV010jSuINDWr0SliaHjAWKqZw3KZYbJqTtQCeipgoFq2732F3lIpxooaWKVaImip5VMj6i0gpbb3QrDbIyQ4MmjnuSvO5ozqGr6gQf5L1QLfn7rWEgvhlunL6XzOBEF54XrA/hntvcejUJybscRyvr4qSFH6o8v43gtLnuNhiq3BMEjf0RLybGZsheUncXgkH6naXgdW+2VEYgaJRhG3lPkmtIFIRKy5hMRWkUL0iqOJtwcE6sNM1J5gTlfNtDuMljqxUgiV5aFsqlrQ0iPeOxY19D6+TJ2r45LDOJA91uRtip3jh3JKkdOXWMY07JNSfaTNZ7wyTyVGcMmaMDxkRAB0c4O+bm4me5Has8h9m9MSmGsEpZHF2drpSuT5vquDvTxAYdnJVzUgKCZgtCNQ5igKxpcMxZa9vyKJGJL551tXJWW150OKQytiLBHDHfHaMLLsEHM7eR3vMw3jv2ZR5Hk5Z6FnLcBRjhVT4ZUxB1ouV+Pd2rqbHU5SnTeIOWRSI7SZBpnE+dJGBBj18A8eGozcDd0leEjKLXtohsHBEljpaR+x3eEZ5z1GGkNPU7xI+W4/kUdWgnDZUIb4C5vtrzxJWTgku1klaTK7FicvOj2OZAYtbk0kA3h2XRm7DEJJ1PMfdVB+dOFmC8m8QaItHYVcyFVUcOhzy/OVdrSQ0VKY04g4khNd6VYa+aIsIKWeTXMtnSbLS0YTHOV9PZAXiYekKx1pusT24VyRr+jsRxp3WdJQ0xt8w+FH6pBlx5UpwD2yOWii4Rcm1NxmGNVlWtrK/KToDTqt8LxJrMg5WnGxxcLJkWoDq1W2PSjvDFFWuPttw5lueK6cm96Ejt2oqGrs4n9OpBvHBFPDiydlCzrECikHx1b/AIJW52N+mKxx3bO3mBz83BwiYatJgw0rGYY63IFUnBy6Vi4QSV+zgsBQLM4Ns6UjC3lpLTaVcYcLJ0Illi9HNUadUG5SJvCfi/Nzvcqsd6AP3orZP9+86dbKY7yRVbYID/oNNGcHZOfs33vCtv/T4gdg7bb5BgRcANguvHMOpBQ4AeE4OiBDLnzl3Ba8PYNdQd2nQpnwWbg48lS/EyHk5Tscn4qABw0lkQFLiwMGHynVliMSXBK8GGcJFRsTw17GDoz0kAuhR38JrW1EE3N/K31ldYOBUGZncoWZqm//Iy32l9v+n38q8/5zbfDvp/dufpeQPp/SmVx21N3/Y+PXR9+h/Y9tcPL+CIMFv2uN/WpF34dsPqb+62ffyn71zOYu7Ph8neb5Y/b8O3djg/ff0S517XtPX9S1Okj6dWwAqna+YHNZv5WV4XvH9/p/arZvDZ9p7Pnfj1l7b48rzjON9wezzdlPle/O1r+HYzEgh4e6zqC4qvv/h1OXv99swDcBZ9Xb6iL3/8X6OYlOtJLwAA -->
