---
name: "rar-cowork-cookbook-dashboard-run-campaigns"
description: "Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_run_campaigns", "rar_sha256": "5bcb98ffe21a85a0a35e8f98bd9d787ce794907d6791734a1948f9e406b741eb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_run_campaigns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_run_campaigns_agent.py` and in the RCI capsule.

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

Run campaigns Interactive HTML Dashboard — Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-run-campaigns
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
      "description": "Name of the HTML file to write, e.g. dashboard-run-campaigns-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_run_campaigns_agent.py` and embedded as the fenced Python below (sha256 5bcb98ffe21a85a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_run_campaigns_agent.py` first:

```bash
python3 dashboard_run_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_run_campaigns_agent.py   # or on stdin
python3 dashboard_run_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run campaigns Interactive HTML Dashboard — Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-run-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_run_campaigns',
    "version": '3.0.3',
    "display_name": 'Run campaigns Interactive HTML Dashboard',
    "description": 'Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-run-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-run-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2e8c862b994bfb25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-campaigns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-run-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-run-campaigns-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of run campaigns with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull run campaigns data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-run-campaigns-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing run campaigns.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls run campaigns data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of run campaigns for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-run-campaigns-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of run campaigns data for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRunCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRunCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-run-campaigns-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardRunCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPbRpblX+G8jhjbTemRWEgC6qiIAQkCBEAsxEYQVoWMfd93uv3fJ0G+J9kuuaorYj4NJQUJIPNuee85N5X49cXq2rCoXz69KJ6VL2grTaPQqxdW7i4OxVDUCfgqEhv8WzhF3taR3bVF3bx8eHG9xqmjso2KHEyXujRtFnWXLxwrK60oyJuFa7XWwi/qRRt6i6xo2kXtOV7eLvyocax0UXp1VLgLvy6yBTnlVhY5zQLZbhbU/1YO/OLH1AvAKDAhaqeFpvDUT4s+sh7SjrK0KNMuiPKHqUMdtV6zsBZNCy6ttMi9RZS3Xm05bdR7i5PKn4E5TWgXVg00Rqm3aIuHpKJryw6YVKSuV38AFlruxyJPp1fgojcCX1Kvefn0898/vETg98unX1+c1GrArRfyXZ7c5Yd3p8Gs1MoD8LicQGRzcA3cBEHIwC3X8xdvVz82Xup/WPznfyaDVQfNT58+54u3z+eX+Q8Q+rCvLaym9VwQ1tKyoxSE4nVBpIM1gWh7bVfnT7frKA9enzO/SSrKxd/mZz8+lbwGXvvj55cCmGDNy/b55acFWJ3PL2DZwO/XWUr540+vaTF49Y8/fZPTdHbsOe0sDFj9+uXt+k0sGPhtaOQvvijS8fCmCyx4VHpA+O/8mz9P09/EvYXky3Pwj0X5YfF9ybM/fwP2PlPPBnK/LxbEAMx8eY2LKP/xTUdd9F5u5Y73409/JdYJPSdJo6b9H8n9+Sk4BAkDovUWkp8+PJbv74vlm29fZf612hIkzL/jCRj+ru5roP5K9mNl/yQ6jXJQK+9r+V1x35uw/Nvi57/07Z9N+LDwP7+QXgoKsbbs1Pu0+PWRIj//4H67+cPffwOi/6UYpehq5yHhS2blke817ZcvP//QPG7/8Peff+hKkMWelX3p6vR7Mr8X14eeP0TwbdSPf5wL9Gt5khdDvvhaQ4tfi/J/1b+9LnQrjdxv95tPi99X4vxZLmYn3pU+Q/C7amyArb+L408vvwHIyYE3nfN4DPDjP/5jwUdOXTSF3y4UB0DXjLhtlHmz8WoYNQvwd0aN2gNxbSIQ2LdxIP/nFZ4tLvzFL//HeYD7R+cN3FdfwfELkPjlK4b/8rpQZ5CsIwC1AIxlQpI+51YwozhQVdZe49U9gCd7ar2PoIo/zj8A9i5++QuJXx6TX8vplwdyR0+Ukw/MjHBNl3qvsy/X0MvfLHcAL3mj53RAblrMvDHDdzNDdVOkANzb2e8midJ04UYAQwA/TQ/ZQO+nWdgvv/xiA2M+509IRhZP4mpWs2Hv5iw+fgTe+GkUhO3n3HPCYvHDr7/9sPjvxT+b9RA+65AAJ7xFHljIKqKwAJXUZWAYWBSwjAAmHpH/9be3mAIxOWBasE6RH3nPySATE899D7ByIj7Cm+3C9kBgQVCzsqhbgPOLqH1dMP7iq71A6fxoZoJwplnXK73c9XJnAlIt4M7XSOZFu2hAujX+9GHRNd5D6y92bT1MzEBJW+0vC/4gAd4p0pkj6zceApOLPALh/7r8z/tASP1Ds9i/i3hdCHPuLUqrtsqwtt50+NZzXQDfvE8Hwq1F7g2f85lZvTlUj0J4hgcMApFx3pb044OynSIDVe8277ofY6yZHdUHS9af8+Ytya16XgoHgD5QGnSRO0P/f72lVBMWXeo+4uc9u5O3VXDfVuWRg/Ifmhnmz+3EV/pffO7gNYQu/v9rgeYoEDQtH2lCPZKLo6DKt+fqzL3g7MazfZyNezoJKvFbo/IORu+Y/DlPI5Bq9fRfz5EPG97GPHGuq8ESyIT8kA8SCqzOLPeR73P+1vVcKdbn/B38PwCHH0gHlhyAAyie2al3hfPTd0tD4Pp8/a0ReOQHCAUIF8jpRdnZKcg33/Nc23ISYNUciPfFzed4gvodwsgJ/+DVvDogx4D8BTAiAlUICOL1KyA/n76b/oeJz35nnvLoBTtQsvVDALDDmw18rGvUAuSy2mfrDfz89BAC3MjKdvbdBkUDPH3e9Gqv6qJmToUPb3H1SoDJH+fvp6fzXW8sQZ2AYD2X/vVZPzO0ZKCbATYACAGpk0U5YHcQlLcgPARa2QwGAGzf2s+nxMftN4e8R9HNtPQ+cXZknjMz/TPZrXz6PWao30sTIC+bRzz0/jnTvmqbZc+42QDsAxrfnz5bgtcnqz/bhsW73E//sLf58d/b/jx4WvtjAnxahG1bNp9Wqye3vlPrK0Ct1dPW5hvNfgQ48fErTvxB3NPTT4t/z6Q/iHgriU8L6HX9up4fnd9S6u0DInD4uL99ROenAOq8b1AK1BcZyKl5vSbA6195730IIL+gBrgEBj95sJnpcwCM/QB+EPzP+e9zfK4xwCt5MOdkU/yu9h8NAMj351p95SfwKG+BbnduDgNv3ok9KqLxXj7lAGQ/vACg9P7JDmzmnmxO4Gber4FSATDbRt7j6oEHYzv//OMOVnz8sNLXBekB7Emb3yfZG2PMjPm7Wng6B5xygIYPM9iDEgf5B5yblc91ZDUgMUFOzk60Uzlb/dysze3dkwS+PEngHy2i/sARMxc/aB7AzH+B+vStLgWxe8Pw33OL1QPz51L7rtIHpXx5Uso/6iRn8vkD6wAFVQcK+sPCew1eHyT0XblfG9l/FHoFXcUsxy0+zfz44Q29wDfYfHxYfN1HgBC+7eweu++8A5vmn+c9zLymjynzDzAHfH2d9PW/Imzv5e/fs+sBcV/mhHumzZ+tE2boAtA+h/HBku/c+KDUN7f/onA/wmt4+3G9+Qijr2Gbpd+PzJsFD379zjI/7s8FVHt/MmJubK25vf6RLJxnM7l6gsDqKXT103c0ApUPGgBkOsfv28J8C0/x2O/NxoFwts//nvj1BdSMNXcsb1XztmEAwwFqfmzm1mkFAAUoBNfP0gfP/qdbibdpTWiBnhbM29iOjWO+78GQhW2stYVsPMzHMdvF3R22c7wdjuLrnbvd4dAOQS0IR8FjD11v7R0KeTaQ98SNL3NbGM2mzHaACHwE0ON9ewxuuW8+PG2eA/R15zL7+ubKry/2FgUjT2jDEM/PYYVD9uq6s6ezsTLW2JgOWlfqVrReDqdrZ2S3kN8pF6FpCstFrufwEIxUHCkdd9kaF7yUyYuAR+QmzLfKyoFtlHNKuGlgfHe5iWf2eDexrXPHsQ2P3BwTka9lxPBtmlxqiG+NyqPujDhE3DJZCuJOwJdcst73aVQzzIqW+hXk5qzJFonhZTJDycr+yoU+JRdVuy4MxlRi9VKN0elisRN98ao1AJRa09lds4Z5K6RSHFuZOrp0V/kIr44iS9Uxzx07IWJ32Mrv2Ymp7mFgRStRTa7XVGxQSjtaAEmxc3W5Bi5B9YHFKtWVWQ7jSXDEWmTpSDuObKrp1yC66jLJ+UHDB1mVrGEji9e2YNTYxutPNbxrrqwnnWDEzaQ8j04H63i4XYG7TCdMRQI1mH67LVuzYQbVK8xePiO8S9AKDB2V84oPkPt6JDbJXhwu5FQThTNmbAO7uUpuGW2T3GE7HkaxOYQSj5UBLLbJ0aq3l65s4yZ1RqimOLmSCKXZ0aEVp9vrit4Mtl16G6vmNgltKSFLXsoo4ELao9AuuQcaN2WxKe+9IPIUMBNi1axKQTGNIp0140pRajSGA4YfCX1pWM4FVnsrN1IDcyczLI1YFZhjZk1ZkQyhy6IiFSnj2FZ8hK0Ljikwo7xRQhzmdLdfZeN1vb3ql1GIgLbwvjR408LPK4gvVbOWUjuxVt6tX2unHWNSIaEcbXfNXTh3T+fW7igwHXuS9+esKRCVZnASidfqYWdfPJZI0P2wVfpr4WcVwjSni1oQ4WSKjD8W/pmjwrYbAuSW56J+4cLapkOpvBJ6adPN/ox3cGUUKcMi1LZydPpmG1Wtm+kpqRmjCO+rKKiqXBhBEHUAev4259gVzGLnQtB6gl1hF+vAojXOXC/w+RTp2yEt/HalL6mxiaKzim3FODl4tFuiRtXB8k2/+JCJwpf14QZd6FB1kMaJ0GVcHeH9tcedFbXbbU7IgV4uW8VMVvAJGXdSLmHb5cj3cqaP5yUlE2xxSCH5lsk0aDw9XdySB6lZM76uSdjtjIhHoxno/XK0l1Aq3oO9kQnysa8K2yUTpTtmiuAmgV5BEjvBF8xsdULZKZSgHxjIsG50yqBK5hOILt4imMGXvS/0yKgLI79lBZGsnYG0nM4gJ1Dh2Z1HZbcb+bvRHtVbhuxilz7ZAndC16IvxkSNGAGcp1cvVqEDFvfRstxQYtMcDHMp+16oWAfvjK7XZw/yDagqhKzgM8lGHcV07sry0Dp2c7i7YjGe6VYSISWOnU6XwnPSCSfuAMXbwEBjB+cH+iIlVwFitDNanfhDjV94jsS0nmGQTr/KMc13UrUMM8jGyqNeDctxGZ8lhDFSrlHR1imRlltdc7auc6wj1mXrj+wZIauVn4IdgE7wKN25yvLO4UW3bq26Z1iGxemISdcnKad357yArwGKE2h2FU+rxHKgMueOS7ylezGmpY3eM56C0uEmLcTdyh0OOnI/xEGFNJgCF/zVLEwdxqabdWMMkyTRq1Gw6yPIn03N8QkaTNeNeqow7l43oUeKlmCNRV0deCqvV2flnrZImY9+OJgXw3DW+NrXkdS5IwEtl+bmEkj9gVdBWukYWNtTcUpORS8FudQZXeRnJMS2exkTkQ7ak4SyTrSL3g++d0QhlLqs2JOZOdQx45yql6Nzr8gygfPbbD0kFiB8Icb88RRoxvFKLw8IobYMURDCJTpF+5uYmXFTRwwMiLhHkIRu9CxgBpFgD7yoQx3Kd+uYOjJp1uVr5pgItmRdWy2jLiE/HCZtcEKHq9r6EEyHcXvf7jeWKTPNmov4i9LhWKEkFNVwrTsa/IWYavnC652C6XUNsO5qa1ZwhVoUr2VH8yEZa4/nG8a0+xFfrmp0dPs7NcpXp0zK3V4aUVwsjsU6WnJ7pXXhmKf32/QYiVV/8tSxGne2me5xhLlcbOgqoeGKl4x4465WomhMuDFhun+tuyEp0d1RkgRykK3jQBhmUnhktnH3RWRQdySCooafLu5k7wbf3tNVtXP5k45II1UlJ3tnpoF6slhsY2+Od45JWf3GoiHPYwXPdqg65cR91LStfuaaA7XSq8gk/ewMxTF35iWyOBPamIkrxiRgP6813C0oayPwU4UrQdz3rLzb9W2YbqiqxSl158k3jUacbh8GG/qwHq5rgVjGDO2c9iyhUOuivnWb8RxeAvOMtPdy0rr7dl3C1N3pSkNPN0SwX64DPbniQ9CdJjs9+WqjuSx9jradn0hhcdZOtLBLBDFXUayeAijGtqSu0+aWXqLHgLxywYFq86roouJQHEVCXR2ne66NB5gyxppanVPqrjHaKN/SK2uXaaQEx55Nla1AAX2M51coclGOylVX5VsIq8lNvPSB6Tl+ABVcip5NLlB5USgvXq034eFqDkSzQQ1TvtSOLu+zSRhPEdsxt+0NbslrA4AnNfZEEOERoXUsOur7LWfBhlMFDH2ASyY+T7W5Y9PhFuQYXq1lcsNzwt2hoX4fbPtbWlZUoZMEVgMEPO/ptJO3vBzxmw3obmmSHfvhgsr2XdSpJbORjJJW1/ZEQFntcWLEl1Sv+5TCWNFyOkkat76zHMeZPIfHaiQbQ++CEjyT8RpmFTjFudpmlKt8SeBbs7L48FSsCZRz/eW0rCM5vPiOksUSpS2tfSmux/lH0Eh5piXXHexr8gEPkAER77aGYcf7jZQPe4OyJUTvNlAa1r2JOeheMVYrSaWwmx6HcXdmof00qgG5FVBL4YhOGPACYsxAGh2aP6YJup4OjKT5xRGTSotbsxeplLVLtadbbWhFrUqMPdsthYzoqqIdgv2uqm+lKtwLwAo+8PWUW1NL3otbER8OWZfVd54yCpoc+ENohhRZ8LmXriMoacUItERsQBehK0yYdBfZE6IV3v54X/YCrGxOhjuQDEQUwVVL9QOirM60dzn1Q3a0jT09QAjppisEXxUNOymo2WHLTg7k8LRb5q27TbBJO53RFcGm0J0K+ZaVgn2cCpNV6kNnr3Y9gGMix7IKZEvKaNDamvbHoJavJsNdxlwT9A1+tlSWTAjXztYCf6n81uc9yDL3KNqowXiyzns9KvfS/nSoit2FsyqCuJ0Hl9ai1G/29zMxdns+S8tTYO80du9n8KiMfZRGlkMbuVVceVO/HANOVEr80hMRweSy7tpWjXoEh7CUlimD0auWedQ1uNbQlNxzDrU1D17WSQeYjxXWGlS0Co5HUUWg8zHQV3KSDqS+0XoKm64Dc9Qko8e20slo1q5/lzer7RXmbJc1g22bIrG8Au1Uk+6gFOWO245hy5jAzAFTYoMaNtwylyihp49xnQpRtz2XVh9UakIamzOsoXvQChTwlk5Vc2CjJUpdvaYhblayPh31Ce4U+eySg4l2EhYNJWntJzuhw5Kkt8oapaxI0GA0pNN14Z3DzNJVBon93dLA10VUusegRdikhWvdCofyvBypPaqu9rZAb/mgG3eqzCRaiehwATuC74qjvrP3O11XboipwqDZcDYUcrOKkt/cu3WvZVy/u5D4oLo2VzmdnGDpWkwgIUHTozD6McFfE1D10DXLKqLViGwsSRXaWxud7SsBrQ0aHYId3gqhEbOepUgsKcoG3TYUcViOfi7tpkjKLqBUMVKfqGtly8e9Vh+Y8y3L9rXShHUYrnq1TJnrpmmUTWBhcXKSQwaTjqmR8dsS3l7JiNIt9iAw0Z1J70t6FUMa7/Jr2ZDdSEvyKwbnRzU/2VSq+MZAjyECawDWuLSyYDm+kJtdzZyCsqx6DU0EOGQgtRkOtZJUlk+YOQ66dD+2URVHyqZHYnNrY/uWoVjUR0/D3ZZE9uiQWWuheQvr1qXGQkAyx4CKpMg8TzxY29t5q1/0qlR6JjnfhdppCDvi7gfdlw7GaRcwkXxL3HsOiUjkdhrG6Md7G3deDRqWkqLXmi9Tm2tXw6yg2tkqCXHI52iuqMJw4EVlPViBNeZs5pSc5PdcreOqcKKEVu8QGwy1/O6KxjycrCN/KNdrKzvqBHOGV7aFjNQ2Y8j8csqqPctcJK8+DyrhXEmQouXKSlbS3jEiYyDDOuhq/YSlGClWddqVIP/O0Eq0uCLttnGKnYRVwg28fXAIlUM2QsXcSMbE91AlUJJ9Mg4yEq5UXjki+SAcEpoolHPOmJ4c3rKpq3sqk4sTLYskWabGjr5AGXKmQFxEWYC0rDPLxBZG57beXq7cHbTCuXejNZu4h8rqUpH1tDWkgRqW6t6ppoTEkeZUkbdEW3VMXOvONtjetBpdjs45RtfFHt3aRAtdd+g9XJ94G8J2Std367CGI5HIS/zELCUcbDCJLQRfzo2OEui0YVDRvZidmMPkNpmGMo7bvkNdzDakk7Lcnkcfz0yE7N3dEar7pcTtjtvT6LrrjbTtXS1vebkEuw2xlfDj7TKZ+vY2bAVYsh2DJDeIr3vQMbn3gQH3xorFyyzAmhPXc/1AZdcr4VHwnoROSx6l3CPTa7l4vrZk3l/YZKIMXSeL3MraKUFq1fGzApcwNTLAdmWpSurpOmobb5VPFImbV+zU8xevT0xsoKq6Xi7F2swQVQtK3hgwTK3DSVMku47MmB4NfMRXq7Fdajyf0H7GLv3Cx1yeG2MTgqlduzGulxrRao7iD5152VWgkYxD+HxozJA/Or7KdJ60pQOyhDx/49jHIL5oQn07Ss7gE5NyRIsxjqVRYVemJ3AmVa34u5R5UbMGJCTA0Km/TSqXtWd115QTkomCptwmUxjvA9g47ptzMK7c1lNTxEkKKjncKnOFGFvwcayQzSFMa0/MIUfsm9lEp13CqSOXuJY/FR2VSEoLQekaZ+9ULy47OgYp5kVQSy83dIyLByTd4FcJvt0M86Tat8udDfYqG6C+L5bicsff0bQMCvJkQUJENFXAmno3ma0FyCL0d5fYiLlQv3mVdHWbO7PLdzxXr0g+QM3lmTYlw7miuR/dOo1xbrzbmFxxPvMJVfHker0qXZKpnCE5ELB4M/I76HOaQ8Wanc3vzplaKPutdGhUjRrrI2N7Z6S+QDGL3MkpiaP1yYaJpUNsqGBTDhfhbGW5PyW+ZNQYLPEYhh6ViWToc6ep4fZuZTBo6obhUt1bPBzv/HZFD1u24TAch6tDKeMlnZyMVSgRfXli2t5n6zgu7e7cyAeEka/37HQenZExd1RBwzrOXB2p9W7hnevOe3GNZ8512d22W77Oy/tJstcsH937qBKwvUdj9E7R8Jt/0ZYnFiBdtXXQ5U08b3Difu0EQXHZG78rVblB9lMOhYJtKqWfyrEqLK+4EYUTfa0898SgnViYXj8OAzYVhGZDBwFR81pGSKIJ/N7EtZzZ1EwpsWCXdYJlX9/eFeUED5RJWWigIkTLNmfVjVFQR13sshvJgvCtF4uea7iaS9/JlYD5cOU7qNvtHJXvhe2u4yHBzQqJl9V4u+kzU2JYYud1SNfUqndeZrs7nNRKoEaku+Ss+GzhUgy30y6SKM6qpxIUW0aw9UCJ6c40Iqg2/IvVW/EYQAbduDhvrndxOIxx2yL2qUNuxTLixKqbGD9fXuo9xaTVpZJJRSkHm/Tuu1hn9pG+dFWxC3CKkvBlxxMcLMjncKnY2qiWYE/d75cnbIgpjeNB6IkCd300GigilneVfBFNGt9uUqPzIlhdo2hCbptpgs/RHtOy7VaBVc059dahtDaRU8P8meMmf6o7tMLp3YSECHoQzo68WXKefIzaQxN3+368LBE+GLttztwlDukPAS5KZj9sb8jYtuIm9TfzBuastIiVNwy87sF676AiGkRDG7R62thud53C+Hyd+hZOQ327GtJWq0uaGyESaxzY9EmzvZkQaZnTVS5u1/1gYtGatjwPGyCRb90dxJmKYwq+QHsDx4wWHyeMD/W3dmgxbBADFyKatFfyg3Wg08JLUHIyUIpSsI23g3LQg2xuekj7wz2ic9eunTgeYdNr7d6S7n68xo+0Lm7B1qbrNnef64wQv+/K1WHAHKxstqXuavskTIOzIuIp2UfHRDvVV/G0XFlLR8JFllghLYUjm26g9Qjb7UdhC4NQgNbk3BnZLpUE0aCaOsCuIPklDNs5aHpX8xsxqrss2gTskEIGnovNiTxPLAGhQW90beX0O3lnFz0X4TE20Aq0S07nLYRGnhkH7qSwZw1QvZM5sbVBKO+6F2I3UZFDPdxPBXHJSOTErIiSCnKNjywWPyPTmhBPco7RnG8Lbac20H5NxnExHZerLh8FM7HvfdkJI+i0UFp0iy7cpRRmUAfcRHVfn/fRxj3NScUI2KpqkLW9G3e4q6AhIvpnCY/PB9XYCoPt9E4wdCK570DTGNBJHq86yDAqU8spTdgiVOzUSw71Oz+IFJGuvAFbbq+c6971ai8A6pZtYeoRqt1VVJZRHrPaRHTr6DFVxDheuzuenzxNtkgIlUqjTaFGkPTTTpqgS7FVOyKeiuK4t/bLjctvVZXQj8w174J4Oua6UA6OdO5qC7NQ8jAmqBrcwhyDA0MjraDi4nDyU2I6TLm5Pk0ycpCNfh2G3R0BBIGLS5oaW6K4+eim3Iw11GCKJIBcz8h1c7RshOiLXatsEj5CRFY85Jq8xmCiDMeJWrXQ3ZGm3Q4/+ftKFhHiWt6xfVhvigQ5VUvILFeUJ6HLk30IxT4K1tDS8mll8mJ/YOW8ETb35EgQxN/+9jKfcr6fvL38q3fC5kOb/2fnQ89jnve3PR4niZ7lfnro+vQvLfn7h5faiYAdzxOvJu2Ct0OkP513ffyLo8F50vR8qer9yPl5eN1awfxG8UuUu13T1tOXBnS7j4O2Dy9218wvIzbz+6oO+P79wedXPfPpZwFcKtsvbfEls+rEm58/3vbJPDeyWu/tMng7+AOT314u+oJsN1+8upz9e3tLALiFvK5fkZff/i+uGhcnDy4AAA== -->
