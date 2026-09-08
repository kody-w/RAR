---
name: "rar-cowork-cookbook-dashboard-create-background-job-schedule"
description: "Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_background_job_schedule", "rar_sha256": "f6b4194e716d4ea8bd3c159bdd5c8c3bdb5e733068964d7e9780f3af4300db52", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_background_job_schedule`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_background_job_schedule_agent.py` and in the RCI capsule.

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

Create background job schedule Interactive HTML Dashboard — Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule
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
      "description": "Name of the HTML file to produce, e.g. dashboard-create-background-job-schedule-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_background_job_schedule_agent.py` and embedded as the fenced Python below (sha256 f6b4194e716d4ea8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_background_job_schedule_agent.py` first:

```bash
python3 dashboard_create_background_job_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_background_job_schedule_agent.py   # or on stdin
python3 dashboard_create_background_job_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create background job schedule Interactive HTML Dashboard — Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_background_job_schedule',
    "version": '3.0.3',
    "display_name": 'Create background job schedule Interactive HTML Dashboard',
    "description": 'Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)',
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
        "upstream_slug": 'dashboard-create-background-job-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ee9bab24f68b137',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/create-background-job-schedule'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-create-background-job-schedule', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-create-background-job-schedule-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of create background job schedule with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull create background job schedule data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-create-background-job-schedule-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing create background job schedule.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)', 'example_request': 'Build an HTML dashboard of create background job schedule data for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-create-background-job-schedule-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 create background job schedule data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCreateBackgroundJobSchedule(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateBackgroundJobSchedule'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-create-background-job-schedule-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardCreateBackgroundJobSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaWLLmX2HeiZiqutivJLSBb3TECAntGxIIULnDpX1f0AKSavq/zxFgu6rbfad7Yj4NVTZIOif3fDLTR7+/OX0XV83bpzczcMoF5+R5EgfNwin9BV3dqyYDX1Xmgj8Lryq7JnH7rmratw9vftB6TVJ3SVWC7Xqf5+3CawKnCxau42VRU/WASFq5i9aLA7/Pg4XvdM4ibKpiwYylUyReu0AJfMH+D5NWFmEF2C7yIHLyRVB2STc+pAiT1gN36qBJKv9x594kXdCCtW0HLp28KoNFUnZB43hdcgsW/EGRAas2diun8Rc/d1XnANniwPGD5gNYmidgh2lxCy92mq79sGirpnNcIODj7w8Lg+LAMj/xHKDrL0DXYHCKOg/at0+//vXDWwJ+v336/c3LnRbcemO+8qIf6m+/aS9WrvnSHRDJnTICq+sRWLwE10AloHMBbvlBuHhd/dwGefhh8R//kd2dJmp/+fS5XLw+n9/m/4y+XHQxELVy2i7wF55TO26SA3O9L6j87oztogm6vimfFmqSMnp/7vxOqaoXf5mf/fxk8h4F3c+f3yoggjO78/PbLwvgjM9vTT//fp+p1D//8p5X96D5+ZfvdNreTQOvm4kBqd+/vK5fZMHC70uTcPHF1Hf0i1cTeEkdAOJ/0G/+PEV/kXuZ5Mtz8c9V/WHxY8qzPn8B8j5D0gV0f0wW2ADsfHtPq6T8+cWjqW5B6ZRe8PMv/4wscKGX5Unb/Ut0f30Sfobbzy+T/PLh4b6/LpYv3b7R/OdsaxAw/44mYPlXdt8M9c9oPzz7d6TntGi/+fKH5H60YfmXxa//VLf/asOHRfj5jQlykLPNnHefFr8/QuTXn/zvN3/6698A6f8jGbPqG+9B4UvhlEkYtN2XL7/+1D5u//TXX3/qaxDFgVN86Zv8RzR/ZNcHnz9Z8LXq5z/vBfyPZVZW93LxLYcWv1f1f2v+9r6wnDzxv99vPy3+mInzZ7mYlfjK9GmCP2RjC2T9gx1/efsbQKASaNN7j8cAP/77f18oiddUbRV2C9Or+m4BHNwlRTALf4iTdgH+n1GjCYBd22TGuuc6EP+zh2eJq3Dx2//0HqD/0XuBPvQNR788sf3Ld2z/ArD9y1ds/+19cQD0qyaJkhLgtUHp+ufSiQCSz7zrJmiD5gbwyh274CNI64/zD4Cyi9/+VRZfHtTe6/G3RxlInjho0MKMgS1Y8D5re4qD8qWbBypaMAReDxjl1VxFwgSA+AdghbbKQaXoZsu0WZLnCz8BKAPQ/ll0gPU+zcR+++03F0j3uXyCNrp4lrwWAgu+ibP4+BGoF+ZJFHefy8CLq8VPv//tp8X/WvxXux7EZx46KCIv3wAJRVNTFyDX+gIsA24DjgZA8vDN7397GRmQKUGNBp5MwiR4bgaxmgX+V4ubPPVxhRMLNwCWBlYualDhQCVYJN37QggX3+QFTOdHc62Iq7Zb+EEdlH5QeiOg6gB1vlmyrLpFCwKyDccPi74NHlx/cxvnIWIBkt7pflsotA4qU5WDv2YxH4vA5qoEtTT/Fg/P+4BI81O72H4l8b5Q5+hc1E7j1HHjvHiEztMvc3vw2g6IO4syuH8u51IczKZ6pMrTPGARsIz3cunH2eegdykALvjtV96PNc5cPw+POtp8LttXGjjN7AoPlAXANOoTfy4O//kKqTau+tx/2A9IOlN6ecF/eeURg/R/3QYJf9+sfGsgFp/7FYxgi/+Pu6nZPhTHGTuOOuyYxU49GJen3+b+cvbvsyWdJZ6VeOTo9ybnK5B9xfPPgD8Iwmb8z+fKh7dfa54Y2TfAOQZlPOiDUAN+m+k+MmGO7KaZc8j5XH4tHB+AMR4oCYIBwAZIqzmavzKcn36VNAZmma+/NxGPyGkelgXRvqh7NweRGAaBP3sRSNXM2fzycjnbGmT2PU68+E9azS4D0QfoL4AQCchPUFzev4H58+lX0f+08dkrzVsefSQImqB5EAByBLOAD58nHcA0p3u280DPTw8iQI2i7mbdXZBOQNPnzaAJrn3SzmHy4WXXoAbw/XH+fmo63w2GGmQQMBbIk7oH1n1k1gw6BQgVIAMAFxBWRVKCzgAY5WWEB0GnmGECwPCrdX1SfNx+KRQ80nEuaV83zorMex6h9kgDpxz/iCaHH4UJoFfMKx58/z7SvnGbac+ICuK8Ahy/Pn22E+/PjuDZciy+0v30D/PSz//eSPWo8cc/B8CnRdx1dfsJgp51+WtZfgd4Bj1lbb+X6I9PwPj4HTA+AsD4+BUw/kT/qfqnxb8n459IvHLk0wJ5h9/h+ZH8irHXB5iE/ri9fMTmp59LI/iOuoB9VYAgmx04gp7gW4n8ugTUyagB6AUWP0tmO1faOyjujxoBvPG5/GPQz0kHAKiMggcC/QEMHr0CSICn876VMvCo7ABvf+40o+B9HtBm8dvg7VMJ4PfDG8DU4F+f7uaqVcwB3s6jIUglgLFdEjyuHngxdPPPP0/N2uOHk78vmABgU97+MQhftWautX/IlaeuQEcPcPgwFwEAASA+ga4z8znPnBYELojZWadurGclnoPg3Do+K8CXZwX4R4nYPxWIuYo/GgQAQ/8J8jd0+hyYsqseohRzxwDkeYD2DYg/p+IPmT7q0JdnHfpHnsxctv5UqgCDaw8S/sMieI/eF0dTYX9I91uT/I9ET6Afmen41ae5NH94oRv4BoPNh8W3GQWY8DU1zhyCsgcD+a/zfDT79LFl/gH2gK9vm77984cbvP31R3I9IPDLHH/PKPp76dQZ2gD0z2Z8VNhHqAJxAUu/94KX4v9qan9cwSviI4x/XGHvcVfkPzbWS6gqBzXhB55/3J9TrAn+Tq65S3ZA8/6Siqm8Z3sKPbECelKGfsAVsH1UD1CDZ7N+99d3q1WPEXMWEFi5e/6LyO9vIJWcucF5JdNrRgHLAdgCtQFHCMAOYAiunwABnv1fTy8vOm3sgK4ZEAoJF0M2WEAihI8Fztr1UQ/BN67v497aQ13fxQMSRWFivSEwnww25BoOUSfEUBgGz1aA3hNuvsyNZzLLNgsGTPIRIFbw/TG45b+UeioxW+zbsDQr/9Lt9zeXwMBKHmsF6vmhoQ3iEqjsGrW7nIiwGqx9NxqZ6Wv3TIO1W7cS5a713dbRxnI35ip9v2zFKpO3tKpSjHgWT1c84Qs68MVN2pccEtC7HlHwWDrvapbaLMsDDkm+SXreMBSeo5XlMZk2GC91ls3tsEp1kmS6jDIt1OfEwlmZ3Bu4b4Y87xNLiHX8ZZdn1zMWJi4K4dcparA0Otx9GN6nEDocr01zSH0xxFZ0Kg+E1t8G4QbpzAaXLVuiEWjn9Si/T2w815Y75i41EnW7i+KROCY7qPdtQ041ZTqL681Js8wti/T7tiEzBx9L9N7V7FLSj7v9UhGUNQ4FdEGnDjS5tDDWZxWi9y4ODfqw6XOZofr0riwtPlpzB2S5DPXbGvdVdIIhdj2FN/RGguncc6W9xBq26i13p+XRbrDaRLPiHo9rVoU47wwz6mZkaNKUBf/eVQp2KuqQHAg3clrhuqlijqV2gcPmNOUGSpmFJVcV3PLUB+KJadWL4Z6J+8ZWK9FV11TGeqaNsFLMDXSCDRoSWt7NXOG8wmQ+g1pS2xRhLArC6RT5QovsuYBdtxjdGtJYU0daxKn7KUIFo2hykGWGwhWdsTFzHzPc/Y6r4hFqYhVV+JjvJ/1m1rgLk9sx310dQdMtQ9kea82tL7ud6RBTLalrBWKmM+zKQuvtcPjOQKvJLA8mtNEV4TQdtRo/bthcZLuDdF/bh9onry5ckL7ALM+8RV1AaJmSTsMRwofSBAnV6dJ2E6V4CcvQuWwbu54d7nJXXm7YibuFKScOjAFnq6tIOs0xundbNTJ1IcNqiGuR1QBcIx7S6XCks8sqrg5EXrEOh9QgO2wwFF5FU1A5ktgdzL61GlK1pB1D+5nseVhoHHNEzshj50vnpXTscyjWU4XISyw5YzTk7PXtrj30u0m4sA26X21b9LYarmECr4J6k6/VqMMuBVP2F96ZojFdOdN4v+bbuChUhlWiO2nsYhC77XKFL5m9Vgxmq60nll1izObOByHXdeONYLQdUUwo4YVVcY5If5QDNtO7bJfntrvaHmrXDE7aSJ/TTlgXuMXo/HKDZFTFKDZP0+IED6s1dV0OEpfHsGzc1wkSHWTpxDCCmhNhl8lHt/TYfZYdcqHVGlEJTeG8VRqClbdrar2WJ3N1QHSgLkptrrs9KbvLFvc0tdbhsZiUtaaVlxxnMNoKmNt66OPylFwrq6rLXJMt88ZFrLQ5jh1ltr2Qnap1BO/CfD0xEtylYPqx6HJAKKmSzVFt+03SahJQKXXQg51C6qq94b0LaYreJbQqsCRHlrZZF9ftoA381rY5qhmne2RXTLhRRkpEYcmBOLky1s4g6s6In8pjY6+CljVXSnV3yiHECMsXGoPejFv4sKzhXqa9i70Zm9DUNp1zOaL88rhkD4F+GE1dXkZG4wotd/AiOu1txxZxpVn1UqLU4lHIo4w6CpJ+DpZCqIVyCLd0Neha6Vbu2rDZIPfWPsHtzaWCCSQeINEWYqWS66ZuGG2MLPSVgya16F5Y+YK1qUt3DsRQdKfUDSNhWy6DkghVbYNnheOZO+6CBpVPwQhjOl7BJQf3VUSddXSZ04e+Ru3mfo6P9l4+rQOyWjaQzHZ7Bk7pAT3cmZ66MUWdC8vz4J0cPF7JZIPsyBwij5gqkJOgrjWxgrfT7nq0C5s9crFIogatOsZ55ewdnLomtsW0N4PiBXxLXyHV44hJxiPZ9EqsK3Sq6oXj3rkoLE8xKJwp+KFOdk6hTC4e3Rt7Ygko6MFgodLFsRN5rnAzZT20+/RQ4xl93KwMpcZ12JLKA9oIKzPiEInuk2QXaeLZiI+DJKiy2+iV3YmrXTvtK8qtSt8dDmynTgAEyUzLaPGYHvZLl47Xk3WScacl7tO9I91Knbp65Ykt59zyVJWSlRvcDjUBaeeNdpfU/NpsdUGZyqN5dPpwY4AySBoEz7NJqUxKM5CVpxB86LaCsuoaejDDgq/dzXqpna/EZn27oSl83jg9SZvlveiD5YEt6bsE711nRwVMsd1LiiiYqnVtK4kTIgy9h2mhVVdX1BlkUgej3cnkZLNpydlbfEAT+nwvvZTL7e1mOOx181ypHbelqlPJGnu8VrbmFrPr5mrnFzaCh1xQtPR+TLIuMrarcDq5aK9LtHUcVnh9MmwmvQ30ROrdMse5pTqyFzxcNiWHNta0KYeekkzuaNrnoyuYgpNdI8Y5btp4GI9DLJsnWZAApvicej0d5RXB5TuhElCuumf6hT6sDuk2PZGIK5HHg7c3haQpCYkktIEST3FrS9SdpHh+vZLTnd+E+Ok83O5uk133SGAJpWvbZ+J0XsKxkoWBxOK8ti4yip72+zWrbZetl2nYlgJVzqak5Z5ILrtjXXgFRIvlslfLUZlGuPNOxzBjEvp4NnXICyOkLWSArsYy2+9d8w6tmrlsJDHXl2PArrhskAYlP7mJTjE0dWaV8tQ0RN+rSVwQmGxd7qyY2JLe3kChy0mKNiPpHCur1gW1aEwUZi1uVHOz2/enbYqhWS7DJHvOPBDDyHjIDPkcreR8S/pMdGF2IjoBFpciuyaZJwmO2CaRcdAJFeBNKu35uybuddbJjsUSqCG3nV6erurxktXcLjztgoulVdZdnDCFqfj7pThL7rEyxRUtEtmRUwmSh1PMwVRKQrY30HYiuTYIzChMdp5KgcLzR9mm5SsdtQhyCM5SN6jNymsvylpBVq7blNHVle7C3sHaRoM6IT8MrrwPDULZ5fI0tUuvZDHMJpN7sF9nOYZoVqVtrw3G7rWlwW0r1Kl2l7t4sJVdCaDF3Ao3g6lg+GRJdZE3BzlPqIbimuPB2TW2XHAH/x4qW8O675E1c4KbqC13ntw2dXXnDy18aUsotNQSpwiuTTTek49ldGlB75g3+xGYprg0wOhctA7RtmA4MSKWJpxKaViEe0o8UNgYuBZeTHx9qmBBbCNJYPPBMiv4Nhhq5a4whkOaJBennl7S4Q1aIorFsu3ob3vRHi924a7KbrPO17nJ5O3tTtu+Z9iHNEPHfZfvLo3oOV5TwukyUCIRZ7Ybb6hp4Plg5dBZsreEq0Kdck9AWbsnDQPehEukvex3UF1rm80ABze+SSOEO50m9KK114wyQPIefUdV4ovYyvstvxuvoHWDBGrbM8rqfBxu0jRiU3YvRzfpvIk1191SEi0qUg+SvaYxKc2UgGNT9J5Wa9BNyJpn9UaADydMILLx5BCte6DSazE4zVlwRSbqD4IBIwSJQbcJoUdVyJstnyS0UHn5jeb5yCL3GbLpPFvYUcO2PUXuPkuBv2HM0/kS24QhY2007kwmbjhckdy6jEQZnKmSSE2YlCalvq/WxCZzVG9j0/s+DlIzhouuvl7QbSddQXcFWUdkiXseS0KdS1eCVJwbBb0AUCTOdB4FdMpHjnDPckMuJJw5ioRIaDSt0RCdMFFencXUcX3h2EYbgvYwltA1blVvOJuKxUyWpNG6MQp0I8QpdzhQGeLpykhyF1WhlcIAsO0NxmRVaaM5n4b2aGyFznKaA6+fUZAMS/iIU6cKia4C4aR9XlsofF+TsjNJElHme4803eJsGSm6PuueXdyS8hoGyejEDuRyhHp06fLSG+ldPnVt0N52KJ9KI5Uh8f5UFLbrpNwkhJ4ahcwK3SdGdlPESxYrBoN3fnNrCk4AeUZISb7f2CKcSPBQRw7sqhahbE444VFxf+zv6B3m4pOyZIXcqhz/eLmEHR4PidaNy22kyVFjw2q33Xq7rS1XoFrJ5xRJyS65Ai7Nzd42G9m2JO5s6bpAYHHgTvIliWsr6BBZzjtDbsLI4rOzUSKKHw1TEudOmWW2zd8mw0c5EkMdV7jtoi2XZgzVbnBpG9OOBeZI1LZqg79TZp3soz7ZjmAcUfY7vB5xJ83llk6FLByG03ZvgSGtFMZlcOzRTlAznW3SeG2k8N29kvRptbVdIfHTpHFNCa1OYVIhumXlLNesdUiAl+QqjyXxaBDbq2nxIndgDTM21vHZ3khdvLEryuFiibw2ua6PSIffxdWSjdtwL0hXy+Donkdl0HrfkKFuhSJqFKnmRMk4NBguNpyyv3fKaA3GsuHrO5I33VbS5XhH1sx6udyj+FnuNlJ+u503u3UujvB65Qe3EPLXcRPUFzjwlW6/l/aHtbORMxtkcM3uFVEiYaiCRcMlDmTecox0IFMFTw78RVZPCBpN4oUaR3UF7ydHv2DjMBar5DoJ/Q4+tqNpKEvGq7Kj1dRqu0qWoQeQrwRtKM3p+TI+0QHrtbqp70AFLq2KzndaGypsL9XtwVonsMQvY6cYLcpHxexwWwXW4QY08ZadkdmIuJZW7DDxlFEeSDE+unuRVBLyusZA77Quc2HDBHrmpO6Gb0/7UcdOa0xTD0bPlYi2rlOEu27NsEPwgYYDyyDhM4ETCt6WZ3slpm7gB/6wPeYoK8sn2pKRsqskn762J+Wm2fx6Z7uIiS8vVGMVPNnygoysznkC7+FJjafleLo2632nBy0q5UUIOxciYQN/TxKSvhSPRbunNydvyqtic8m08eqIV7kSMyntRDs2ZbNYlZueJzh1aEYXqjET16aoGSE7BDUSyUmy8wyclGN0XJ21HHGIs1q4AZLFh4seV6RsU5OwlTjszFGbPoO6LoQwIRR5ZDB7PL3dcBdi9tFqfXFX6HV5011EKzpKhU++SRbpuoSylbyrqmHQOK1gtDMfHYiUpIjw0PQ2R5eUa4IOCksILoW340FlUrDwvBELDWBtDXuNUmrLesVOd6VY8+Ul6E6cMXpuextRQO9C3AYxxu9TWkF8kAwCUhuoR68DMAvSpnq0+E26UX1/eTpmU5TJKzLeMlPXtcXeCEUmay9Nak1R4saXza4M1TZX441oT/ItqQpWL6tYMqDerKBTWos01PCkouZ3qL60kQBHXL2LAl2fTtzZz+31BR12h2ql2k5K0tWNE+325J/6xnbO/V1GLvfGOjE1A+YuxdTd5cQ1EEXKGneIxBUwH1sIKFbIOQhk5uzuzKt8hUXxwlC4ohNKunKZ/S4yiCGlN4R6sVT8YJ2aq9GbKYVsWV0Tj97J0iN8G+7FBq/cbURibnc1YonvGkUvmZU9KhVeoZOZlc2IL+VtBGrc2fcQfkx6Gcw2RaQdO3V0MW66ECZ7Us29rtmpi514QzXOxW2Z7+1wavG6W0HCeVKlbaq5uOLA+I1rruSO6oYdAkS4w2dl1PzBEetctfzaRT0r8u4N6tCOtN7LoQucQp/GI9KgDW2DdjJJJYyglsOGc++ujx0sMHgP3KkrsbbCr86GX2O8c1PFS3igOLyetI5lN3JuqM72bnVW0RuWEtpkkI8Mc9TkAYzpdcWdG6QFWGDeaTC9X3p9vXY17MJmzJLgEfOY0lWCQXzEZ6HNbk6NKO5D10Yyq0m2ukfDBNkFKz0NOt3O0XOGNOdyQ7Q4jpuIB7s7fY0OkFP7U0xgjeEN6670yrJd09etzhZGHMbMkW8uazw43Zqb28hiQEAih97KO/DLRsyD9Fp75A3uRaY856djJRrhNblxLBsx5RX0CJ3do1Lad069GaTU7DwH948H/sogPFLr3CY8a3GoMQB3cH7pHiJ0tCPb2F7bSQgq8SgTAyqsMJze2bmenlKy2dmDuwnOBcW6yrXaQ7IV03JH3A+kIN1v/E5jFR2n6m5r4OuNxEmNkpn4JZNLgzk79RWJ4JsZ6NqWWcpCry7BpMjat37XlYjRsx0Dqn0lCxuDhofivEQsMDLUULiCqRWFx01xVu8HWioYyi/9aAtda8iOSB7DlKvexsZR0glyc8du+O2UusltMI9ococbG/Q6ot4xsHq8Od3uxG7ggssCXnc7emV5CX5rXKO7rE7dehnuQJ3LW/WykXk1O98J93Tq9vDqwGEkwWYXhQwdVw2CCj8jcO6RCO+alaFC10RPau7im/vR4+EO58kuVsPQZGrSOMliiODUNTZHWDU9ERfXdAKq3aAKnrlyi9qub7R3Y/RMpchtsY5Ti3SWyKGMyY170M14Miv/gChSiCE9omuH4GbeKQ5a57Zlr1qKEKbtthFVkcz2yvJyOuw1ScNCaN3g8AYOdyxkZf6Z4zYU7ojI2HAoGdhmedTQHvdd7bicTPwmYTqbd9aEEhqpiR5irwZOCo9HdFpql6IRWxtJsMvJFLiOZ2G5cUp5DS9XhAxXtwukbLM+wLfjqgvDNNfWTG8OW6eIPDGbMvfcH8WpVlBkZegekVIcb+zuI42iu0u0I4a7uQ/VO8Rh27vEutEQkrbYrbyVraXwpS7HcCgsjm8g3vNUG1gAp3TcgFW2VawLlMAwg5SxtTxn1kaFOMtDmtByrs3Uu/m9vMEIWYmevb5Bq+3NZA/2beKjTbGS0OioY/1liLisTMkrcj5L9pFnj6qDsumxgfawiupQPLCqC2p22J0l356s6xbBNN9wkbFD2a7pQIcqBnKI91znobxLy6vVBurrE78SGf12CxAF2Sx7yEJOUA3fUYiOsPt+OdKDuKO2iIRDnHOR6ohKgmsiC6l/REoD884+mPocwmJLOdE0XF2e7jvXDLLUMmCPH/Z6vd2pV3WSyZwJ/B1ooUjO3d5i4ob70ErYnIIovjV5iWrZabMR1jx76CvevA/9zR+XdJ/xmXJP0L5mKUsJYMFRrjF2kqAmzXrohjeYqlGowKWaDoI0NNgCu5sTqUrYtBZ4A0GGE9/m+dZoQnenaQi21tc4D8akY6ZQFPWXv7zNp6ZfT/Le/u3X1ebTnv9nB0vP86Gvr5s8jioDx//04PXp3xftrx/eGi8Bgj0P09q8j17HUX93lPbxXz2KnKmMzzfCvp56P4/TOyea359+S0q/b7tm/NJW+ePlE7DD7dv5Xct2fh3XA99/PHv9xhj8dvzn6yNB86WrvjxPE2eOjxeWisBPvl9Gr4NGQOD1dtQXlMC/BE09K/16dwHoir7D7+jb3/43rBdR4govAAA= -->
