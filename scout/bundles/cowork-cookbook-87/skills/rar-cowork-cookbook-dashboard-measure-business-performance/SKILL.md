---
name: "rar-cowork-cookbook-dashboard-measure-business-performance"
description: "Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_business_performance", "rar_sha256": "3a4cb90dc48f26c747c2e18b6a652e0fdc30524ea7b2293ab270d19b9030080c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_measure_business_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_measure_business_performance_agent.py` and in the RCI capsule.

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

Measure business performance Interactive HTML Dashboard — Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-business-performance
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
      "description": "D365 legal entity to pull from (recipe default: USMF).",
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
      "description": "Name of the HTML file to write, e.g. dashboard-measure-business-performance-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder to save the HTML file to (Documents/Cowork/output/ in OneDrive).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 3a4cb90dc48f26c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_business_performance_agent.py` first:

```bash
python3 dashboard_measure_business_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_business_performance_agent.py   # or on stdin
python3 dashboard_measure_business_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure business performance Interactive HTML Dashboard — Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-business-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_business_performance',
    "version": '3.0.3',
    "display_name": 'Measure business performance Interactive HTML Dashboard',
    "description": 'Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-measure-business-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-business-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c74cb205c8f1cee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-business-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-measure-business-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull from (recipe default: USMF).', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-measure-business-performance-2026-05-24.html.', 'output_folder': 'Folder to save the HTML file to (Documents/Cowork/output/ in OneDrive).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of measure business performance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull measure business performance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-measure-business-performance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing measure business performance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls business performance data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only; call when you want a sha', 'example_request': "Build me an interactive HTML dashboard of business performance for USMF's most recent fiscal period.", 'inputs': [{'description': 'D365 legal entity to pull from (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Name of the HTML file to write, e.g. dashboard-measure-business-performance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder to save the HTML file to (Documents/Cowork/output/ in OneDrive).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when someone needs a self-contained HTML dashboard of D365 business performance for the latest fiscal period that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMeasureBusinessPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureBusinessPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-measure-business-performance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder to save the HTML file to (Documents/Cowork/output/ in OneDrive).', 'type': 'string'}},
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
    print(DashboardMeasureBusinessPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWLLnV9HcFzHlerIvCBACT3TECAQIhEBC7OUKF/u+iE2gmvruc5DutV3d1W+6J+avkV0lAefknr/M9OH3F6fv4qp5+fxyCZxywTl5nsRBs3BKf0FXt6rJwFeVueC/hVeVXZO4fVc17cvHFz9ovSapu6QqwfZTn+ftwu3bpAzadlEHTVg1hVN6wcJ3OmcBrhZdHCyKqu0WTeAFZbcIk9Zz8nltUvmLsKmKxW4qnSLx2gWKrxfsf7/Qx8WHPIjAKrAh6aaFdjmyPy+GxHlQ283LGOW0qPM+SsqH2K0zBO3CWbQduHLyqgwWSdkFjeN1yRAs9upRBCK1sVs5jf8RyOL4n6oyn/7HAgiTL25xUC6mql/cHCAiIBM7QNlgdIo6D9qXz7/8+vElAb9fPv/+4uVOC2697N7JHQOn7ZuAejPD6bsVAI3cKSOwuJ6AxUtw/WYjcMsPwneLfWiDPPy4+M//zG5OE7U/f/5SLt4+X17mP0pfPlTvKqftAh8IXTtukgPbvC62+c2ZWqBS1zfl0wZNUkavz53fKVX14m/zsw9PJq9R0H348lIBEZzZnV9efl4Ad315afr59+tMpf7w82te3YLmw8/f6bS9mwZeNxMDUr9+fbt+IwsWfl+ahIuvlxNDv/ECEZDUASD+g37z5yn6G7k3k3x9Lv5Q1R8Xf0151udvQN5nSLqA7l+TBTYAO19e0yopP7zxaKohKGcPffj5n5H14sDL8qTt/iW6vzwJxyCugLXeTPLzx4f7fl0s33T7RvOfs61BwPw7moDl7+y+Geqf0X549u9I53PMfvPlX5L7qw3Lvy1++ae6/VcbPi7CLy+7IAdZ2ThuHnxe/P4IkV9+8r/f/OnXPwDp/yOZS9U33oPCV5BuSRi03devv/zUPm7/9OsvP/U1iOLAKb72Tf5XNP/Krg8+f7Lg26oPf94L+GtlVla3cvEthxa/V/V/a/54XehOnvjf77efFz9m4vxZLmYl3pk+TfBDNrZA1h/s+PPLHwCASqBN7z0eA/z4j/9YHBOvqdoq7BYXr+oBxPYAL4tgFl6Nk3YB/s6o0QTArm0CDPu2DsT/7OFZ4ipc/PY/vQfof/LeQB/6hpRfiye2fX3H+K8/YPxvrwsVUK+aBKAwAGtlezp9KZ1oRnnAuW6CNmgGgFbu1AWfwK5P8w+Ay4vf/jUGXx+0XuvptwfGJ08MVGh+xr+2z4PXWVNjxu6nXh6oZsEYeD1gk1dzmQkTgN8z3rdVDupAN1ulzRIA+X4CEAZUtelBG1ju80zst99+c4FsX8onYKOLZ7lrIbDgmziLT5+AcmGeRHH3pQy8uFr89PsfPy3+1+K/2vUgPvM4gfrx5hcgoXCRpQXIs74Ay4DLgJMBiDz88vsfbyYGZEpQn4EXkzAJnptBnGaB/27vy377CVnjCzcAxgM2Luqq6UAVWCTd64IPF9/kBUznR3OdiOeq7Ad1UPpB6U2AqgPU+WbJsupAWe2SNpw+Lvo2eHD9zW2ch4gFSHin+21xpE+gKlU5+N8s5mMR2FyVCTD/t2h43gdEmp/aBfVO4nUhzZG5qJ3GqePGeeMROk+/gGr0vh0QdxZlcPtSzlU4mE31SJOnecAiYBnvzaWfZp+DvqUAMeS377wfa5y5dqqPGtp8Kdu3FHCa2RUeKAmAadQn/hx7/+MtpNq46nP/Yb/g2cy8ecF/88ojBt9agL9uhfi/b0S+dQ6LLz0Cr7DF/8991GyeLccpDLdVmd2CkVTFerptbi1nTZ7d6CzfU0+Qot/7m3cMe4fyL2WegBhsAMfHyoez39Y84RH4wQdYpDzog0gDbpvpPhJhDuymmVMIyPVeMz4CQR8ACWIBoAbIqjmY3xnOT98ljYHm8/X3/uEROMCRwFog2Bd17+YgEMMg8F3Hy4BUs4Xe3VzO5gSJfYsTL/6TVrODQPAB+gsgRALSE9SV1284/nz6LvqfNj7bpHnLo4XsQS43DwJAjmAWcPbqLekApDnds5MHen5+EAFqFHU36+6CbAKaPm8GTXDtkzbpZuR82jWoAXZ/mr+fms53g7EGCQSMBdKk7oF1H4k1Y04BmiAgA8AWEDlFUoKmABjlzQgPgk4RPAPmrWt9UnzcflMoeGTjXM3eN86KzHvmBuEZ7045/Qgm6l+FCaBXzCsefP8+0r5xm2nPgNoCUAQc358+O4nXZzPw7DYW73Q//8Oo9OHfm6Ye5V37cwB8XsRdV7efIehZkt8r8iuAM+gpa/u9On96K56f3pHj0w/I8SfqT8U/L/49Cf9E4i1DPi9Wr/ArPD8S3yLs7QMMQn+irE/Y/PRLqQTfIRewrwoQYrP7JtAOfKuP70tAkYwagFRg8bNetnOZndHkUSCAL76UP4b8nHKg/pTRHKJt9QMUPBoFEP5P132rY+BR2QHe/txiRsHrPJnN4rfBy+cSoO/HFwCdwb881c0Vq5iju50nQpBHwPBdEjyuHmAxdvPPP0/L8uOHk78udgEAprz9MQLf6sxcZ39IlKeqQEUPcPg4FwOQ/yA4gaoz8znJnBZELRBtVqmb6lmH5wA4t4wP9P/6RP9/FOhRAP5UIADu1cAaz/T68CYaGFSdPu8+P8vHX/L51rf+IxMDtAkzXb/6PFfMj2+oA77BrPFx8W1sANq9DXIzh6DswYz8yzyyzOZ+bJl/gD3g69umb/8i4QYvv/6VXA9o+jpHxtO/fy+dNEMOgOTZ2I/i9ggiIO4NwASwePAavS7+tYT7hMAI/glef0Kw17gr8r821JtAVQ5w+h/FYR/3Z/5zIf5HqT7sKu/ZKELPxIWeBKG5zZHLYNeA+P4rFwHWD1QHtXE263d/fbda9Zj6ZiGBlbvnP1L8/gKi3Jl7kLc4fxsbwHIAgp/auUWCACAAhuD6mbrg2f/lQPFGBTQNoJUFZFAH81wS9j2MCBHc22AbDwlWhIs7+BoJ4ND3UHiNYIGzcRGERB0X2cD+igRbUBgmYA/Qe8LA17kbTGbJZrGAQT4BJAm+Pwa3/DeVnirM9vo2v8yqv2n2+4uLY2DlHmv57fNDQ+TKhYyNO4kmZMLEmN+069U2KnfvoN2K6sXUGbO7uhWKwUIusNFcqfOaSRzJM2OilWUnTqszdBaWk0qW6vHOMrnS1kcE8tNtdNGndTvZBJRtbMIJ1pAZTPR2OE6ZYTvYpQAZmvv5xV63Ee3oWKmcJ5oQaFMbxhj1hyE2yrO7DnCaFkcJWhK5P+qtPaIpfKereosJbbXKhdZncV7lrengKZe1wZzhVZLzm/2RZBzPraWoIgQvPBWbhjBFc7X0BorbGQfsRseS1ipmaG7Gtayo5qGgrvVdbcewsMFcM9UKrwjCno+Q3k7gXUa5GNtqeKZxaMAT4YYWbwysRyUROsJ2J489W4oKN64OBka322jC8Z0ZQO51FRaiTkDBoEa6SOJLGYIUdrm8BdeYym+OPup1OQqoXXs1dYhg43C1yyXjtHmRB9ZhJYkrRxSPyW2/Jb1rnuC8Ep/jSIMZvrzbS/94qrbYcXIaOl8SYrbFplHtmlsYX6/mMRk5axBsuynPiRWvAst04uvSBGOWdE91VCXvqrq6CzGqbVUuvjL1vsbMZJ2w1jXPJSahD9CWuRX7ld2fuZN2gfN93DdMqGUTIvgVvTtE9IBgl4H0N8qmvW/G+yk1cstwjIvQxpisCDnTFscaO7IXZ1LEgtTaAGMVm6sVPY+ilVxsQwx1NM41owt7i13pvC6FEu71KywW/NSdCgszkfueXCfo5QxlcW4wFB8U04VpedKGZSLj88OGEfhe2CuUaLQ5J9x6+ewTEBNVMMzWgoDTqRCQutqPmhA3Fr1jikA53dUlt6V2rjRSRG6cjstIS2n4eHG1LmrOSLfdmo3Q6aR+UHa1Melav4qvTe8Ga7GRzufBps0TtcecWB6tYgn7mR72RUOFuHiztCMzMAfokK0ohtAQ+MS7bHqT235fnXJSW0pqe8EPkkDKQsKedjJMnMiLmxgMXK5A9HW4he0EhDcEjx7ZFVa4qgaxIyRptcEFVpJAhAJh6XAqDaNWSQrhvFSAIPmEHUR0KL3EjK2ItSnBNbhVpDkG3LB5r8Tr/JCg9yRup93qUu+koxCF/NnyUsj32nOE2kc5KM2N0BKHFcxNfHU6AqSKHbXLcNhOj8Ixgy2TJy5V3e4vzFkwuorJTpqboeW9M0sCYjV071agCQjchLuasYoZOlVUuF2ec2TDo8eAUJTEDUkXG5Exw0h5bR4brSnUxLwXWYPn1U0X8j3O9CIBp8hJFzbczXT7fCgZlOWUDHYN/5qHXmqPxt3h1GYgZVZCCayLgBcRWydy7VykCLG+701Z2/AkE+KhqvIhpnrkET0oJ1jbLKuIjKd4O3rsppJN9QCjxYkbsxoRm81Q8aIhXxU2uHlMPYiijJ5E9hiPVxLurnq3CmxNPZEeVZ+1NWZchr3JJBliY3zm3nYMkUG5J3QB3K/ynD/k4FlMC5SAb8rVzk5JmxKzQ3ohcb9PhpEtdBS9j2jiQIGjRnGrb4ptSRy19u6JQZgF9Khid1nnOMHVaGCUrDOMYFPxjD4WMmaVEQtX3GHnrdhrcOCJgtOuhhkbGJnbt/A+VrLE6GeK8qDQdjRv4+M2YR51TmNWg5hAJ2K9ttoOkTPHMLTbLsXUYZmcyxLN5Aan1jtsqMuL2ptQmTJZWPKNcR6VIjpVKaUYm2wtCNsR7ZPKdq6XqdtSuFJoxSlMNfeWlysGK2W1jNEguhpeyafl6Va1fGTfIG9koGR72LIEj2Cgf44zZzxsU6lh0IaE1lSkOwR93m1pIi3Ndc/7dJWaFY8HyrG+6fdDQ8MdfpdUgJqMym3bZLvOiPhAw3wEd0m/vClIqV1GiW4jixna8ArX6WhSXclnKCwz3uFAjUO7Sh2AxU0eqUHAB0nrkrRV7rTeErkDWVDbc1HeN8teZRGsNdn9eSqMpmXIfQ7j0SW9iFhFySTinM6WVWgObffDiVTTNkb1jbyz81scQTW5FMkwtoZ9usHkcAMRfK3Ksgxnza1RTydpd1McpmVcikX5vTQtd7LgaaavT1ePn5T84m2qMCmYw6oliHUvXA8dHIuBeKxp7C6sCWWd2nfBztRDHMDjbXCsW2MLdH0O13XB8UOvqavbkqN8/H7KIz3uOMPx7yta4aMy3YAuBCqVcYXFWZNPY7sZhH1I1gdtsMlWQwUYudbNXtxIdGqQ3PXUWgHHdLsD76LEJWIJksk2vHIpJHQln3H+tL2sMBwJShFbHUtuO7hQz1Cbs3K8niFl7QjryM44AT/hS7YXePysHVX9DrGkxDkRnALapmiU3rFL7mIJ68VNFO4kVNXijkiK6oiWZqB7zJmCth1+yKfr7sAcrTLc4yXcarKuXlJ2q/bxtD5QXBJxkZpkPagodZvYS9fXad6grD4/3LTgvOXXqr+VYxyihkhvYM3LmQLrBiUi4koQWW3UTiyrafYhwbKdokgjczlUvJdYVnc27ne/AfgCR1cp2Wq9EI0FRbLwONgUdbbi/hxwVm6gqHrYTtQJWiN8AQBVb4oN1gTqvgquUnVlMQOUHL/BbPacSeigYyfl4BGrlQLVBV3xihNL11KmB87bp0gq3NE1b6v8ziBh/ehOzWUdOJnqsauCS6qo5jSzFbKpiShVqO0U4LKRXOLEKurqfNPiNhN3fMU7mza8nOIhgreJxkJ+DeEXO4lOPa8qZep5eQLaJCvR4Tj2xbqYWt/1PJQZ3Ru6vZ/uok0S2t0iKZoqD32wQWBdp/O2FQhcPwsHAuvv7BSYZVz2d3u9naz1OPaXTrIpf0lOXcWyzTUusGtFCXxulEx0qbEzSy6TmKsdGL3QRAKDDqRaY5RqMiSj2uuB8D1NQI3dnd+ex2B05SuX3AVHYvZwIzjLeoXml5i6rHa6UKxa+qDejhilJ2ycHcs+WiV6NDi+N92O0s2I8BwdcyZiKhNAk+qUMtLowoq5baODoG7b4nAFyLHkKZIOIAAGDiYwS/+GYioJQUi9a1uJA43lEMu70+QOeLBCE/UunY9DSWwL06SvNEmfQ35nHkKxz5f5zYKCdl3BdHjJAyQT+G1sN3o29RdDYMZzfDUV9g5Kwg25YMcWkSLPanjSDbxNUyx3CBWUVKYawb3aaol+pa6X6NrrGR3z247aeqmTTqOJRVvkdrzXitpMDd+ghwsNnaTaQSW5OQcITKdopluqzjoFtoVbuk296LzlVpK6U1qh5dJCYEAN0dRWtLSDDKw85trAwscoEE7UJrPpZdKFJ/qup/HczE4bwpGHEVtCRBeyQoG110Di7UaNLtAaINVWGhqoxwSKxqGG8XvsSh53+JEzUNiYUoJzWd0w775Cm4NMDgezqyu5smoVyYbcqVuWCrKTIVk3iqMj07x0+DnauXs52bfT6bDbMd11v040J99yB1sNrPhI6+aJFrUiPZ/h/R2U3V1nnu66C6XqJmkTbvR2Z7PtQy2JzwZE+9x83oQg97K+pNzQkkLU3c2rQxqb5bLtKa8h85rml8dcuZvr226tedvVXoDAJJN1jKAaCE4gWamV6IlYrZeJndv+2Z88ADkDUieJJfpJxW29+tgaNmjIRYMKKkbKVK50aPjOXZZ1dr3h++OGW449XDOWuKPNmtc9sQLTrKUnLe31YRmzrocdw5TfXhkwHWSFgNRKdkZu0lE1MtuUt/sA54qxdgqaEDlajuQbwJI73iZ7w06dTK4L+ayvopxPJ/Dc67mKi457oxFNSsIYqloBaD7ocrO2bXfTnJsmK9Zy4W6WE64nXq/Vfc0dIjGQEauLd6eVE+ui20/ndeNHLLutawTbyYRmV/bESauDFxrL5VIYqkHjkEiLzoeoYdx6vRLTHIbFi2+RtV+YLqVi0VmI2gjj5CnmxuMuQar7yohc8crtjpm5XGnSbbe6SuUOLeUdsj9FN7ifOCgItToQCyG95XlxRG6IvYfJlFc7TgVNY4kjva7dT8MdHWGvBYPdVuFOZ9lg68necifxwq9XRu+mDTTozq0iQ/1o6Es0gpLlcq+N8f6MGdM9Zy9eiRN5hGbc4Fb6cD27m5rddkK8t3bRvjsf5Jt6qDh77Ticq5UkvOR2t9sN4AC/coteuN/g656WupN0Yqc7IbrouXXuO2mvZi1WH47yCtm6vOQQDL0lT5uNSdX3yWKk6bjhN34Ja0IvmWrm+krE4Esk0n16aWWHi6uEscQclETieTYwnOh62QnMXVtzaQqLuQNizomPk3GU4NiWh25/EJaRzqDi6EFbK5QyP+mOEcq7a1RF8vioOqelbIG+KiqsbYPh0Ebc2+2y69o1MsVNm5Sj25t9QE3XIr3T10NJbdpkRIRb0ZnV5hRjiS9agnPBd8Guj6BIXC03K3rARFe5mLsyo0xSC6UVPk5j2NlrxLytHYJs91SBCJ0bdIE/upq9h/ZlejjYuHrTNnunu65AH4jEJHVjlSJWC+Ga+1hw3+feyica0K/18b7NcTghBMJaqa1xnZq8qc3lZcuwI30k60Bm4GBz3g4md2FV/QjZtYP4Kjap+To/NZsEA1W0sUM0M+T2oF9RC7Lv9lVEIdPyRQTZmUkFZr8rgoZXDyEQKIeSgNtV/pIXj65ebNgYESUJcSGSvEDYWdEuNaJq676DRo3o0q7yLLbv9LtPdW3dEPZ5utmml6UWV8awOMjaiF75U92e5HK1vcUrvDl5A0nBinoAQ1sCOq1TtBP4s8bcxwGvjyR8BHmiwWAu2FxLq5Sayb13nYIhTHWudz2yFGVvtU7TkjFOxU7zStBqXkRjLS03hr7nfNSmqTrdixm0QZE+G05qwMOy2+94iIb7O5gHGyzIUiWwvfSkEmbeMAPeJXkrl2LgSpXB3labZa5ocnc19wdkyHJhaQ6I5Yag+A4emIe2x4vAEMEp8SXkLt6raQDdR2KtpGbvHRK5WuejvbZxv74GrjXou5N89XYXnDQQC7YQEpGM5QUxCC/dqsS9vaqeOoyGeYGXvLGc+FxT82zSRnxErDCz9+nIJGIUwynH4niLmR12hkV9ld/bAwh9Xrhteko6a1y9jTusGpy4YdShEnJhz1Yy1FPt7RiKIny/lYmxko5QbgHRzU273GzW5yMYDG2R31NJ5hZLmnEa8+zcr2tqNR1FiL3hY3doRwh1WA8qpt15NyzhsjXglNFWt3vRHQ5FD7cjswni3JQs787c4XqQ8MwGUWDa2/Vo0yfpekvtzRlxEBfHyTobew464b498owBeg6ljhpMjVB3mzeiRe8xLDVG2URb0FslRMgzcJMGsByBYrFaVwgiIDudkq7KJEl5GSSIgobS1eQtJ0aMYxnjohDjkinuUgndWvFh5zaKjKMdR9lbqE+hmtWmKx8d481qs+f0UD8s1csev41WZ2OKi2ylU2AaJj0OQQE8FanXribDjlWWwXrCjcRWoGIZbjSp9wLUi5X7flr6JAfMl2ojwlrj4G3u3j5hMHtQ3ZW5WpsMpPrQxtEBvsJEn7CysJKWxYiZq9Xdu97UnNSE0IMnSgro+t7D+lqqVpiGN0hFWKw+NaV/vMqp28oH3l8F66xD1sqeUJRNL+7HyV/HMOVl5YFvaEnwLXflt/YqQihtnR9J/I5pWngvsTPfWKzE7W1hUHIuC8xpuccu9wtBnislhrZ0Aa9O2WlrWQfZP7DblEfx6/7QHGsWQ7vbyO9he1W0qAJhtTTCKndGHQxBe4S2Cydu7+PaV2U7vOtmWwc0eXLPaiXmtUyZqMCI1wNMId2S3hs15h9NC9rbuUJWPFcrUAilJkVKwLlESoDGAgGQhdSkfOpE+FjLo8sTon+2OAXrVz7q2vCUp4FRlOqYTx2Bh8zhqsetZJHiXsrMEXcNQzqjxoW74TgbeRwpdlJR7huqu58EUyaVAt4wrumsZURiLf2iTtoeMwh5qQa0uz/TZGkcxnpHSlvKgE/0md1sioxGa4IWDrp/XOK7C+zHXHi7J1zpl7WX3kfEDjq3cU6jn6I+Y+jy1elkMbTqITfF83LTaahrLeVAK4Iu2iu0zevWDi57e3tfxza73ZybGILgYUjRC3HeE42Sh4ib7fO2ZPjWDbtlfuh4fEinCSFtqNBjVcBCVutWdzBwN9dMdmo84oQQXppX+WAbBxAE7BWzOffA9f3o6uthytFmcAOHSI7wSRXr1W5VBwSx4W+3CyRoeWtRVaUe7NY/IK5wW8L9Zb2J8tZPM+Z0odIsH1ol2arNXhEoyFDX/XYXwTxKtSgy+W67Pk4eHq3VU3CKvJowTY+rMGfT+Ta8hahdcxUt56pA7HgOjYAN8TEZKoxwdLRvhqzFWxxfh/WmY0NsbKjQ3RDRZhVoBxayiB0AkcSnR/xY3Aih2LtTxaKuoHsCq/k6vGo8fFCgY5+CsRg4LcDW0GES/KDRG8rE3GaLIjjqufnkOvi5XsdmMuB27IacRRkHaOnBwU487RPYLDc6jkuopbr7EzriJEGBdGCgGIZtLtpKlz7kriXtWHQ1UBqrscuGgypS3lGKDpNoqkf8+bS3LmHWjgVMa3GjiSpKHBRiy6hGi4JRTZMxhycDH5ERLmARyB36Ua3POM0teyP08NhG4XTydH59lvM09QM896cxPyUqfbfWlyt/tezIgtc6BXU5BCaCOwQVIVOP+HqL+OMy7mKcb5GrLa5R+ipB5HokBKqh4FOoWPW1dULOxgJyuEncUmIpQZuPSv72t5ePL9/P4V7+zTfA5rOa/2fHQs/TnfdXOB7HjIHjf37w+vzvCvbrx5fGS4BYz2OwNu+jt6OkvzsE+/SvHSPONKbnC1bvB8nPA+rOieY3kV+S0u/brpm+tlX+eJkD7PguYlN54PvHM9NvbGcHVE3gOW33tau+vp2lPl7vKQI/cbrg7TJ6OxsEe9/eKPqK4uuvQVPP2r69CDA74hV+RV/++N/aHsnYUC4AAA== -->
