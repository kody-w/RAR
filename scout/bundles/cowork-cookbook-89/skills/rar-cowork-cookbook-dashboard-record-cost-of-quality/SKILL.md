---
name: "rar-cowork-cookbook-dashboard-record-cost-of-quality"
description: "Pulls record cost of quality data from Dynamics 365 F&SCM for a legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_cost_of_quality", "rar_sha256": "818a58496d6b74042546f1bb663ebf340716dba9d0933e96dd9d7ab27d5b0a3a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
