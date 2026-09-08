---
name: "rar-cowork-cookbook-demo-data-forecast-cash-flow"
description: "Generates 25 realistic forecast cash flow demo records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_cash_flow", "rar_sha256": "5b64ff2ed69cd6952314f435c6d1815e8930769c8e3d642a6482f10a1fb888fe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
