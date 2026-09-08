---
name: "rar-cowork-cookbook-dashboard-define-customer-order-requirements"
description: "Pulls customer order requirements data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_customer_order_requirements", "rar_sha256": "52e845a5c76ab1e3af7b68daa104979add1956221cde46c61a94a160155ed3f4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
