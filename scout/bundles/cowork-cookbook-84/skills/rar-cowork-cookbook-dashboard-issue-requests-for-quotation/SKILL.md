---
name: "rar-cowork-cookbook-dashboard-issue-requests-for-quotation"
description: "Pulls issue requests for quotation data from Dynamics 365 F&SCM for a given legal entity and fiscal period and returns a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) saved to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_requests_for_quotation", "rar_sha256": "8ca78b24cc9bec59b68cc72f62bc2e3057409a8866d1d89579c1e56f9c15fdee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_issue_requests_for_quotation`. The original RAPP
agent is preserved byte-for-byte in `dashboard_issue_requests_for_quotation_agent.py` and in the RCI capsule.

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

Issue requests for quotation Interactive HTML Dashboard — Pulls issue requests for quotation data from Dynamics 365 F&SCM for a given legal entity and fiscal period and returns a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) saved to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation
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
      "description": "Name of the HTML file to write, e.g. dashboard-issue-requests-for-quotation-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder the HTML file is saved to, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_requests_for_quotation_agent.py` and embedded as the fenced Python below (sha256 8ca78b24cc9bec59…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_requests_for_quotation_agent.py` first:

```bash
python3 dashboard_issue_requests_for_quotation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_issue_requests_for_quotation_agent.py   # or on stdin
python3 dashboard_issue_requests_for_quotation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for quotation Interactive HTML Dashboard — Pulls issue requests for quotation data from Dynamics 365 F&SCM for a given legal entity and fiscal period and returns a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) saved to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_issue_requests_for_quotation',
    "version": '3.0.3',
    "display_name": 'Issue requests for quotation Interactive HTML Dashboard',
    "description": 'Pulls issue requests for quotation data from Dynamics 365 F&SCM for a given legal entity and fiscal period and returns a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) saved to the out',
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
        "upstream_slug": 'dashboard-issue-requests-for-quotation',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-issue-requests-for-quotation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e73fd4ae5dd71f60',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-quotation'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-issue-requests-for-quotation', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-issue-requests-for-quotation-2026-05-24.html.', 'output_folder': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of issue requests for quotation with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull issue requests for quotation data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-issue-requests-for-quotation-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing issue requests for quotation.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls issue requests for quotation data from Dynamics 365 F&SCM for a given legal entity and fiscal period and returns a standalone interactive HTML dashboard file (charts, sortable table, RAG indicator) saved to the out', 'example_request': 'Build an HTML dashboard of issue requests for quotation in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-issue-requests-for-quotation-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser dashboard of issue requests for quotation from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIssueRequestsForQuotation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIssueRequestsForQuotation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-issue-requests-for-quotation-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardIssueRequestsForQuotation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
