---
name: "rar-cowork-cookbook-dashboard-adjust-inventory-levels"
description: "Pulls adjust-inventory-levels data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_adjust_inventory_levels", "rar_sha256": "fa07cea45ee219bb8d763d2ddac07ef52d9a81da81978650a449ddb6caabfa2b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_adjust_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `dashboard_adjust_inventory_levels_agent.py` and in the RCI capsule.

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

Adjust inventory levels Interactive HTML Dashboard — Pulls adjust-inventory-levels data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels
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
      "description": "Name of the HTML file to write, e.g. dashboard-adjust-inventory-levels-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder the HTML file is saved to, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_adjust_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 fa07cea45ee219bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_adjust_inventory_levels_agent.py` first:

```bash
python3 dashboard_adjust_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_adjust_inventory_levels_agent.py   # or on stdin
python3 dashboard_adjust_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust inventory levels Interactive HTML Dashboard — Pulls adjust-inventory-levels data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_adjust_inventory_levels',
    "version": '3.0.3',
    "display_name": 'Adjust inventory levels Interactive HTML Dashboard',
    "description": 'Pulls adjust-inventory-levels data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-adjust-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '70acbce7534d464c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/adjust-inventory-levels'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-adjust-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-adjust-inventory-levels-2026-05-24.html.', 'output_folder': 'Folder the HTML file is saved to, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of adjust inventory levels with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull adjust inventory levels data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-adjust-inventory-levels-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing adjust inventory levels.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls adjust-inventory-levels data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard; read-only.', 'example_request': 'Build me an interactive HTML dashboard of inventory adjustments in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-adjust-inventory-levels-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder the HTML file is saved to, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 inventory adjustment data for someone without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardAdjustInventoryLevels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAdjustInventoryLevels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-adjust-inventory-levels-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder the HTML file is saved to, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardAdjustInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
