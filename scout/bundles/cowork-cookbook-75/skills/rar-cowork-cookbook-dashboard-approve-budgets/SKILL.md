---
name: "rar-cowork-cookbook-dashboard-approve-budgets"
description: "Pulls approve budgets data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_approve_budgets", "rar_sha256": "37f22e6e06f17611d0ef264e0d0d686cabbf8ce9dc91a2930f9bba27d8279d65", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_approve_budgets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_approve_budgets_agent.py` and in the RCI capsule.

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

Approve budgets Interactive HTML Dashboard — Pulls approve budgets data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-approve-budgets
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-approve-budgets-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated file, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_approve_budgets_agent.py` and embedded as the fenced Python below (sha256 37f22e6e06f17611…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_approve_budgets_agent.py` first:

```bash
python3 dashboard_approve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_approve_budgets_agent.py   # or on stdin
python3 dashboard_approve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Approve budgets Interactive HTML Dashboard — Pulls approve budgets data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-approve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_approve_budgets',
    "version": '3.0.3',
    "display_name": 'Approve budgets Interactive HTML Dashboard',
    "description": 'Pulls approve budgets data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-approve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-approve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7964a83ca6cc353a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/approve-budgets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-approve-budgets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-approve-budgets-2026-05-24.html.', 'output_folder': 'Destination folder for the generated file, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of approve budgets with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull approve budgets data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-approve-budgets-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing approve budgets.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls approve budgets data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of approve budgets for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-approve-budgets-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated file, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable approve budgets dashboard from D365 that someone without D365 access can open.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardApproveBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardApproveBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-approve-budgets-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated file, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardApproveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
