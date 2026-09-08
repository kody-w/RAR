---
name: "rar-cowork-cookbook-dashboard-manage-product-compliance"
description: "Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_product_compliance", "rar_sha256": "085d90ca9270deb96a62cb273cab077170222bd368da03c78cf9bf6195e28122", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_product_compliance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_product_compliance_agent.py` and in the RCI capsule.

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

Manage product compliance Interactive HTML Dashboard — Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-product-compliance
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-product-compliance-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_product_compliance_agent.py` and embedded as the fenced Python below (sha256 085d90ca9270deb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_product_compliance_agent.py` first:

```bash
python3 dashboard_manage_product_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_product_compliance_agent.py   # or on stdin
python3 dashboard_manage_product_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product compliance Interactive HTML Dashboard — Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-product-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_product_compliance',
    "version": '3.0.3',
    "display_name": 'Manage product compliance Interactive HTML Dashboard',
    "description": 'Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-product-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-product-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37c40a13dc2a8fdf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-compliance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-manage-product-compliance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-product-compliance-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage product compliance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage product compliance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-product-compliance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage product compliance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only.', 'example_request': 'Build me an interactive HTML product compliance dashboard from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-product-compliance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable product compliance dashboard from D365 ERP data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageProductCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageProductCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-product-compliance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardManageProductCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaWLLmX2HeGzFVdbFfhHbc0RED2hBCaAdEu8Olfd8ltNTt/z5HgO2qbved7on5NNgOkHRO7vlkpo9+e7O6Nizqt09vmmflC85K0yj06oWVuwuq6Is6AV9FYoN/C6fI2zqyu7aom7cPb67XOHVUtlGRg+1yl6bNoqwLt3NasDQr08jKHW/hWq218OsiW9BjbmWR0ywQHFuw/1OjxMXPqRdY6cLL26gdF4Ymsr8s/KJetKG3yIqmXdSeAx4u/KhxwLrSq6PCfQjX11HrNQtr0bTg0kqL3FtEeevVltNGd2+x18Uj4N2EdmHVLiCQeou2eBB+6VV0bdkB0kXqevWfACfL/Vjk6fgOdPMGCyjgNW+f/vLXD28R+P326bc3J7UacOuN/kpWtHIr8OSn0tQ3nQGB1MoDsLIcgXVzcA0kB3pl4Jbr+YvX1c+Nl/ofFv/5n0lv1UHzy6fP+eL1+fw2/1G7/CFxW1hN67kLxyotO0qBrd4X27S3xgaI3XZ1/jREHeXB+3Pnd0pFufjz/OznJ5P3wGt//vxWABGs2XWf335ZAIN/fqu7+ff7TKX8+Zf3tOi9+udfvtNpOjv2gGsBMSD1+5fX9YssWPh9aeQvvmgyQ714AR9GpQeI/06/+fMU/UXuZZIvz8U/F+WHxY8pz/r8Gcj7DD8b0P0xWWADsPPtPS6i/OcXj7q4e/nsoZ9/+WdkndBzkjRq2n+J7l+ehEMQO8BaL5P88uHhvr8uli/dvtH852xLEDD/jiZg+Vd23wz1z2g/PPt3pNMoB9nz1Zc/JPejDcs/L/7yT3X77zZ8WPif32gvBalZW3bqfVr89giRv/zkfr/501//Bkj/H8loRVc7DwpfMiuPfK9pv3z5y0/N4/ZPf/3LT10Jotizsi9dnf6I5o/s+uDzBwu+Vv38x72Av5EnedHni285tPitKP9H/bf3xdlKI/f7/ebT4veZOH+Wi1mJr0yfJvhdNjZA1t/Z8Ze3vwH0yYE2AF/mxwA//uM/FmLk1EVT+O1CcwCKLYCD2yjzZuH1MGoW4O+MGrUH7NpEwLCvdSD+Zw/PEhf+4tf/5TyA8KPzAvjVN7ic7QqA7csLzr98h/Nf3xc6IF3UURDlAJHVrSx/ntcCkI5m/Pcar74DqLLH1vsIMvrj/AMg8+LXf4H6lweh93L89YHx0RP9VIqfka/pUu991vESevlLIwfULG/wnA7wSIu5RMxA33wAujdFCspAO9ujSaI0XbgRwBZQu8YHbWCzTzOxX3/91QaCfc6fUI0snkWtWYEF38RZfPwINPPTKAjbz7nnhMXip9/+9tPivxb/3a4H8ZmHDMrGyyNAwoMmnRYgw7oMLAPOAu4F8PHwyG9/e9kXkMlBFQb+i/zIe24GEZp47ldja/vtRxjDF7YHjAwMnJVF3QL8X0Tt+4L3F9/kBUznR3OFCOeK6nqll7te7oyAqgXU+WbJvGgXDQjDxh8/LLrGe3D91a6th4gZSHWr/XUhUjKoR0U6V9P6VZ/A5iKPgPm/hcLzPiBS/9Qsdl9JvC9Oc0wuSqu2yrC2Xjx86+kXUIe+bgfErUXu9Z/zufh6s6keCfI0D1gELOO8XPrxUdxBFIG4cpuvvB9rrLlq6o/qWX/Om1fwW/XsCgcUA8A06CJ3jr0/vUKqCYsudR/2856NyMsL7ssrjxh8Vv4f9Tv83zch37qFxecOhtbo4v+jVmk2xZbjVIbb6gy9YE66aj5dNDeLszjP/nIW+SksSMfvXcxXpPoK2J/zNALxVo9/eq58iPJa8wTBrgZ+ULfqgz6IKuCime4j6Ocgrus5XazP+dfK8AHo/YBB4HeAECCDZt2+MpyffpU0BBaYr793CY8gqR9GBIG9KDs7BUHne55rW04CpJoN8dWr+WxWkMR9GDnhH7SafQYCDdBfACEikIqgerx/Q+vn06+i/2HjsxmatzwaxQ7kbf0gAOTwZgEf7o1aAF9W++zNgZ6fHkSAGlnZzrrbIHOAps+bXu1VXdTMEfHhZVevBCD9cf5+ajrf9YYSJAsw1tP1788kmvElA60OkAHgCIigLMpB6QdGeRnhQdDKZkQAiPvqTZ8UH7dfCnmPzJtr1teNsyLznrkNeKaAlY+/Bw79R2EC6GXzigffv4+0b9xm2jN4NgAAAcevT5/9wvuz5D97isVXup/+Yfj5+d+bjx5F3PhjAHxahG1bNp9Wq2fh/Vp33wEErJ6yNt9r8Mdnlfz4womP33HiD6SfWn9a/Hvi/YHEKz0+Ldbv0Ds0Pzq+wuv1AdagPu7Mj+j89HOuet+xFbAvMhBfs+9GUPS/FcKvS0A1DGqAXGDxszA2cz3tQQl/VALgiM/57+N9zjdQaPJgjs+m+B0OPDoCEPtPv30rWOBR3gLe7txFBt48vT2yo/HePuUAaT+8ASj1/rWpba5L2RzXzTzuAcsDFG0j73H1gImhnX/+cfKVHj+s9H1BewCS0ub3sfeqJnM1/V2KPPUE+jmAw4cZ90Hmg7AEes7M5/SyGhCvIFRnfdqxnBV4DnhzS/jE+C9PjP9Hidg/lIC5Tj9aAIA+fwJp61tdCsz4Qvjflw7rDsSfM/CHTB/158uz/vwjT3quVH8oUYBB1YE8/7Dw3oP3R8X6Id1vze8/Er2AjmOm4xaf5uL74QVq4BsMLB8W32YPYMLXNPgY3vMODNp/meee2aePLfMPsAd8fdv07b8wbO/trz+S64F8X+bYe0bQ30t3mhENIP5sxkcN/Vo5HwX3pfa/kM8fYQjGP0LYRxh9D9ss/bGVXtI8SvAPzO/N6PycRp5rvuHc92SdhQSgP5avdKUL59mErp5YsXoyWf1AACDBo3CA8jub9rvPvluueIyPs6zA0u3zfzt+ewPpZM19zSuhXvMHWA5w9mMzd1wrADuAIbh+AgR49n8zmbxINKEF2mJAAyIxdwM51gYmINezN7iFw44NE4hj2RBBrAkIhmHbRXDStSDEIUjH39g+vt5gHkyuYRjQeyLNzCOLZrFmmYA1PgKw8r4/Brfclz5P+WdjfRuEZr1fav32ZuMoWLlHG377/FCrzdpeoYStlsflFVqpQ3+WoApjpKs1ehgth5tgapvNltgF3gFtg3O1s29MG4UZP61oNkYu1NY3w02fw9rKqvBs5Esrsxt7LxCiY5qRN3Z1hfvX9RUBBBCPWuvd2YxG5GyElsFv9NvRLDNOqwdBw67Hhu/vqR/7G3y5YixvhKlxPVHysCFWSx2MckmlF9ngH4yiPNe1H7kHX7DV/oK2jH8f+PvqLjfY0TAPl6Jl8L0mRhiC1t20HlecWZ0n44IbsFRF7DERyLPQoNGR6ZgpbUyc0anTkDpeKhSKoZrZXWy5ksm562CFmaMauVZqFnVbFQK29ikWPl+UqyYVqbEKg3q8RBUE6znd3+QrgZGb1ZRCK1/Wyet0Wq78lUcdN1hwtdrtXiT46jQVeRjAtaOxVOakaX7aTr5wYquqL5QrT2jSIT3eZdecJGVp72hxS41Vzp+jqysjE4txllPdiMOAm+2VEXSRxGJYcmNAAS+LcggmzKmOsOBGibZnsejk23mKC0jsoLILoq3AzkJab0feWDpNv+W8M9kkdHMWqktQ9v29V+lDYFtmoteQdsYaFDnqsELUggupdsBz6CAsa5Y6EDrRTMQwyfUlNSUHNfQzfbAioWKZY45fdjvm0jXrY+zQnHrD7two1Pud5Irb1aZrSga639Q0jpZWOLZn+XweFc4YG5k14KuHZ5tDh2jb1XmARvZgqsl6uz5ZaWY4dnG5DIkqjwetOZRtLt7QvXzsslvsKJ04as4Wcw/KJVhVJWIWlDI1uzBUZf6OlXd2oHp4Ar6FD7cpNajCgodCw88Ba12Geqshdlul+EGj3MFLOT52bhWRwWE1DUZyhJTbalAloZxuSzG/pGRDnpfiVKriYNx7FiYDTziae+OQ9ejx6ukMN3kriyuXR/2cZsO1hykEoIXkY6R8uZm2Zq4VFEGufJC51VY8QfuQuqXNUsKWtJ5lIVCPnFh2hdKrfu/5nHwafZw+MHg2IbjpF9k1QNyq9nZ+0vQ7bdm0E58abSgfcy2mZJEQzM7idnthM4WcK+4CnzdlakJuPXWcuKLStooroaOFULExXW88zNp5QNimIyJWcDyVQtaFCnutjDQtUKX2+fVaCsLVFqd6OcUYPsjRvNxmK0pwtiJBejY1wpeLfstc7mo3ujMQA3thW1K6x5cq02OX8BWV26P7s0rQ12FDAwX5RCzIYIT8zlOV60U7IMH5HjvTgdGN5ia47dpPRKxfIsqFVluiPTVwA90xu94S8inMGfNcc82VpevwQkdOJIEYK7dBVBwNTuIRWZfVRMdYD9nH0VhHrloZUkKTUX5iJyS6X4YrK3I14itru90osbBstk2AGXkAXdMqUdCNgyMbDubyU1Xmy+ogXJYF35/tAbYQ1izzOgDmTaezolR3S3ePl5IYd4qmqAVI1d1EwN1IbFKNzdkiF/FJQcgcaW+3aef4Nl8cizBennN8W3U71LtZdEdK5HbjkhOPHk+EzrQVzV4sSU3upw1IGwEaU/JY91tLTfKws8aolPgmxY0Bv2stThxAQGSx1Vg8HsQ7DF9NY7OGbXJCUREViwNoiO69c5imriDaDT82ZKFwSCgkGSY5Ps9HlWtCxICrHeIvEaddKhlRXC1GzeiYP/XO4FGRGLKjQyCpfJIOZ0Rw5Nt+o4lU2uOMGctVEwYdRCQI6uaFcMoPI3+bSP5IHbjBsLNDHR+1reAxe1OlvX48FeFWhQenXi83mx4RmuWO15RtzWNlaGp7qeTbihITQxcc2oSL3j1Sja6jRsfvJuHEqRyakU20pfkEabpiE0KXzBCOIsXXMkXEnmWkRukSxnGpYlEwiKc1vW6qfXdaW01aEen2zt5th3YI65bv7ENeYOa4nbrRPo++jGD9pkQovYKGOEeDOoe8s3XQxwIi1ptiR8VDqullhpE+Lu8uR093RAkOObZZUn4fkf5IkZ7qsfTyvKwt7tqOCTHiAX0Sp+XFZhjeOmxbT8dRT+N0JWWd+OzVktBrgyhjprqTCsG25ODUn1T3nhzi/pZ2Z44VmWGf0detJccAc/c2lVOnUKfaINufdxm150+qgpYJFooihazXnEWpF9HEbnfP0OW6pMy1lJLtrXFBlDH4wRGFq8ibU9zeRhu9u0OCXagTsnZxb7weaYioSYRqyYDd7iLVuIo3mk1oEN9JiktLLeFRUxlLAVmubCi8cTSztLHNjYKrYh3wPrOVNEOgxaKnT2S3xLpDx58ZnZ026WlgzZ6pFFgUec83twJmnoOLPHWXyqVtQhrRfCsOgnLYtNDZi1JVAKvD852Pp20mUIWayis8pVDjkI6Bus6bjh/7MqSM7bo8h0Z1zA+xH2FwE2oHoYTQi+gmmwtt7Bn2KsmDBe8s0iiSJqnp2DL24sblz+vM2Uqjl54Nw5rYieGCbEp4RgyUiwHTVnAPq2KQJAOUsCO3LR1lGxNHCPjGFdJCj9NQoy5uCk+oQiurna8f1kXEjmjjZHgaunR9cgbavdRJw6Xo5tJrpzi/xVszkCIHwyphapUdfe0jNIMzcs2TBeTKuJNufaUH5ZmtL5wXIV08hoZl+DciF/aamaR7xm8Ekk4E9VIkgUIZ4IIcXf2YrtDc5JNMVUwEMZeJT/tsuaMKdplfUShBmK3sqNl0BMX8yNxzZwAdFE7trup6cHA4ge+3aAr67SRP9m1DnnUz3VG7XOh4YpxWOKGspWS8Okop9G5uY6Of52HeHVWMHk1s2LWVe7rt1HAz7gqWsfv9oFPiNklu6LQzj8bAb5e+q5ljafLlzlFxlWoMdbkt62C5wzpShrddJffWGPY9xBt1hhNhUfQn3duRMBTfSALDVdMEloAjLOZXAersquQo8oW/Y0BrzXhNWkJ6vLQ7pE8U0T7ATtrJRdubbMFv2QN5IZFyaFNXcbfFlqOiS1/zuqAfipXQ2Mo+HrIabql+e3VO8HW1Qqiqh8tjmKGg5RmCuE323r1tqwSbIJnHfJFPzxOz8w68DO2S6/5+1pQRp/0ckYTTLgdOK0tK3+aI1YZMpKyLUmROh2Yy9dHlkqkUp3TdmUqyZEtpsxlJrdCvWG+hp7iB+i15tgIl4Y/VqeRLuacFJd9ChcNfligjNjSDGtB+c1inDkspV6xtjNpkykuW71gcqtiYO5s7kYoT1DeIUQl2F1ZYC/baWpK7vZOcNft4sE+nW6Kddas9q6jIYOjlYMiEhRFHizrw6f6wjQRRVzDaMRxvd20p7ToJmILda4upw31Xoktfpvt4I+6vEOT7XXofM0S7FGRtc7ezYXeSe8lroq34TX6jbIFyYPgC54gsGvtBgEhc1uxLdo1dDqpqE1bsCthXO4TX+0pthXBXBTKzL+n+3KHJZGoJpfAGqaMMLAilN3QRH9rmEtamIKh4sqq3YZi5agNti9uuhlioF9ZuU7daJY6xsVMaAQSdSpm1D62WZX2sGp2q9ews2zsVPdKGPJ0iJGRiFmnv6rhHrgajHVihXav1hB2AGpIQtKhm1bxgxtVd3Qh1R8Sr8yqJXHq3U0FjbCAlx+VLBlcwGXK6KsM4Vaht4nKvzixfwsfEUAchvjWgmxC6RF33ms2Pu4txrpPqlCqrNDl1TiFfbd1Ui/GaJeW43SUqVtqssg1J9bZZrkoZy+m7Y25vZriWMkhJzscg4uChDCyo5tki9JGRQdKjM14PTq+MuyVdxIxvaho+Vq4hu3I4Ml3DgKBUS8W4rQ4acZFk+gq3QzhSzXgrNCJZXjsYZYwlgSbVxYIr+M6RU2qXjgWX6wMtBkN7b8IDVV0rUh9MKDDujRRvDw3rarG5d1FtikrMdJi9vjSPKxReZlTfqErJJ9oBF5egFcskToL7W+6mWdCv+NgyZV4wAicRmpi9dYK2vPBZhQ/8eKBIZ50azAlf3drTetp2/Y7hrARWuP2ER/VgrNUlE0VlNtK5gRYwGXqQLReJK69v50Ehl6vVxO8FRt0MhuqnjBzenMCkqAqNTu4ZBCsYFlvrLni8qGtnt0Wr/Z04X0TlfJdYKdoWFTt2EbdRtiaMnL1rlSLo6hrd93fr5ME9ku2oiyBNp80S8h3WNC+1F5fxPe4bh+OCkMLxnTTqK0mhuaPrcyqC1CvrWAzHvaoa500sjzowoIwHZoyct7wiqLpmbXzDk+w44LZal28odV068clh0h27OjjleiOIZtI30904I0lf8jJHe+vCD40UHoaKGA5ORwx8exTtWN8XiGJylkwLA39Yh/C1l6EMYdBdjHD9ZKv2lWTUbRcczjZyS/ACkUkLFbGNBXPEmt4b7J3a7OiKnM7TIXN79ZpqFpxB9nQ0p2Kfe9ouXIaR3gWnQMfv7KodIwi6j8vLOLbQVbWYBIKHPd0hgU0X6FqoMNtWBqRNEz0nVN9F0Txbejm2hK/RkhDXGZvc4GN8vToei96gG74rcr82CDy1FcZbZ/W1Bsi0Zw7l2bsk0v1Wp5jBiEvretRd/yYKkLJpwm7nF8edr3mp3rJ4s+H1GGFw9LbdL40VgwRcY8QyDhrrJl7Kip5AzPWib3fC+qgI+uCeqiWRt6GOXmiobq+ThyGOoFXkbRVqAKo9IRvQfeNdj8yNtNa3uvPgMgSTMwmzpiUPOVpHhxm0MQZF9628Wm1sZMXSZJUeKPEqpqvV8YpavHvPuLY93+tIW9plEXKEBptXy7gkK7IbTJZpPAW64uYW1Zc7IFNL164gYDJ6NGnrcqJBO9BDTiBZdo8iaZyvNDAVW63l74Xp0PvVKXS6+HDfYfC+Pg9JlUbEkWyxYMql2tFMz5EGSL7fz3xbQ3DeHaQ9S6sJnzMqu1qe1uCD2aGQo6RxWvFcjujKrWn3ZAZMJASO5FFHiUUQrV2t7xAyQexd6jouNpPRi9YtF2JcvJEExDjijd/0a/+Wazuz1w/BDvxDfd+TpI4QJzQsg0KprfU6EhshDm/nbry1Ft6mobdX4mucb4vmbrCxBN8Sb9pkqb4JOJMUV6Iu5nlzJBV3uN8FphMt6cKkoCsstIjkVPyyKm/0pXICg5IvknnNpzgCdb493DqbJ/BML0eq8E+JbrC7GuVtMNAPhTUwBMbcInWw6W4f2OI+tkayRZX0aCW5jyeevI9RSHY3JMqO48RziXSZEmdqdX2rbfKKXzsIZ/ZE5iKh6TIwu7yQeCp24dUeygHbEDok4o4n4cNuEk97FTmGdiTV6kiHTXdLbngEXXVBagg18M1TsAmvGaxYwmp53BIn16Uu4/VcIzV10KI8iimU2C7HE0v0tovq57NHb4xLm6NNQcDnzQ2rQZNrwcPqllwzWcQhyCZ4bIMrnWhUIjJeYx0gfgWzdCKeHCyV1NFt+3Hjt2mMRejWOJ9pFjvmsYrQYFj2V+pmnfNYxXfygG6xvaTq52pStT0MuzfWQsMY2bayi7RHegjgvKUIffLSeiJarSU30/py4gZ6JZMOV10dlOz2IB38PdvrGEKsThpjRjp3WusnzitjNdu0d9dDGkd3Wcxv8+tupxsejjL43tnj133oD4hwEQxMHzQEOYjK9RIIHt7QXsERnuPhSCVyR8MR1sNhh+jUJZctX0sc60I6fU4KPDay634pOwmxkwQtZU6JbGTVCR8QEUftnSCOOVbeNgTOoykps+tgl62PVbYfpig6tlkv7BU9WG36/hzd2X3CHPa5Th7Fk84nHiYlx1RtLHmUQvdEkFsVNA7+zWaHsydMTntq+fpuWcfJ3ZF3R+XOxKkrI/G+qWr4cJeGVVPcmu1kXIXODmLmzF+3hEDs4pVhSPChMf1y5MfRXTPFyo/heNxnLmTb5+52lcCMI8Dr2p1qQj3dj4pTLU/a0dnDhSmcCf/ErY+gNU/r2wW2neks5ZtDfT5Yu+zu9tNhv+kuQ2Yb3MlYZ7KE2dwudvDp1A5VmvtyZkyyIbXWHrqThLwh/a3A95YYJ4I/3M22X5PkKAXt2mnSu55TFsWljZeg9FpHWVYF6GMpZNheL3HJ0yPt9igWK3J367RBWN99vJw8d3kv8yictMRV1sfIR9fdRpZ0764EW25FpjfPwi+My9yKYB3I6g4rdjK3SyA9AgPAfSUsJ9G9tJTftft24FpFuixdWx2ajkgNjJjaTXe+IK0c9Ql/k494kS4BfrcwXtJp2qFudN3sXVLTwiGabE69ddwuG9W8X7YCCmPj6sS2E+WpnL3HQggf8PVdttz03hz8xNNgkYeMQyzCXoCfYLmzrqfNJtAQKcRpomT6kQITxLA9rOMmCzpTXUoQFTASsotI0CbYLVZBmKSWqX+wGQwy3Htzm/p1fiWuBb2M9wp06Yc1DQt631UuPvXkWFcwmt3vJ3kjWyA53Yw8IdF+ldbI3iNGzFu1shlYK7Wh7XZ5w1mkt04jqZMUlEC+C0f4RhMStCrvFzQt8xXG0u5mdTzwBDwt2dy2Jr3mrLaXPdB6npfYhYjhdjQnnbqzMgnTl+44jL2yXCF3GqZMkEuNN5IjtLnAApHUyGnVkTEkSQkRBNCwD4KD0q4OJQgMkypiylhDzNLMlkUr0d7grqdrfA0KQ9yL3iYRNxlEm4Ft0GrvwzoZMgrsTNLd0yRQPWnvDoNxzWLglX9fhn6tWPv9UrI8x3JthLlPHitgoXtUuWqDHFHZNrrbhm+n6ByUa8aVpUAwHS5CJRyrCQwoHfsBxO/94MhgK0wZNpBmx6dt1ED3QJYMF7lmpLkcMXFNNRtRQYn9vafPwT0MwZ3tdvvnt/mw9OsB3tu/8wrafMDz/+ws6Xkk9PW9ksfhpGe5nx68Pv1bUv31w1vtRECm56lZk3bB6/Dp787MPv4LJ48zgfH5btfX0+3nkXlrBfO7z29R7nZNW49fmiJ9vFsCdthdM78r2cxiOuD792es33g+D1ejIP/SFl9qr43qmdnjraPMcyOr/XoZvM4RwfrXO09fEBz74tXlrOrr1QSgIfIOvSNvf/vf7zanJLEuAAA= -->
