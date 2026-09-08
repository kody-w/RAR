---
name: "rar-cowork-cookbook-demo-data-forecast-demand"
description: "Generates 25 realistic forecast demand demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_demand", "rar_sha256": "1eb44b02926644add90df3bd670055ba3e30cd45c5573a19ea044c323b183dd3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_forecast_demand`. The original RAPP
agent is preserved byte-for-byte in `demo_data_forecast_demand_agent.py` and in the RCI capsule.

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

Forecast demand Demo Data Generator — Generates 25 realistic forecast demand demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-demand
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
    "legal_entity": {
      "description": "Sandbox D365 legal entity to create records in (default USMF); must not be production.",
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
    "record_count": {
      "description": "Number of demo forecast demand records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-forecast-demand-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_forecast_demand_agent.py` and embedded as the fenced Python below (sha256 1eb44b02926644ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_forecast_demand_agent.py` first:

```bash
python3 demo_data_forecast_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_forecast_demand_agent.py   # or on stdin
python3 demo_data_forecast_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast demand Demo Data Generator — Generates 25 realistic forecast demand demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_forecast_demand',
    "version": '3.0.3',
    "display_name": 'Forecast demand Demo Data Generator',
    "description": "Generates 25 realistic forecast demand demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-forecast-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-forecast-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ab6d95fd076e758',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/forecast-demand'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-forecast-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'record_count': 'Number of demo forecast demand records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-forecast-demand-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic forecast demand data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for forecast demand. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-forecast-demand-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic forecast demand records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic forecast demand demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo forecast demand records in sandbox USMF, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo forecast demand records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-forecast-demand-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need sample forecast demand data in a sandbox D365 legal entity for training or pilot demos. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataForecastDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataForecastDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo forecast demand records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-forecast-demand-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataForecastDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
