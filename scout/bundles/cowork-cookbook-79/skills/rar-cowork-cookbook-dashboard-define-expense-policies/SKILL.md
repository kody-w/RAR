---
name: "rar-cowork-cookbook-dashboard-define-expense-policies"
description: "Pulls define expense policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_expense_policies", "rar_sha256": "a322a1375a1780f60aed0ed24fa7bfa13ea48813c66e9df59563f049a7908200", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_expense_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_expense_policies_agent.py` and in the RCI capsule.

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

Define expense policies Interactive HTML Dashboard — Pulls define expense policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-expense-policies
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
      "description": "Name of the HTML file to produce, e.g. dashboard-define-expense-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_expense_policies_agent.py` and embedded as the fenced Python below (sha256 a322a1375a1780f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_expense_policies_agent.py` first:

```bash
python3 dashboard_define_expense_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_expense_policies_agent.py   # or on stdin
python3 dashboard_define_expense_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define expense policies Interactive HTML Dashboard — Pulls define expense policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-expense-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_expense_policies',
    "version": '3.0.3',
    "display_name": 'Define expense policies Interactive HTML Dashboard',
    "description": 'Pulls define expense policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-expense-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-expense-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4dcd684c06621056',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-expense-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-expense-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-define-expense-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define expense policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define expense policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-expense-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define expense policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls define expense policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f', 'example_request': 'Build an interactive HTML dashboard of define expense policies from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-define-expense-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants define expense policies data from D365 rendered as a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineExpensePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineExpensePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-define-expense-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output).', 'type': 'string'}},
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
    print(DashboardDefineExpensePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
