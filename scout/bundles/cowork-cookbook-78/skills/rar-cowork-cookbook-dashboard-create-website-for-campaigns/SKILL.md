---
name: "rar-cowork-cookbook-dashboard-create-website-for-campaigns"
description: "Pulls create-website-for-campaigns data from Dynamics 365 ERP for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_website_for_campaigns", "rar_sha256": "589a6240c6f3b0f37d007b3de5af69bad846d32816285a3d84f2ae77073acad4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
