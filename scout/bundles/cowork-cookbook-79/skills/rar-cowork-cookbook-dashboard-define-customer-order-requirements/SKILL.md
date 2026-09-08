---
name: "rar-cowork-cookbook-dashboard-define-customer-order-requirements"
description: "Pulls customer order requirements data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_customer_order_requirements", "rar_sha256": "52e845a5c76ab1e3af7b68daa104979add1956221cde46c61a94a160155ed3f4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_customer_order_requirements`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_customer_order_requirements_agent.py` and in the RCI capsule.

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

Define customer order requirements Interactive HTML Dashboard — Pulls customer order requirements data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-customer-order-requirements-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_customer_order_requirements_agent.py` and embedded as the fenced Python below (sha256 52e845a5c76ab1e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_customer_order_requirements_agent.py` first:

```bash
python3 dashboard_define_customer_order_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_customer_order_requirements_agent.py   # or on stdin
python3 dashboard_define_customer_order_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer order requirements Interactive HTML Dashboard — Pulls customer order requirements data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_customer_order_requirements',
    "version": '3.0.3',
    "display_name": 'Define customer order requirements Interactive HTML Dashboard',
    "description": 'Pulls customer order requirements data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu',
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
        "upstream_slug": 'dashboard-define-customer-order-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a499b5fe949ee7cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-customer-order-requirements'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-define-customer-order-requirements', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-customer-order-requirements-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define customer order requirements with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define customer order requirements data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-customer-order-requirements-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define customer order requirements.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls customer order requirements data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu', 'example_request': 'Build me an interactive HTML dashboard of customer order requirements for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-customer-order-requirements-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants customer order requirements from D365 packaged as a shareable browser dashboard for viewers who lack D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineCustomerOrderRequirements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCustomerOrderRequirements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-customer-order-requirements-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDefineCustomerOrderRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
