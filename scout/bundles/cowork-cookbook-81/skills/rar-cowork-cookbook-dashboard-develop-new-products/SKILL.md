---
name: "rar-cowork-cookbook-dashboard-develop-new-products"
description: "Pulls develop-new-products data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_new_products", "rar_sha256": "eb041282f8487c9f4d3c5697e12e81ccb07c7c94fbed4a32937bb5c9f65db146", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
