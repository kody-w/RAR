---
name: "rar-cowork-cookbook-dashboard-develop-order-management-policies"
description: "Pulls order management policy data from Dynamics 365 ERP for a legal entity's most recent fiscal period and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_order_management_policies", "rar_sha256": "e04231b5d10336dbb71c51835bf910f1684217fc77668b32f60731358235f531", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
