---
name: "rar-cowork-cookbook-dashboard-configure-segregation-of-duties"
description: "Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_segregation_of_duties", "rar_sha256": "18bbf04672d3a293b386865747f3ec12ab0ec09f043b66ccfc46d0a496915a84", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_segregation_of_duties`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_segregation_of_duties_agent.py` and in the RCI capsule.

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

Configure segregation of duties Interactive HTML Dashboard — Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties
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
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-configure-segregation-of-duties-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_segregation_of_duties_agent.py` and embedded as the fenced Python below (sha256 18bbf04672d3a293…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_segregation_of_duties_agent.py` first:

```bash
python3 dashboard_configure_segregation_of_duties_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_segregation_of_duties_agent.py   # or on stdin
python3 dashboard_configure_segregation_of_duties_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure segregation of duties Interactive HTML Dashboard — Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_segregation_of_duties',
    "version": '3.0.3',
    "display_name": 'Configure segregation of duties Interactive HTML Dashboard',
    "description": 'Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou',
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
        "upstream_slug": 'dashboard-configure-segregation-of-duties',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '25f176502e1c9fd9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/configure-segregation-of-duties'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-segregation-of-duties', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-configure-segregation-of-duties-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of configure segregation of duties with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull configure segregation of duties data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-configure-segregation-of-duties-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing configure segregation of duties.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls configure segregation of duties data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou', 'example_request': 'Build an interactive HTML dashboard of configure segregation of duties for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-configure-segregation-of-duties-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of configure segregation of duties data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConfigureSegregationOfDuties(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureSegregationOfDuties'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-configure-segregation-of-duties-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConfigureSegregationOfDuties().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
