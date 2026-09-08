---
name: "rar-cowork-cookbook-dashboard-develop-order-management-policies"
description: "Pulls order management policy data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_order_management_policies", "rar_sha256": "e04231b5d10336dbb71c51835bf910f1684217fc77668b32f60731358235f531", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_order_management_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_order_management_policies_agent.py` and in the RCI capsule.

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

Develop order management policies Interactive HTML Dashboard — Pulls order management policy data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies
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
      "description": "Reporting period; defaults to the most recent fiscal period available.",
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
      "description": "Name of the HTML file to generate, e.g. dashboard-develop-order-management-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the saved HTML, typically Documents/Cowork/output.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_order_management_policies_agent.py` and embedded as the fenced Python below (sha256 e04231b5d10336db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_order_management_policies_agent.py` first:

```bash
python3 dashboard_develop_order_management_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_order_management_policies_agent.py   # or on stdin
python3 dashboard_develop_order_management_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop order management policies Interactive HTML Dashboard — Pulls order management policy data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_order_management_policies',
    "version": '3.0.3',
    "display_name": 'Develop order management policies Interactive HTML Dashboard',
    "description": "Pulls order management policy data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-order-management-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3b78861a0f512636',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-order-management-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-develop-order-management-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to generate, e.g. dashboard-develop-order-management-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the saved HTML, typically Documents/Cowork/output.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop order management policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop order management policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-order-management-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop order management policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Pulls order management policy data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;", 'example_request': 'Build an interactive HTML dashboard of order management policies for USMF from the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to generate, e.g. dashboard-develop-order-management-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the saved HTML, typically Documents/Cowork/output.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of D365 order management policies that recipients can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopOrderManagementPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopOrderManagementPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to generate, e.g. dashboard-develop-order-management-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the saved HTML, typically Documents/Cowork/output.', 'type': 'string'}},
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
    print(DashboardDevelopOrderManagementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
