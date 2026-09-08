---
name: "rar-cowork-cookbook-dashboard-create-website-for-campaigns"
description: "Pulls create-website-for-campaigns data from Dynamics 365 ERP for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_website_for_campaigns", "rar_sha256": "589a6240c6f3b0f37d007b3de5af69bad846d32816285a3d84f2ae77073acad4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_website_for_campaigns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_website_for_campaigns_agent.py` and in the RCI capsule.

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

Create website for campaigns Interactive HTML Dashboard — Pulls create-website-for-campaigns data from Dynamics 365 ERP for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-website-for-campaigns
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
      "description": "Name of the HTML file to write, e.g. dashboard-create-website-for-campaigns-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_website_for_campaigns_agent.py` and embedded as the fenced Python below (sha256 589a6240c6f3b0f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_website_for_campaigns_agent.py` first:

```bash
python3 dashboard_create_website_for_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_website_for_campaigns_agent.py   # or on stdin
python3 dashboard_create_website_for_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create website for campaigns Interactive HTML Dashboard — Pulls create-website-for-campaigns data from Dynamics 365 ERP for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-website-for-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_website_for_campaigns',
    "version": '3.0.3',
    "display_name": 'Create website for campaigns Interactive HTML Dashboard',
    "description": 'Pulls create-website-for-campaigns data from Dynamics 365 ERP for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output',
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
        "upstream_slug": 'dashboard-create-website-for-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-website-for-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dd3d8a7d1090c766',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-website-for-campaigns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-create-website-for-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-create-website-for-campaigns-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of create website for campaigns with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull create website for campaigns data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-create-website-for-campaigns-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing create website for campaigns.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls create-website-for-campaigns data from Dynamics 365 ERP for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build an interactive HTML dashboard of create website for campaigns data from USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-create-website-for-campaigns-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable HTML dashboard of create website for campaigns D365 data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCreateWebsiteForCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateWebsiteForCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-create-website-for-campaigns-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardCreateWebsiteForCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
