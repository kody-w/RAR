---
name: "rar-cowork-cookbook-dashboard-retire-services"
description: "Pulls retire services data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and saves a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_services", "rar_sha256": "e6671c1094692998907855e1cce603fa9f2bbd16bd227dd459379d142ef177c4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
