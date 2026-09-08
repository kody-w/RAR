---
name: "rar-cowork-cookbook-dashboard-define-product-policies"
description: "Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_product_policies", "rar_sha256": "723362df79a243334eecd97b5826d981832976c8f6f827542108fdb7d9efaf38", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_product_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_product_policies_agent.py` and in the RCI capsule.

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

Define product policies Interactive HTML Dashboard — Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-product-policies
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-product-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 723362df79a24333…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_product_policies_agent.py` first:

```bash
python3 dashboard_define_product_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_product_policies_agent.py   # or on stdin
python3 dashboard_define_product_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product policies Interactive HTML Dashboard — Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-product-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_product_policies',
    "version": '3.0.3',
    "display_name": 'Define product policies Interactive HTML Dashboard',
    "description": 'Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-product-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-product-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6f160fde228b570',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-define-product-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-product-policies-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define product policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define product policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-product-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define product policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls define product policies data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;', 'example_request': 'Build me an interactive HTML dashboard of define product policies for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-product-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants define product policies data from D365 packaged as a browser-openable HTML dashboard that viewers can read without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineProductPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineProductPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-product-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardDefineProductPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
