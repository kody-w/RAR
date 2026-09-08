---
name: "rar-cowork-cookbook-dashboard-develop-new-products"
description: "Pulls develop-new-products data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_new_products", "rar_sha256": "eb041282f8487c9f4d3c5697e12e81ccb07c7c94fbed4a32937bb5c9f65db146", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_new_products`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_new_products_agent.py` and in the RCI capsule.

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

Develop new products Interactive HTML Dashboard — Pulls develop-new-products data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-new-products
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
      "description": "D365 legal entity to query; recipe default is USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-develop-new-products-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated file, default Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_new_products_agent.py` and embedded as the fenced Python below (sha256 eb041282f8487c9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_new_products_agent.py` first:

```bash
python3 dashboard_develop_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_new_products_agent.py   # or on stdin
python3 dashboard_develop_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new products Interactive HTML Dashboard — Pulls develop-new-products data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_new_products',
    "version": '3.0.3',
    "display_name": 'Develop new products Interactive HTML Dashboard',
    "description": 'Pulls develop-new-products data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
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
        "upstream_slug": 'dashboard-develop-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a7d8a4a2ee0f940b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/develop-new-products'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-develop-new-products', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; recipe default is USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-develop-new-products-2026-05-24.html.', 'output_folder': 'Destination folder for the generated file, default Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop new products with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop new products data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-new-products-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop new products.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls develop-new-products data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard for develop new products from USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; recipe default is USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-develop-new-products-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated file, default Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of develop new products D365 data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; recipe default is USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-develop-new-products-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated file, default Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardDevelopNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
