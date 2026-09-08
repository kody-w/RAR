---
name: "rar-cowork-cookbook-dashboard-record-cost-of-quality"
description: "Pulls record cost of quality data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_cost_of_quality", "rar_sha256": "818a58496d6b74042546f1bb663ebf340716dba9d0933e96dd9d7ab27d5b0a3a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_record_cost_of_quality`. The original RAPP
agent is preserved byte-for-byte in `dashboard_record_cost_of_quality_agent.py` and in the RCI capsule.

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

Record cost of quality Interactive HTML Dashboard — Pulls record cost of quality data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-record-cost-of-quality
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
      "description": "Name of the HTML file to write, e.g. dashboard-record-cost-of-quality-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_record_cost_of_quality_agent.py` and embedded as the fenced Python below (sha256 818a58496d6b7404…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_record_cost_of_quality_agent.py` first:

```bash
python3 dashboard_record_cost_of_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_record_cost_of_quality_agent.py   # or on stdin
python3 dashboard_record_cost_of_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record cost of quality Interactive HTML Dashboard — Pulls record cost of quality data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-record-cost-of-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_record_cost_of_quality',
    "version": '3.0.3',
    "display_name": 'Record cost of quality Interactive HTML Dashboard',
    "description": 'Pulls record cost of quality data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-record-cost-of-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-record-cost-of-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8ade323c78d4ad38',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/record-cost-of-quality'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-record-cost-of-quality', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-record-cost-of-quality-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of record cost of quality with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull record cost of quality data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-record-cost-of-quality-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing record cost of quality.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls record cost of quality data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o', 'example_request': 'Build me an interactive HTML dashboard of record cost of quality for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-record-cost-of-quality-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable cost of quality dashboard from D365 that recipients can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRecordCostOfQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRecordCostOfQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-record-cost-of-quality-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardRecordCostOfQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
