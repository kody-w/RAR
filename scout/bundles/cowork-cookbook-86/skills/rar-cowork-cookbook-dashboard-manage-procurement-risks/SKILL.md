---
name: "rar-cowork-cookbook-dashboard-manage-procurement-risks"
description: "Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_procurement_risks", "rar_sha256": "d0e12e3bd273bba6c0e540db90ca9815d11251c0a1a8f3fa2f3c139ca47fc199", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_procurement_risks`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_procurement_risks_agent.py` and in the RCI capsule.

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

Manage procurement risks Interactive HTML Dashboard — Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-procurement-risks-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_procurement_risks_agent.py` and embedded as the fenced Python below (sha256 d0e12e3bd273bba6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_procurement_risks_agent.py` first:

```bash
python3 dashboard_manage_procurement_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_procurement_risks_agent.py   # or on stdin
python3 dashboard_manage_procurement_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement risks Interactive HTML Dashboard — Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_procurement_risks',
    "version": '3.0.3',
    "display_name": 'Manage procurement risks Interactive HTML Dashboard',
    "description": 'Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-procurement-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '965201866d8669a8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-procurement-risks'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-manage-procurement-risks', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-procurement-risks-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage procurement risks with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage procurement risks data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-procurement-risks-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage procurement risks.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl', 'example_request': 'Build me an interactive HTML procurement risk dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-procurement-risks-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of procurement risks from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageProcurementRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageProcurementRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-procurement-risks-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardManageProcurementRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
