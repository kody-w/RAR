---
name: "rar-cowork-cookbook-dashboard-dispose-of-obsolete-inventory"
description: "Pulls obsolete-inventory disposal data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard, read-only, to the output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_dispose_of_obsolete_inventory", "rar_sha256": "c27dbb8d30bafd7cd1974a00b98a5e98b65f2604fddb1c24b300d4da2f923cb6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
