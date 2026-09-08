---
name: "rar-cowork-cookbook-dashboard-define-product-policies"
description: "Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_product_policies", "rar_sha256": "723362df79a243334eecd97b5826d981832976c8f6f827542108fdb7d9efaf38", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_product_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_product_policies_agent.py` and in the RCI capsule.

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

Define product policies Interactive HTML Dashboard — Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-product-policies
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-product-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 723362df79a24333…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_product_policies_agent.py` first:

```bash
python3 dashboard_define_product_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_product_policies_agent.py   # or on stdin
python3 dashboard_define_product_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product policies Interactive HTML Dashboard — Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-product-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_product_policies',
    "version": '3.0.3',
    "display_name": 'Define product policies Interactive HTML Dashboard',
    "description": 'Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;',
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
        "upstream_slug": 'dashboard-define-product-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-product-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6f160fde228b570',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-define-product-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-product-policies-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define product policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define product policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-product-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define product policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;', 'example_request': 'Build me an interactive HTML dashboard of define product policies for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-product-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants define product policies data from D365 packaged as a browser-openable HTML dashboard that viewers can read without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineProductPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineProductPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-product-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardDefineProductPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPaWLblX6Hvi+h0PuyrCSThihfRmhFICCSEhnSFU/M8oAFJZNd/7yPAzswqV9eriP7U2JmAdM6e91r7WPz25vRdXDVvn9+0wCkXgpPnSRw0C6f0F0w1VE0G3qrMBf8tvKrsmsTtu6pp3z6++UHrNUndJVUJth/7PG8XfhAmZbCom8rvvW5RV3niJQG47nTOImyqYsFOpVMkXrvA8PWC/58aIy/CCuhbRMktKBd5EDn5Iii7pJseRoRJ64ErddAklf9x0cVg0dAkHRDqLNoOLHHyCqhMyi5oHK8DUhbbsywBlW3sVk7jLz5oF2HhxU7TtR8XbdV0jpsHi8f/Py5USgB7/cRzgFs/L7pqVrGo+q7uO2BZ7gfNX4CzwegUdR60b59/+evHtwR8fvv825uXOy249MZ+08U+/D8+3T++vAfbc6eMwLp6AsEuwXfgDvC6AJdAxBavbx/aIA8/Lv7zP7PBaaL2589fysXr9eVt/qP25cO6rnLaLvAXnlM7bpKDUL0vqHxwpnbRBF3flM/YNEkZvT93/i6pqhf/Nd/78FTyHgXdhy9vFTDBmTP55e3nBUjHl7emnz+/z1LqDz+/59UQNB9+/l1O27tpAFIMhAGr37++vr/EgoW/L03CxVftyDEvXU3gJXUAhP/Bv/n1NP0l7hWSr8/FH6r64+LHkmd//gvY+6xGF8j9sVgQA7Dz7T2tkvLDS0dTgZJzSi/48PM/E+vFgZflSdv9t+T+8hQcBw4omw+vkPz88ZG+vy6WL9++y/znamtQMP+OJ2D5N3XfA/XPZD8y+3eic1C17fdc/lDcjzYs/2vxyz/17f+24eMi/PLGBjno1mbuw8+L3x4l8stP/u8Xf/rr34DofylGq/rGe0j4WjhlEgZt9/XrLz+1j8s//fWXn/oaVHHgFF/7Jv+RzB/F9aHnTxF8rfrw571Av15mZTWUi+89tPitqv9H87f3xcXJE//36+3nxR87cX4tF7MT35Q+Q/CHbmyBrX+I489vfwPYUwJvALrMtwF+/Md/LOTEa6q2CruF5gHgWoAEd0kRzMaf46RdgL8zajQBiGubzNj3XAfqf87wbHEVLn79X94D7z95L7yHviPo1yesf33B+tdvsP7r++I8g2WTREkJQFqljscvpRMB+J6V1k3QBs0NAJU7dcEn0M+f5g8Abhe//kvZXx9i3uvp1wcNJE/kUxlxRr22z4P32T9jpoOnNx6gr2AMvB5oyKuZM8IEAPZH4Hdb5YAVujkWbZbk+cJPAK4AvH9SDIjX51nYr7/+6gKzvpRPmMYWT35rIbDguzmLT5+AX2GeRHH3pQy8uFr89Nvfflr878X/bddD+KzjCAjjlQ1g4U5TDgvQXX0BloFEgdQC6Hhk47e/vaILxJSAkEHuknCm0nkzqM4s8L+FWttSn9A1vnADEGIQ3qIGHAewf5F07wsxXHy3Fyidb83sEFdtB9i6Dko/KL0JSHWAO98jWVbdogUl2IbTx0XfBg+tv7qN8zCxAG3udL8uZOYIuKjKZ9ZsXtwENlclYNP8eyE8rwMhzU/tgv4m4n1xmOtxUTuNU8eN89IROs+8zCPBazsQ7izKYPhSzrQbzKF6NMczPGARiIz3SumnOedgUCkAEvjtN92PNc7MmOcHczZfyvZV+E4zp8IDRACURn3iz3Twl1dJtXHV5/4jfsDSWdIrC/4rK48aZP/JzCP+/UTyfUpYfOlRGFkt/n+emebIUIKgcgJ15tgFdzir1jNj8xg5Z/Y5ec42z848uvP3geYbaH3D7i9lnoDya6a/PFc+8vxa88TDvgFpUSn1IR8UGcjYLPfRA3NNN80cVOdL+Y0kPoJgPBARlAEADNBQsyffFM53v1kag7DM338fGB41A8IEQgnqfFH3LkjaIgwC33W8DFjVzH38SnM5xxr09BAnXvwnr+akgboD8hfAiAR0JiCS9+/A/bz7zfQ/bXzORfOWx8zYgzZuHgKAHcFs4FwHQ9IBNHO659QO/Pz8EALcKOpu9t0FjVR8fF0MmuDaJ+1cJh9fcQ1qgNif5venp/PVYKxB74BgPfP9/uypGW4KMPUAG0BBg7IqkhJMASAoryA8BDrFDBAAgF9j6lPi4/LLoeDRiDN9fds4OzLveRTgox2ccvojjpx/VCZAXjGveOj9+0r7rm2WPWNpC/AQaPx29zk6vD/Z/zleLL7J/fwPx6IP/97J6cHn+p8L4PMi7rq6/QxBTw7+RsHvAMmgp63t73T86YkYn16I8ekbYvxJ8NPnz4t/z7g/iXg1x+cF8g6/w/Mt6VVcrxeIBfOJtj6t5rtfSjX4HWiB+qoA1TVnbgL8/50Vvy0B1Bg1ALjA4idLtjO5DgCqHrQA0vCl/GO1z90G8KiMggcg/QEFHuMBqPxn1r6zF7hVdkC3P4+TUfA+n8Jm89vg7XMJgPfjGwDV4L9zeJspqphrup3PfCDqAFi7+dZ8ApwhYuzmj38+DyuPD07+vmADAEd5+8e6exHLTKx/aI+nl8A7D2j4OOM/6HpQksDLWfncWk4LahWU6exNN9Wz+c9z3jwZPmH/6xP2/9Ei/o+s8KDsxzQAkOcvMwc5fQ6C+MLyYh4PgD0PnL4B8+fu+6HSB/l8fZLPP+pkZ8b6Ez8BBdce9PjHRfAevS90TeZ/KPf7DPyPQg0wfMxy/OrzzMMfX4AG3sG55ePi+xEEhPB1KJw1BGUPztu/zMefOaePLfMHsAe8fd/0/R823ODtrz+y64F6X+fKe9bP31t3mNEMoP0cxgepPooUmPtg4Jfb/7KXP6Ewin+C15/Q1XvcFfmPY/Sy5cG4P0j44/rcU03wd+bMk7AzT+Yf2Mp7Tp/QExegp1Do5x9oBCofHAGYdo7k7yn6PVDV49A4GwcC2z3/jeO3N9A9zjzOvPrndeoAywGkfmrnWQsCGAMUgu9PNAD3/v3zyEtAGztgHAYSCBTDcNQPiY2DrjAMWwWB528Id02iuL8hERJDNwTukSEekiixXqEITIa+S/gb0A4hRgJ5T1D5Ok+UyWzUekOE8GaDhisEhX1gB7ryfRIncW9NoLCzcZ21u9447u9bMzApvTx9ejaH8fvRaI7Iy+Hf3lx8BVZuV61IPV8MtEFcCJPcsTGXJbwcVcPft8mFHtF8IjasCYYwjTCrwk81NIPXwtqjopY5qdElzvg1K183vLzFd0eUCdbYvSAoijvlwrnsUyjRNVFDWYTY3O7kvSsua6xgdSLfy0k+NYE47TOthxN1X9PcrYWlq8xcNW0ql5BCXLqlCB92fc6UegvdBOy26u9yhh4ScSOnrZzwTN91/Q7OV6a7Y6VkwpcQ126gDeRm+SWqJX0/0j0v11vRr7NdoV6kVt2lvFUbFsNtpqsqX86wNg4O1ZTqKRKi+mxxibVPJts/FJID2YKLbVaisztcqfbO6W4t5lOh31hot5QO2RhYwuSrBhNt+MpIdtbpmhBDO/CZo0FIJW/TadUarj0tg9u2Q/c1vglvYaEiS3LAY9HyhZYTeNvdnYq0yJpRs0Yxau7ersg21D1MBM0uYEny2E7McF3ZBLi6deP9ILZuFAkn45rnrOQG8jE7rTpVPiQ5SboiZTnIrur5SEDdnVbXCZXxnlbAGh0KNU7t763VXRWzdkm3oDUlIhDqYMdIlsW2o0ZVFI2REOTwrdLwKUt3fuxTQnCShethku3r2lihyVmtGz3UazfgDJima5G54aspvNMrlejvxHQNjI0yePVOKhL2jOiaLmjnA0wKzO5gi0vE37VqwamOcLYveRRhSkGFOBbogmtWNt/W6CpGJKkkb1wmIHLJjvkxx/r6prkdHB3Xlu+pkcHZW10+O82J5wqU79phV66jkWVy1xbzgL6PRJ1bvWgKw/3Erze0akcuohPehbFslIrGXZmdSRhL0EPjbuRDv6vH6krrB9eBd/51YDrphEU7t0MvzoarD3LW3+mkImhn4zuVnnlaG4eJZJI67xtrhedNLYeinKitVUqu4tNwJ08SuVNbsUxiNF6zdqswl0NxPEES3pFuafHcpV83B3uk5fRALo/I1i6Es3FHo748pKpsGol1uQqx5oe9P62WaaMXdOBtPUjgIZKGIjYMleIwQROzzZbleYv70CjfaIEoDHKPn1KKl64TKieqhnJk78s7XiFbSb4mPGiLdUMznjxmvjgc0zXb4xSCJPrIbqoitda8vlO62vK88bo8d20sE+E+qi5ZoV25wenb4SCOVB0Hp1UWWDcuYpjqxg7SaPDD0aGVIDk7A1eQ/ZHGiqV9tgtju8VabamutEvA3sgxqQujyItmhVFOchjQKLq6p8GnNX8r3sR8d8zzzXlUzjtc6HHaWQXKWdWRnREVxMUkDrhzdNr0ckN7bCuYEXIbUpNujscYSYZ4X3bU9aCxwKREjXptONqCLuNpyLhgWqM0G0pu4X1U7TorTwbPxOyeS7BaOHXRfilzfL7emORx2IamNZ1RCqOUmlxuGdkyDhNhasoGAAhMHDbyJtf4bNjT0s6A/QHdWXaZn1hFiBvntLdNX+r5xqDXtLgWNZmtlDA4oOe2RS9V1sZ4pQQClDsecioP/HLjd9EtoeW1eRO93UB1SNNufQApTHlfJ9LKPirFzoUVkYPbVAli8trKO5iJAlnKKPzM7yQPyQpHH3bywd1db4xfEnspwsqm21ginjLMermB91pI+JhNZrJq6AwWblVcua6nwbq3GxHufbil3VV5ueuJEQ77c170ri94KmFvlhtcQs8qYAu1uifOgfRGOmUMJdcpFyqPPi+C6giliGI0qchuAocIFe+wMY9gm6g1Ze6KyuEuMVO8IqnEKk6nvTHp7FI+7UU9SoWYKiSOp0FdDFiDkDVIqU2wGityt2bPCOp16zO273EKNaaMz9bXWva3dJusJNGkVGwvyOq0ynylGOhMc/pSDwf7eld2F5S21DrxkRuvGK3Y3S9EfyASqr84e7a19KPt4GMg5eWObvie0CWf2Ks5LR3ya23dh7S/u8gyOG5vm01c8EKC3GMTTupycC7OTo3pjV431pbfXuVsK0kN3dwg9HQi0JXjd4wCWOdE9rcLj5CQIZvTyjtCZkkg5vri93oebO1xva4CRjqlNCuJeTN42J08Atq81pNxvaiCsTfYCGJlqkb4s2sPTL/uRUSOzcCVW8aCR6pkQ3EdskYsupfBvO4tFs0tATlThsGfmLbyALKPgkM7jlBIUdsKrVwhkKYUrUkpeLl3Rog3k4wnBHcbbkNaSUyWudaZbI+YXO8IczlOXkML2PW6OZ6WEquTxEoJ+xXFTfRNnPghp8aahTmd5530lvmMInByoR2wDl12475SpXwZGqeTKExWZZDUNKj0aEfG1r7l0P2gHkZGTIQ+zIhb1XBU7nBIbCV3Z6C3EtewFWas9slVgjTM5Dm6onVWRW7ni6Prok+Vw75elWh8PjOCXUDhveQ6Q6LPhuitCK/N1BOVE4c9LdqK69vceWPOEwqaXK8riVcmxaaBAzRspqTQ0caNVmtDcNWxE9hMa7NrOu4iswz5wvD2rNAM8ka+ifBpjGnD3Zn1td83qV6tjy2HtBaTjoogicdkqeXEvmVoq8NP1F2u0WByOEHkIRlHuNNSS1L9du7cwTIlZO/sY4c/DeMeWXXJSsXdyGEpC/S4s+pwdFjDHFWIXVlQYpPszwh+ykgBNHCWnZBgONvn5aW63MdLQrBKpwfksHN6EbLU9dbaRUgiirqIJ3Sc2ladTRCstpkjiZXsEm2oHeNbBFORzkLnmjR0jIuUKj0UxqGGq+NycAVVuUs7WhUwZKoCNtgUjUBR985DUYxYVfnAaJzQO1V7a+StzgQdbAjTmd2dmA4Pjud2vVmOgwtxonZdWSVeyZfLgWCD81l0wTn7oAqjs6biLEuUwNPofXGmTAzfs3reEmp+s2ILDFeHIuLg2qjRVi4Jaukw14aOrxRHXVE2z9KLl/NCzNpdmVonMGl3zlClScNhZ1O5lSTLUBcRTDZ0RMJGe/Yu60lLteB2zs6HYhfhSw3ecgbUjhHla8NKDg+4h69DvfF2FJ1VucxM+rVCnZAQ0z23CeQxQFbqhvUHzAKTZohfEy/rBaKTujuzV1Czw5cIXJzvl2qpDsuVvW/iPUVMp9BKuV4JrlnMwywUyqsKVgIw/25E7URBhFbtMo1peDtLaim/MrZ5hXtzCyrczeFDG17DLpR9xN2l+Ko7M2Ph3OmOqVUBpXj+jGXFPab0yIgceZe7IYAAjUo9wWYBLAB6iTWGkDscSSgAg3AlHQtU7y42zBUxPVyOjrjKdFEXhKtVas2Z4xrvGk5cN6mXXdZeyLYvVP5yuCIGc4K1kvaK061uTOwObbrLfQ8nhscx+4qm2QwBrC3yIWzvvJN57Ghq57lpy/iT2+CevGUJgKW3+Lq8MUfo6lr1Fbv0O3BoCOXy2vUwwQyieTfjnQUmE3lox3Sdr72602wFlSUPhbXmYAQXxDJhu04ut83ltg+GSjzu9HjJMu6O9pRN1E8omu09LqfX7F69TNrZwuDDpiTWJ93KD+q63TbuKd5PFFbtysgW8dXg5Ii1ZJCxN7TBXFJgjg1xPr1ohW5IERK5e+JgVHZ+y8q49Qiq3yXEBhSGu8J2HJcgl2snaxvPQwOUONEZqSWQVqX1pnd0UIpn9HLd1Cu30d2W2QkaQRE6OCny24AsT3bqH1j1cLC789VeIq6hnZVeTfgrt+XjAjO1S3TZM5IF0UkSdbu9Riix3HCWl7VuKRB3MON0su1nsXS6JUnPx5e9NjXrbZwIsZqNZ8MqmdxTGVeEx4Ozy/HBcSSX7rYDdpJOhxWK0qejYrEJAmazrOa9buxbjU8H4oYdO8j0OFm/VGq8d7LyOoLjrpGbpkRPuDcaGwTu2+lao7XoGafbiWQtV9STK9J3unddbnNpxVYwfYnzSiWouqTF2DlmkUXOB6sCSjejxcXTjnWZ6LQuS0MgixFMgh3mb7vpZmlhtvNaKmP7k3DeGWoKowjdOCQz+npuc1Gg7O8SbayNFsnN+1DY9IrRWkMqhTuej7GOnZZceLWniTYtvBKGNIDN4yohG/NCFvGtJiC4X/reCboWsSQtD9FkZYIlBfL6cs5rO18enDHU8cFGy/3ajVbHEDIPltWk5B7R6fhk1Bf9ch3MoQtuUhlcbpOGwt7Yb/RKNEuTzdBxdRNYAb0rqAgd16dKbiDpzNK2sdyuj+TRvhaGAyvJ7aYvxYmpCyVlqsO6g+B9CzeKN4LqAeQiemep87X86uSKtCWSM1ZDp0nTsT5TmKqgqnpLrI72tJcY7lgNvR6wAr+Nz5aRozRNO/fetZvcnuT9bq3KV7GnaDK9YIzA+A04BsrswTwzCMdPamHej5qKRZbMYg45+HU3LVV5MCmK9bErfNHNcjz4vK/UGusvI+cKIESBLYTym02SKqfqltyVHNAnWfUMTq8xkOxta2RE4/hkeLZKEoeDzF2ag4f6veJIp7C4ottVgHrsKdwasWQ2ls37dmxnaxw2MV/Z7dpt3Yddvrr194O1swU/WSEItq0DyudMquPWKH4LdR5n7oZnOBvN2YpDutdyzIpwpBDN7HRk15h1KRFZuJ8jAh0NtFvWaRq02L7cHmFecYptwGP4BtkumUFvOfF2Kbk1t7t1d36jMmCaxaiJVpFhGjYX33DTJZL57HaV8SrkQbLjesPlYPrlpGC+HWzwkDN9+OSRd35ovKS37naB9ROrrcq4IrZhkkdo2pzYO5ZGQnuDlsdbSIrHaS9jO2t5N6FVEqrliDqegSTTsj81MJqe48MUXBjimshbLO8Bi6fpwMWhy5T0cdhtTDB7XRoZo3L6KrqaWjurdMmlGT2eu6NAtjqE37kwRRo1s41QYRG1bZCz3a2OyoC4SXsxGnQdpjeZ88CwmdwlIoaVcHPGXTBSwbEPSd2qsuQdt1F3ELbDcZwgr/Wu3GbmAaOosnTPthzxBKpoY9If8uMGIA+E1wrpoITT4AxWmOZWbeXgqDpoeiJLdZnlxtQumy3RHo7kvT63lphFXJ1F3vEGgaOdX9rkCR51nW4dHNkavBq117slo52vTPCNrS7XEdGv3vEkpAFmZQG2QXlzGQk6Kd+os4Ldesk7heOx3HNL0QFtmOuBWWrMIKi4E8IWX5tCtaNSJC349bRadQ11XSpusTuSuwzXoygda+5Oe86KEbAkIR2hVZXlTrByzxiIeCXcaWxqb6zCpBahr4ilwY4rMlRS4nZDqKuh7TIwlQX9+YJFGmsCTDQOiHVU7Cisgq3q+3pxXBYnRK/boe2xML4TcM6paE6GvhH0rAqDs7+xSuvJq1aOVNjboOp4eEobB5a3J97eynsS3ZUaFqjOdp3W1bTU8IMBWfSe0z3dMcvTthejW5CebwyeNAOUMIiMbfMyGG67oxyj0t1Aj6uBIcd1aRQpdMmVo8OPt8OhCLSlA6k8bKwqL46rbRNPyj3vBbOBWjmUrxTP7U6b4LBegQPwIIlbCA0vu/3BSaSUDChFvWc64rVtHm883VDNXrQ2g3TGEBwfSOtQE0E/kljtkLCkN6FyxfFlYo0Qugy2utR7AaYd9sU2v3tU7wdQo9uGWI2pfyKCbSUOdu+6mJmDqsb8QMMs5HbSEaFv1koN+jsfCRO/a6aboJK3zwDYuJRwo3XB9KC+FLZA4pVNDgLre45NwrutiaFb9nAU4lBQkIBMl/sK74j9OIVrpuJ1zakZm0V2VwAb/v3QH06xYJ9JpF2uN5xnQNtpPVCNc4Hv27VTVQmhtVQM81aJ9QbTmisRTuKKXIc0GF/XXGKKbeqB0/cK2ep90eG0uMKzIwmwbSC43dIoUFhFuwu/6oelgWZ27g+1MxrnJXIheNOgligHWt1vCNB9owomyTq6ZP6ALK/brcOh8hFec/5aw2392IzgyI/flaXcXTEZpDunJ7+zMe8KwakLT2yOzfxckWNDazd3fUVrUwKAsd6jd9tAzjV0t0fNiNwGk+VRhdy8tQuETi8HO733xhhZmNLeXc+pXShX9nbZbI36XLipsYba1BxVgbUzL3bJA3FohdutEnEFviTTceOc9lUV6OPejI87M9EROimOMT0Zo+9cYgacb/ptKduxnx6nfmf4LnZR8OaG+NxSVxyD3S0b8w4JnRmvJ2Ik5qKCahIMJJ2uZpc8YTV6k7FlxCGWkJ6UXQ8FEHlbM/ZowjE6wkRIORd5DQ581RZFVz1yzk89hq7zEAA4G1UR6ZkbU/ItIndzQi2dENQe1+NcjReI6OcKeWRY7cAiWarEJHFZ36YcNQ/uhSe4deQVV8w4GjlBbNpmQ0tkqhljLCSxvC5GuDy3w4bQ1seyZ4wRPZ5CXxQUzYhHQaSV1ufg7X06dijlMbGxks0Y1Vy/PBTsKhcUlXRJnz/FODRiWwkE5hZE25Xss6rLbo3jqlcYPIbBsLHfL0s32S83cLj0KxPTUWk4B5ULAYRwiPCYbf3lMlZvkBEdOmy3rcwjXWHEKA8AUNSOcCUpFa9pfy06NzaWBgn7R58tGHeE0pJsRAQpOqPloHjZSqHVbMbOPPRNy5YFH4hQXWw7chexVgNB0ImTPTIw1IA82G4j+LHZn4+G2ZsjEa1W5+VBm8SMo6/8bX3gVmeXunArJ+uj26ib/rYeXFTqC4d0SJ6hKyI127SUi8jNWCfCFXYJhkUxEcZijaynEWNVysWWYzEQQ48RPoRKG4c9Wdh4vxPpWQrwPDhPNcZJtSNiZg/a0tXK+zHme0/r+b6KaxumXTaCzRgzD1Ao3W6wTwo1RXi0U97QvXArkrOmWty5KMluXaQKuprSI3zVDufmKLm9EhPkljipsSusThFFvc1PT7890Xv77/84bX7M8//sadPzwdC3n5g8nlUGjv/5oevzv2HTXz++gbkGWPR8ptbmffR6APV3T9Q+/cvHkPP26fmLr28Pup/Pzjsnmn8L/ZaUft92zfS1rfLHT0zADrdv519PtrOJHnj/4+PW7xqfz1mTqPzaVV+boEua4G3+ceP805HAT5zu29fo9YwRrH/9DOorhq+/Bk09O/r6jQLwD3uH37G3v/0fWm/sNdIuAAA= -->
