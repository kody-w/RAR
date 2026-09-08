---
name: "rar-cowork-cookbook-dashboard-adjust-inventory-levels"
description: "Pulls adjust-inventory-levels data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_adjust_inventory_levels", "rar_sha256": "fa07cea45ee219bb8d763d2ddac07ef52d9a81da81978650a449ddb6caabfa2b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
