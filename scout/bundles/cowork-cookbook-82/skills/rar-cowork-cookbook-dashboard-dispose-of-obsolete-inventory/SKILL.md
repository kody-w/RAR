---
name: "rar-cowork-cookbook-dashboard-dispose-of-obsolete-inventory"
description: "Pulls obsolete-inventory disposal data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_dispose_of_obsolete_inventory", "rar_sha256": "c27dbb8d30bafd7cd1974a00b98a5e98b65f2604fddb1c24b300d4da2f923cb6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_dispose_of_obsolete_inventory`. The original RAPP
agent is preserved byte-for-byte in `dashboard_dispose_of_obsolete_inventory_agent.py` and in the RCI capsule.

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

Dispose of obsolete inventory Interactive HTML Dashboard — Pulls obsolete-inventory disposal data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-dispose-of-obsolete-inventory
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the generated HTML file, e.g. dashboard-dispose-of-obsolete-inventory-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_dispose_of_obsolete_inventory_agent.py` and embedded as the fenced Python below (sha256 c27dbb8d30bafd7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_dispose_of_obsolete_inventory_agent.py` first:

```bash
python3 dashboard_dispose_of_obsolete_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_dispose_of_obsolete_inventory_agent.py   # or on stdin
python3 dashboard_dispose_of_obsolete_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dispose of obsolete inventory Interactive HTML Dashboard — Pulls obsolete-inventory disposal data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-dispose-of-obsolete-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_dispose_of_obsolete_inventory',
    "version": '3.0.3',
    "display_name": 'Dispose of obsolete inventory Interactive HTML Dashboard',
    "description": 'Pulls obsolete-inventory disposal data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the output folder.',
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
        "upstream_slug": 'dashboard-dispose-of-obsolete-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-dispose-of-obsolete-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee1f891b664bd9bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/dispose-of-obsolete-inventory'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-dispose-of-obsolete-inventory', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-dispose-of-obsolete-inventory-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of dispose of obsolete inventory with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull dispose of obsolete inventory data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-dispose-of-obsolete-inventory-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing dispose of obsolete inventory.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls obsolete-inventory disposal data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the output folder.', 'example_request': 'Build me an interactive HTML dashboard of obsolete inventory disposal for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-dispose-of-obsolete-inventory-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of obsolete inventory slated for disposal, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDisposeOfObsoleteInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDisposeOfObsoleteInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-dispose-of-obsolete-inventory-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDisposeOfObsoleteInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
