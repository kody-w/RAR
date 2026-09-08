---
name: "rar-cowork-cookbook-dashboard-approve-budgets"
description: "Pulls approve budgets data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the ERP plugin and saves a standalone interactive HTML dashboard to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_approve_budgets", "rar_sha256": "37f22e6e06f17611d0ef264e0d0d686cabbf8ce9dc91a2930f9bba27d8279d65", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
