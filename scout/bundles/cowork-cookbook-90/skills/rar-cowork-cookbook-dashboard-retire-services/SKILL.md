---
name: "rar-cowork-cookbook-dashboard-retire-services"
description: "Pulls retire services data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_services", "rar_sha256": "e6671c1094692998907855e1cce603fa9f2bbd16bd227dd459379d142ef177c4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_retire_services`. The original RAPP
agent is preserved byte-for-byte in `dashboard_retire_services_agent.py` and in the RCI capsule.

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

Retire services Interactive HTML Dashboard — Pulls retire services data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-services
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
      "description": "Name of the generated HTML file, e.g. dashboard-retire-services-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_retire_services_agent.py` and embedded as the fenced Python below (sha256 e6671c1094692998…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_retire_services_agent.py` first:

```bash
python3 dashboard_retire_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_retire_services_agent.py   # or on stdin
python3 dashboard_retire_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire services Interactive HTML Dashboard — Pulls retire services data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_retire_services',
    "version": '3.0.3',
    "display_name": 'Retire services Interactive HTML Dashboard',
    "description": 'Pulls retire services data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)',
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
        "upstream_slug": 'dashboard-retire-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-retire-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad32ae65c48c882e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/retire-services'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-retire-services', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-retire-services-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of retire services with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull retire services data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-retire-services-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing retire services.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls retire services data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)', 'example_request': 'Build an interactive retire services dashboard from D365 USMF for the latest fiscal period as a standalone HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-retire-services-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable retire services dashboard from D365 ERP data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRetireServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRetireServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-retire-services-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardRetireServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
