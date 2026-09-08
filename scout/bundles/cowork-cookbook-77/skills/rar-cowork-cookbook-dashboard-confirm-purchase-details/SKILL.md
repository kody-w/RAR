---
name: "rar-cowork-cookbook-dashboard-confirm-purchase-details"
description: "Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_confirm_purchase_details", "rar_sha256": "309b54ef6794ca0aae660f23cb8bfe794841ac548edbe6078369a72e4cb36f9c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_confirm_purchase_details`. The original RAPP
agent is preserved byte-for-byte in `dashboard_confirm_purchase_details_agent.py` and in the RCI capsule.

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

Confirm purchase details Interactive HTML Dashboard — Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details
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
      "description": "Name of the generated HTML file, e.g. dashboard-confirm-purchase-details-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_confirm_purchase_details_agent.py` and embedded as the fenced Python below (sha256 309b54ef6794ca0a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_confirm_purchase_details_agent.py` first:

```bash
python3 dashboard_confirm_purchase_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_confirm_purchase_details_agent.py   # or on stdin
python3 dashboard_confirm_purchase_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Confirm purchase details Interactive HTML Dashboard — Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_confirm_purchase_details',
    "version": '3.0.3',
    "display_name": 'Confirm purchase details Interactive HTML Dashboard',
    "description": 'Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-confirm-purchase-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f994bcbe73e854f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/confirm-purchase-details'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-confirm-purchase-details', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-confirm-purchase-details-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of confirm purchase details with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull confirm purchase details data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-confirm-purchase-details-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing confirm purchase details.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f', 'example_request': 'Build an HTML dashboard of confirm purchase details from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-confirm-purchase-details-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants confirm purchase details from D365 packaged as a self-contained browser dashboard for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConfirmPurchaseDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfirmPurchaseDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-confirm-purchase-details-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConfirmPurchaseDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
