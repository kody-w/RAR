---
name: "rar-cowork-cookbook-demo-data-forecast-cash-flow"
description: "Generates 25 realistic forecast cash flow demo records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_cash_flow", "rar_sha256": "5b64ff2ed69cd6952314f435c6d1815e8930769c8e3d642a6482f10a1fb888fe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_forecast_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `demo_data_forecast_cash_flow_agent.py` and in the RCI capsule.

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

Forecast cash flow Demo Data Generator — Generates 25 realistic forecast cash flow demo records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow
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
      "description": "Sandbox D365 legal entity to write into (default USMF); must not be production.",
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
      "description": "Number of demo forecast cash flow records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-forecast-cash-flow-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 5b64ff2ed69cd695…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_forecast_cash_flow_agent.py` first:

```bash
python3 demo_data_forecast_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_forecast_cash_flow_agent.py   # or on stdin
python3 demo_data_forecast_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast cash flow Demo Data Generator — Generates 25 realistic forecast cash flow demo records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_forecast_cash_flow',
    "version": '3.0.3',
    "display_name": 'Forecast cash flow Demo Data Generator',
    "description": "Generates 25 realistic forecast cash flow demo records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-forecast-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-forecast-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e973af84362a4b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/forecast-cash-flow'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-forecast-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'record_count': 'Number of demo forecast cash flow records to generate (default 25).', 'workbook_name': "Excel staging file name, e.g. 'demo-data-forecast-cash-flow-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic forecast cash flow data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for forecast cash flow. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-forecast-cash-flow-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic forecast cash flow records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic forecast cash flow demo records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo forecast cash flow records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo forecast cash flow records to generate (default 25).', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-forecast-cash-flow-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training forecast cash flow data seeded in a D365 F&SCM sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataForecastCashFlow(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataForecastCashFlow'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo forecast cash flow records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-forecast-cash-flow-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataForecastCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
