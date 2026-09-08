---
name: "rar-cowork-cookbook-dashboard-define-organizational-structure"
description: "Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_organizational_structure", "rar_sha256": "a5a04270fe04cf8c595ed761137bbc26e2ce3d8ec70464ef57fab831ff929f2b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_organizational_structure_agent.py` and in the RCI capsule.

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

Define organizational structure Interactive HTML Dashboard — Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-organizational-structure
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-organizational-structure-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 a5a04270fe04cf8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_organizational_structure_agent.py` first:

```bash
python3 dashboard_define_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_organizational_structure_agent.py   # or on stdin
python3 dashboard_define_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define organizational structure Interactive HTML Dashboard — Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_organizational_structure',
    "version": '3.0.3',
    "display_name": 'Define organizational structure Interactive HTML Dashboard',
    "description": 'Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c418468dcf1159c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-organizational-structure'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-organizational-structure-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define organizational structure with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define organizational structure data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-organizational-structure-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define organizational structure.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls organizational structure data from Dynamics 365 F&SCM for a given legal entity and fiscal period (read-only) and saves a standalone interactive HTML dashboard with totals, inline SVG charts, a sortable detail table', 'example_request': 'Build an org structure dashboard from D365 for USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-organizational-structure-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of D365 organizational structure data for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineOrganizationalStructure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineOrganizationalStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-organizational-structure-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDefineOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1HfF9G2nzKvmIesqIhGCAkQMxpxOtLMIOYZ5PZ/74N0b9rpynpd9aI/tewMSXDOnvda+1z024vdtVFRv3x6MX07X+zsNI0jv17Yubdgi6GoE/BWJA74t3CLvK1jp2uLunn58OL5jVvHZRsXOdiudWnaLIo6tPP4bs8X7XTRtHXntl3tLzy7tRdBXWSLzZTbWew2C5TAF9v/abLyIiiAwkUY936+SP0QbPTzNm6nhxVB3LjgSunXceEtfqx92/tY5On00+NuY/d+AzY3Lfhmp0XuL+K89WvbbYG4BX+QJaC7iZzCrr3FELfRoi1aO20+gHVpDJabp93Cjey6BZeAnKJubScFBvutHaeLxxfgrD/aWZn6zcunn3/58BKDzy+ffntxU7sBl1427xo2fgBkqt9EwXwPAhCT2nkI1pcTCHoOvgOvgPMZuOT5weLt24+NnwYfFv/5n8lg12Hz06fP+eLt9fll/s/o8kUb+cATu2l9b+Hape3EKYjY64JJB3tqFrUPNObPyNRxHr4+d/4hqSgXf5/v/fhU8hr67Y+fXwpgwsPszy8/gWQCfXU3f36dpZQ//vSaFoNf//jTH3Kazrn5bjsLA1a/fnn7/iYWLPxjaRwsvpgax77pqn03Ln0g/E/+za+n6W/i3kLy5bn4x6L8sPi+5NmfvwN7n1XpALnfFwtiAHa+vN6KOP/xTUddgMqzc9f/8ad/JtaNfDdJ46b9l+T+/BQcgVoF0XoLyU8fHun7ZbF88+2rzH+utgQF8+94Apa/q/saqH8m+5HZv4ieO6L5msvvivvehuXfFz//U9/+qw0fFsHnl42fgl6t5077tPjtUSI//+D9cfGHX34Hov+vYsyiq92HhC8ZaL/Ab9ovX37+oXlc/uGXn3/oSlDFvp196er0ezK/F9eHnm8i+Lbqx2/3Av3HPMmLIV987aHFb0X5P+rfXxcnO429P643nxZ/7sT5tVzMTrwrfYbgT93YAFv/FMefXn4HGJQ/0XW+DfDjP/5jIcduXTRF0C5Mt+jaBUhwG2f+bPwhipsF+H9GjdoHcW3iGeSe60D9zxmeLS6Cxa//y33g/kf3DfdXX/Hzi/eAty/fovyXryj/6+viABQUdRzGM/wbjKZ9zu0QoPmsvKz9xq97AFjO1PofQV9/nD8AIF78+i/r+PIQ91pOvz7wP34iocEKMwo2Xeq/zv6eI0AlT+9cQGv+6Lsd0JQWM5UEMQDyDyAOTZECjmjn2DRJnKYLLwY4A+jtyTwgfp9mYb/++qsDzPucP2EbXTx5r1mBBV/NWXz8CPwL0jiM2s+570bF4offfv9h8b8X/9Wuh/BZhwaI5C07wELRVJUF6LYuA8tA4kCqAZQ8svPb729RBmJyQNQgl3EQ+8/NoFoT33sPuckzHxGcWDg+CDUIc1YCcgNcsIjb14UQLL7aC5TOt2a2iIqmBdxX+rnn5+4EpNrAna+RzIsWUG4bN8H0YdE1/kPrr05tP0zMQNvb7a8LmdUANxWAPYvZzMcisLnIYxD+rwXxvA6E1D80i/W7iNeFMtfnorRru4xq+01HYD/zMk8Kb9uBcHuR+8PnfKZjfw7Vo1qe4QGLQGTct5R+nHMOBpgMIIPXvOt+rLFnBj08mLT+nDdvjWDXcypcQAxAadjF3kwPf3srqSYqutR7xA9YOkt6y4L3lpVHDT5ngX8+Egl/nVO+ThGLzx0Cwdji/+eZao4Qs9sZ3I45cJsFpxyM6zNz85g5Z/g5mc4mz748uvSPQecdzN4x/TNQDMqwnv72XPnI99uarxHzACIZD/mg2EDmZrmPXphru67nLrI/5+/kMZv+QEpQDgA4QGPN9fyucL77bmkEgjF//2OQeNQOCA4IIKj3Rdk5KajFwPc9x3YTYNUc8vc053OEQW8PUexG33g15wzUH5C/AEbEoEMBwbx+BfTn3XfTv9n4nJfmLY9ZsgPtXD8EADv82cA50XPqgHntc6oHfn56CAFuZGU7++6AogOePi/6tV91cRO3M3g+4+qXAME/zu9PT+er/liCHgLBAp1SdiC6j96aYScD0xCwYS4Dv87iHEwHIChvQXgItLMZKAAQv42vT4mPy28O+Y+GnGntfePsyLznUWGPbrDz6c94cvhemQB52bziofevlfZV2yx7xtQG4CLQ+H73OVK8PqeC59ixeJf76R+OTT/+eyerB88fvy2AT4uobcvm02r15OZ3an4FiLZ62tr8QdMfnxT68Vvg+Pi1Db5R8PT90+LfM/IbEW9N8mkBv0Kv0HxLeiuytxeICftxff2IzXc/54b/B/AC9UUGLJwzOIG54CtLvi8BVBnWAL/A4idrNjPZDoDfHzQB0vE5/3PVz10HoCcP5yptij+hwWNcAB3wzN5XNgO38hbo9uZxM/Rf51PabH7jv3zKAQB/eAHY6v87h7yZurK5xpv5jAi6CeBsG/uPbw/IGNv547fnZ7V8CnpdbB4o2fy5Dt8IZybcP7XL01vgpQs0fJjpwJ/ZYvZ2Vj63mt2A2gVlO3vVTuXsxvM8OE+QTxb48mSBf7Ro+w1JzFT+mBIAEv0NtHBgdykIZls8TMnmsQHY88DtHpg/d+N3lT646MuTi/5R52YmsG/oCigoQRYenf1h4b+Gr4ujKW+/K/vrvPyPgs9gMJllecWnmaM/vIEceAdnnA+Lr8cVEMa3A+Sswc87cDb/eT4qzXl9bJk/gD3g7eumr38McfyXX75n1wMJv8xV+Kylv1qnzAgHGGAO5YNeHwULzB0AKvlvbv/L/f0RgRDiI4R/RLDXqM3S78fqzaYiBczwneQ/rs99Vvt/MWuelsGE4L2ZtSnc55i6egLG6il59R2tQO2DQwATz1H9I11/BK14HDZnA0GQ2+ffRn57Ad1kz9POWz+9nVbAcgC5H5t5JlsB7AEKwfcnSoB7//1zzJugJrLB+Awk2bgNYQgJBT6EuQHl4jTueyQBwyjpOC5C+Ijrox7luySEEZgf4GRgOxQKBwGN0AHiAHlP0PkyT6DxbBxOkwFE00iAwQjkAXsQzPMogiJcnEQgm3Zs3MFp+09bkzj33jx+ejiH8+uRao7Mm+O/vTgEBlbyWCMwzxe7omHHR1bOJF1WF5yOpbB1TRvyzcBen+oMR2RDhULWGYX4fp5GN7R5IXF1ePR5NeGt4wAxK2NDRxqUrnBq0oU437u15Gk3a7gKmatetEzjV/ldud17hSgvsl1uuaoPb4eliW/4fQiZ14voRXwWlZf4hKcCfzXwwAx4niaWq63tr88mfSxYbaTJ1fJgDSfzLKh3jGC19VqqD07sic0uu4cQVnR9Pwr9qg8oXDpd9zHENrqUnlhjiq7JdPcVao8JENf014iPTdNAapOZoM1+P5ql1ibK0sa4wj5srngfnsUhJGOlUozRj+B8T2/rXghlU5VN5LbBaWCbyhHQJvHDK2n6zloYpI0c3kNjtb9c/FU94U6fS/hyGaBYldc0vloSfHyJV2ksHs9srRinTWITZ/HqlWJfEAoryM1Z1kXNVVFeUKWNstcH276MTOMRKnxTUca63jm0XIsXUcHowA0ShmSL7Dy5B8qsecGEb1ku9TqU9JaeiaTdl5ur3h2joy/kVmdX54J00xxphLDG83PCH3Wj3BfncyGsQ6HGgnw096JO7o5yWnCYecKELLv7qWrW22pPoEe3jnpSOKGl5HHnK7tRKb8h8sAgSCRF6RQVXUS2TwV2Nw0laaJJFAokwbs01A2xLre4eWZXgjtCPVvvy50nMyu8aUoI6q+7/FrkUNEGUxlziGvelYkqD5YvcR6ErHzhhhz5u2zhEWvu+30TbjdBRW0S1ynMbGLiILnBx2wVK7JzS/hAGwVBUdZYwh5i/pZKhwoniPoYDu36FJqakGDlatfcs5HQg/J0ux+ObHJF0vAADitbewcXoDOstmor0RQUjISga4UM5z4/V9ye52rhgpXDKi6l6iBOhU0ce+rYelK/DjYyniZCdcFY2tdXa645INxduG5rUrfCzkIPV1QbN7Um31XnkKj+TirxBF63ZWkZMgFTzjiOwTpBBcrE5D4hAqfvsyCEtl1zzDcreZQ1MaSSTa/l5511Iddo5t7EFS1rmCmhfY9zNTsNwsTGU6tkrLqV3FNMQENxJe4od5eECzGcs5zbM/edAd3YgyS0KLPvGzMui5OLuhehM0QPMg5WeZLR3D60CZlaZSPq0MlJBl+8ZOdNyS4Vod4rysZRSTzo8raPl34sNr7jCnfMqM9Yg3AlJje7u0wel/frjs5RVtJNBzTnmTkr5oC2rSo6dRApdRCfTn2lJqWcc0HDcj0SB2tyKyYdW5+WHa2lYrkXito9eHa9ytqt2CFWQZKBc9hIhJsPbh3SyWV1iBW2iTJi7E6udGtukLE6Grfhik1atc5j5Y7cGUtfGocej1cYAbeSll4pZotrnWFRaG9tjQ3f9D1BQ0dlr+bKmmYV5KJ2vcYfm2islke03YNjoFylOVUxTaUEES6ht4gdK0ugbN0d9lvXXGoSLdSIUq1kAdeE7S4TAk7S+vNKoPe+NMhmRB8DbRMgirrvTZQzKHeT6zdkj117bL0sPI1Ipk23Qrn1nqbvG0zZoBdOqTZb2z6fm9Wxc3fsljJu3W5LsMrGaGyT2KtCUkjHK3HprgecvDTUbuP7NQeHZlVgWkpe3JtBlpBHUr6xPR02yaonMai8ONtUHamIFe+H4Qam/Bw+7Mc7QFVbxOmBbPOTqUorUtzbxj0/1QmWjjpPGcIAR/OfV0Lsjhqx6I0pQjQqLqdof5Ag/XZriuV1JZMZEYnUcMLVQ2Pe+UE/c7q6gXbru75mtsNGcPWsZEbMjo7cqbH3dNBb9NVUYz1lJmaoJmbZOFFx4hwm4hv5OOXRJalwyURruTW4lpML4TYJTnaEhNNGXK9LrLXojdqqBXSwtwYLiRd7dSoPBpWtnc7TOB0fCkNXUxpp9xeEh68Nv1eKiNqPAVbGrnLFw46rz1curuyg7ytcyxxq6R79+iBvNVvcaQp+EtIdn4/Hyqubox8ORlJAECpROOdvlrznNJiSeexus7zVFNXxfb+6EzS8wwLtNlT3JXevSFfcU3v4cL9fKewcqcwOOQlHZuP2CQcloxdh3fW+EZJtk6sQjzNGVXX3wxp275TuWGxGIcYVG8c4UO2lPvk7Wh6IOtSOzsCn2gAOT2u3MPvt3Mj4yKrnnVuRvMQGmi3IBcmf1Yyz1npRi6OYns+mJmpT6DjEgUdzR7Enx6HkfAVZBHTEPTJHsJGqRUfYF4EWAjafsmH0AqpgMmEX3tSL7KxBOPSDnnoVtHQpUav0+1VCg4tDDGGVpGq+PViUHtbSFPlrWlpf8G1uXcuOPg8+LKAcF4sVvjQL0sgEZY/SJTcpzSYP+2no1wVv3u9QbqyG6SiAqlErSR8v55PHhyzHdOp+S3LI8hBz/SnjV0TKNEe5sIqD3XCTGQ+SwToMUlrrBJenzFyNbo3JoIWGvqDCSuxkXrjISqFqoz2tQ+pYJLq129mQq8EVoQ+OgDEHfXnHmuKUifa12pcqQxn3cR04W76Ku1vdHgvsKG/55sreRn4nJ1rVVVtSEFhfbom1cJdLxJ8cdyeIK3nCt/rywLZuH6TOcHVJRLXtyMbDgTJhrI0Hk3fyjuaLm+rviZbJ0NMRzAZCiyeMcIt3B5gwE5qgMrlIDMuviEjA192phxmhbZawkeZcuh9iL1Kykzmxvt4Hxuq8P2bb0EY6ds2qo25jcTjW3dgKq91tH3F2WBNKsJxQIV6XetCYaa3tzj6iHUFCxAvopOWys0zD60fa0rek0kdIhpNCie3TMYkTtquJvdyGU0luAvtulROb5PSS7u/JUGsb4OltL6VJvtku7QFK4BuOSufbcdeemdr2oqS5mZlurO18ZPJROZaiaCH12jf2BttwNs3gpUknzhVnXRov9vv2QoShfpcS9Twp6XTEbNDCOx++b9C6ys5swu276m4WirVZD9jaF852BEgByhLTTfHBvPlBfy9MZaeEhGqiPFS7581+465NLztlqNqe/KoO9wODHc3z1mINM1d4PIxaxtcQP7N1abdeEk6zGmn1dIqaSVl7aAnbxIan9d0qKHvxGNI2N0ye60bJoYwDnNkbBtQ2Lez7BLFdaTv9QhxEC2anRNzvI0tjObMUjzGH6RA4UWLhFsFO67y4qsoUcyjUiggKUI7g0G1FnVW6HWT5ZK8Lnamqc7JEhJBDWIo3YqH0zcNxdPS7au2jfGtFko6KUZ/BLUH3dhpZFGRGCHeSRc3kw0rTx/HaMIQs6Vekt8XKPXXOFl/7uFAl09lG4stdCKsMtm8NY4sb5kiOZGYkonYy+BFd9dV2a1oSYnrpUQwjJqMKomFRe5t0lZMNTLmtN4aCrFXC62Rf4293wu/vYQUqT5qCOhBl6JSeRHFzlsIbbbi2l9oIj0nehU5OPZaIsLznuouTTODkdyZba7tbu1R2VC7BCdqalGSvysNUMDJ02F2ZS4Nhd8wv1vrlSh0KhtjbkTsGextfyx5hl8NJZALrFOkeJWXW0FrTpi6kU3ip5O2BzBW7N1OOoeRpXzUbFCEHdBkN1rlItx0u1+oESnbPW8HSugaKUIj3/rLGt+jF34lcnOyq/oSHx9rpGYS/qtR1Z9AYHk7OsZdY597dZESFXQyuXMrYevpQk37tZY63QgaNaJum2ue3osmaXYIMVk/XYnhdx6k9WmXXtdThyq/zfdiKpkmqWXeTepdwXX63nBIjbGTRS9Z5GFJZB6PQZZNwzI2uMkjfnyQs3iFRGdqbkIIRZjOCAxWl6NZWv2O8eTKjETZO0JBLJjGY3NHYIetDTmmjp/HsCAhUUvJSN1i2MalkdckIPIOWJBZWFxtBkKH2rQMYVm2kxayNx0xS20QVW58ryJxcKD722PnGiPTOL71m17ncZV0tWSOa9BUyIfohcNahajDlNbFVT2bvaJKpwsFocRzvTqSDU6wWRxzUTOzuKrGck+HWnSjRdC+fO4HTponHT6d80wNKpAIOE9AQnAbWOnldUZYHjrzhUK50gxfS9nZSWqj0o5IGZE7sb85R0AZp6RVGMGU3WUf2K+aYi8XmJhR7y8KOVkCf+0sqyyA3RLcsRhpdwdrZ3pMrdjS04ihVp9PO7nh+XZFONsEXmezSlSWqxGE4ueckUjf85RZOa0rSRslWrpfNbtuELXah7JiNDX1Q967Cu0Lfa/rhnroJzMDOxe+HzT6VJyg8HXK6pwA+eDfz2sVOnBACc9uXimZVO1oth4hptMMSMIDcWV4XcoGgVMQmZdp+vA3IIWthx9b9I8lOYjpYQnbYi7lAXWgxGW9tLXrX4/2kpCVc6FdG3cYn/0r2DKWTN2vTLMm9LBkk7F4hDhmX6y1zxzxapS9WUhlw191ZTTpjYELXqZThB/LqVI1M+NQdbaudScHCLYThy1AfbU2mNoLXY7vtsWVQN5FyK+cJNIMwU9NuLbmrj75RwyvIoYJohfpFQO4OtkYeDSI8JZ2cVbRT4itYpysJb1rcRxxwrJPhJrA77bqqTafyr+s6N+gTad8kHZzH48Olu62MHRcQF5UMtlZv1l487VaeeLKVxGjW2JluYARbJQAbz1oKcJ+UaeU4DuJJInbSsqQEq1DCcmdB8E2ycz8O43UlVjXFVE7dhTHqQpl07yxElCIH3ffGysArMiR3U6wtUyiFScJrVDDG89DIBVrq7Z1DWzm+00pteNxtsOshqow7ODJbMWPT6f0CYrlaTu3yuJXT3SXTAZME1EmVkIlsuy0J4ZdzeCKu537K8YtctLQu7PKok+KmvN25MCDXHBfAosXzVbu6ndGTwRKFY67FA7kGJx1hE+eEr+CD3tfyutF2LR+VFkUip93Ue3SG9p6zMZL9VNqkky5Vaoym/HyW5L7b6oQGBbqcKeBAh1I9T6XhkJjw2l05q8slD8rUkjGZontM1ynScdSE6bNoMpXTWOmYkGEZ74koelEctzczamVjlRgdcEIwk4BMKg3GSFPviXFJbq6Zfryium7rGy42AGFg9cFrJopQaywTw0w52CPKFuFestyzf/Zz275kSwnWyTo11wXt147rq+Bsyte9QEqqaoTW6ooclF7KsVwqbZ/bBFfO7MQ4Ufhri5Gyhsib7Hpbb686sb5taFVyYieMXLUvxt72ma3Cq9mWUy9sNqzDa3GEqHoHXdXlTrLTqxmR9p2/h+Qg30x1Uq4EYP/lRRsxeXczcE0ceSJspb0QnnPcYI81PV2vYFr0xn3d4SzHZ6SBZZKnREHWq7BpaW0XQhiyokRi53Ekf0Ly1j3iijd6sZThrLj0BzwTkXLjBzCGTF01QWt0DbOaUl0TA42QeOkQBF0mY7frNcI7rffc2Rtgow7rpg9Rh0lr6cqSA22fR/WCNnnn3sygkaHq5sPq1LAujBcIsoaOJ0OpLMhTUtAAiAX3CnERrjYY/5o+IvZiRCgXaXOTe2ZkT0p+gP2T48jmxKx4fipA5vTjKVHVwXMtgz468F5Y5QaAASQy+isDjaRHJ9KOXjpwPVUq0YExgw7QQ9b3glCfeyvKl7TmXLQOOiNpJiaofw/i5ZllzoABRi081xsYD9x7WNs5SsTVReXxLdJCyy1tWqIwigbqH5Qb0uFgZtnafkGsgyrO5H3NbLX0skXbc49Wh661b3R84tnWKxkPItNqHHOk4i28v1y8FcuqezCwBHxlSuNWyGwwmSq2UW7qjX/rbynAiZNmHTS/97cwT+FLjhWRtWMYiFkT1wKqx6BZLzn6esqrEytrGHM8dzV1vrKRXuAQhknyzSZ6E0bToucMnufC1SE526PbaHGDouYRDD9XutJPkmOrkwoL7fUureyKjKUE7Ul75zEq1N7FBEvCuIx13kKvTEBUHjIqN9rbGXxnNE3KYxnZUJ2V+DfH1O4mhJbDMXcQC91rLY8oXIy3sM11d1nbU2cHIcu2uk5jL2lmWSCn1iWCI+Efo4YjaHQjJxcYd3a2ol/Oh51OkNvwuqPJUs5QvlI92hUvMl3c7FMctXRzaFAj2x4TKl0vt/2mT9CwGpYMmhCjquwDEWP254gww96Tw8QTb2etYs0d2trblPU5q+c1obIQAZ5U7Uzn+KnrsB6GNQ8yreOStGvkSAykV/luTAcXmVF6XJqqsbmuIT0zT2eGFslMl5fX80lXCRnr+2VKTy7RV8yqqmTydvBDt+Uw3Ls5Xo6UcJc7qNu0vR1kUMJZmkQ0adYFmIfg5QbQH+bFF5rfUpMZ9fHd2Rl2tzOyycjvhkdgCDat4L7tKJoVEO2+tuq816myvFx9LF+ysHgNtYO+46YrodQXO8ZLCoYRQ3OJnJG7JGAFKXBvEJOc1aXOqnWO867EMKS329wDEe7Q7K6Q8eYgLLexeMNwO2DgPK1VBEGPO5pTw4LG44ovjvloHW/EfaCmuuqwpO89zRvtkwefspVzibgAgyXO9ajlpUXPtsiuaJvJwBFZjVxqtwl67r7xcG5HtknTH0GLVpUNd1veWiG3guybMLY1z11FFrfsjxWc5JQChw6JO52HYG3vNTJ1l8YLrQx0Hcl6wAV972jGLbvdtPu96zVvHXRqG9tUteSWp4LjzWCwz5YYhqLerfZlbjpXtrixR/jIHQwRPtguT09kRfS7jtEbS2UwUrBWUsHBzLlQ4z5oclyXw6YkPJVKvCE5kbRUOA0FCe2yDzxzdQ7B5Ee5EI3BNtqJWobZxrQmzhvlROaXvERL904a0g3PDbMSKttizhAOi6sevl/QiVwBINiVxpJkztZ9mUQ1USTorvIpsgy2QcSQnQ+gXGWzjQFmOW7ZIQONrRg+LSQrPeoDw7zMT1nfn/q9/Ps/cpsf//w/ewr1fGD0/hOVx3NN3/Y+PXR9+m/Y9suHl9qNgWXPZ29N2oVvD6j+8uTt47/86HIWMz1/Sfb+oPz5DL61w/m31y9x7nVg9fSlKdLHT1bADqdr5l9pNvMPeV3w/udHtV81g89RDKxviy+138YPVY9fNWW+F9vt+9fw7Ykk2Pn2m6ovKIF/8etydvftlw7AS/QVekVffv8/DFEVJkAvAAA= -->
