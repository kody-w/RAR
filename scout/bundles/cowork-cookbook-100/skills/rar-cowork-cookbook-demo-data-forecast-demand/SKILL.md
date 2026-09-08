---
name: "rar-cowork-cookbook-demo-data-forecast-demand"
description: "Generates 25 realistic forecast demand demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_forecast_demand", "rar_sha256": "1eb44b02926644add90df3bd670055ba3e30cd45c5573a19ea044c323b183dd3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPaWLblX6Hvi+jMfNgXITS6oiJaaEBCCAlNgNIZTs0Smic05Kv/3kdwr+3MyqxXL6I/NQ4bkM7Z815rH4vfXuyujYr65dOL5tv5YmenaRz59cLOvQVd9EWdgLciccDfhVvkbR07XVvUzcuHF89v3Dou27jIwfadn/u13frNAkYXtW+ncdPG7iIoat+1m3bh+dksE7wV4LZb1F4z31zYiwZcd4phwWwwdMH9b42WFqkf2unCz9u4HRc/en5gd2m7MDSJ++nDomntEKhpIz9bxDkQ4AG13oIdXD9dzBbPxn5YuMCI9rt1s/gPD79qv+3qvFn4thstcr9/s+eHZlHWcWbX4yLxx1fgoT/YWZn6zcunn3/58BKDzy+ffntxU7sBl14Y4Apjtzb35iLz8BBsS+08BPfLEUQ2B99LvwaeZuAS8GTx9u3Hxk+DD4v//M+kt+uw+enT53zx9vr8Mv9Ru3y2fdEWQDbwz7VL24lTEJHXBZX29th8dQTEECQmD1+fO79JKsrF3+d7Pz6VvIZ+++Pnl6KcMwXS9vnlpwVIweeXups/v85Syh9/ek2L3q9//OmbnKZzbr7bzsKA1a9f3r6/iQULvy2Ng8UXTWHpN10gNHHpA+Hf+Te/nqa/iXsLyZfn4h+L8sPizyXP/vwd2PssPQfI/XOxIAZg58vrrYjzH9901MXdz+3c9X/86a/EupHvJnPh/ltyf34KjnzbA9F6CwmozzkFvyyWb759lfnXaktQMP8TT8Dyd3VfA/VXsh+Z/YPoNM5BX7zn8k/F/dmG5d8XP/+lb/9qw4dF8Bl0SxrfQd05qf9p8dujRH7+wft28Ydf/gFE/7ditKKr3YeEL6Db4sBv2i9ffv6heVz+4Zeff+hKUMW+nX3p6vTPZP5ZXB96fhfBt1U//n4v0G/kSV70+eJrDy1+K8r/Vf/jdWECyPO+XW8+Lb7vxPm1XMxOvCt9huC7bmyArd/F8aeXfwDMyYE3nfu4DfDjP/5jIcVuXTRF0C40t+jaBUhwG2f+bLwexc0ifiAecADEtYlBYN/WgfqfMzxbXASLX/+P+wD3j+4buK9mYP4CkNT+8g7ZX56Q/evrQgcCizoO4xygskopyuccQHDezsrK2m/8+g4Ayhlb/yPY/HH+MCPur38p88tj+2s5/voA5PiJdCotzCjXdKn/Ovtzjvz8zXoXcJM/+G4HJKeFC8wIYgDMH4CfTZHeAUrOvjdJnKYLLwa6AEeNT7Dv8k+zsF9//dWxm+hz/oTlzeJJXs0KLPhqzuLjR+BPkMZh1H7OfTcqFj/89o8fFv+1+Fe7HsJnHQoghrfoAwv3mnxcgG7qMrAMJAakEkDFI/q//eMtqkAMoM0FyFUcxE+ymqs+8b33EGs89RFGsYXjzzFcABIq6hZg/SJuXxdCsPhqL1A635rZICoehFv6uefn7gik2sCdr5HMixaQbhs3wfhh0TX+Q+uvTm0/TMxAW9vtrwuJVgD3FCn4ZzbzsQhsLvIYhP9rATyvAyE1oM/tu4jXxXGuv0Vp13YZ1fabjsB+5mWm/bftQLg9c/DnfKZXfw7Voxme4QnnoQJMEc+UfpxzDqaQbC6h5l13+DZ4eAv9wZT157x5K3S79h/cDkwZF2EXezP8/+2tpJqo6FLvET9g6SzpLQveW1YeNcj9YX6ZSX8xs/7ibeCZ+bODoTWy+P9uApr9p3Y7ld1ROsss2KOuXp95mSfBOX/P4XE2cXbk0YPfxpR3KHpH5M95GoMiq8e/PVc+svm25olyXQ28UCn1IR+UEsjLLPdR6XPl1vXcI/bn/B36gTeLB86BZANYAG0zV+u7wvnuu6UR6P35+7cx4M3nOR6gmhdl56Rztnzfc2w3AVbVc7e+5RaUvT93bh/FIGLfezXnCMQLyF8AI2LQf4AeXr/C8fPuu+m/2/icduYtj0mwA81aPwQAO/zZwDlTfdwCzLLb5+AN/Pz0EALcyMp29t0B7QI8fV70a7/q4iZuZ2h8xtUvAR5/nN+fns5X/aEEHQKCBfqg7EB0H50zg0oGZhlgAyhS0EhZnD9L+C0ID4F2NsMAgNm3GnpKfFx+c8h/tNtMSu8bZ0fmPTPPLwJgOrgyfo8W+p+VCZCXzSseev9YaV+1zbJnxGwA6gGN73efA8Hrk9OfQ8PiXe6nfzrZ/Pg/O/w8WNr4fQF8WkRtWzafVqsns74T6yvAq9XT1uZBsh9nQvz4jgofn6jwO4FPXz8t/mdG/U7EW1N8WqxfoVdovnV4K6q3F4gB/XF7/YjMdz/nqv8NRoH6IgNVNWdsBKz+lfPelwDiC2uAT2DxkwObmTp7wNYP0Afh/5x/X+VzlwFOycO5Kpviu+5/kD+o+Ge2vnITuJW3QLc3D4ehPx/FHj3R+C+f8i5NP7zkoN7+1RFsJp5sruFmPrGBbgFDVhv7j28PSBja+ePvj7Dy44OdvgKUB/CTNt/X2RtdzHT5XTs8vQNeuUDDhwcONzO9Ae9m5XMr2U3ywPnZi3YsZ7Ofp7V5vnvA/JcnzP+zQdr3vPA7RgAo90T3r0wC8P33NPG3RdYB1pkD6jwAw3vOkX9qx9ch9J+NOINpYNbnFZ9mYvzwhj3gHRwcAMm8nwGA92+nssfROe/Agffn+fwxp+OxZf4A9oC3r5u+/jeC47/88id2Pb37Agg7/5OEHbvMAQUHcPlBqn9k2vfQAOPfS/dbjGD0pz+NxDt9fnmW2B9VPjl2JuAZLh9FPC/8sPBfw9fFX/b3RxiCsY8Q+hFGXoe0Gf5E9cNbgN6AA+fAfcvIt7gUj0PabCWIY/v8P4XfXkCd27POt0p/m/LBcgB2H5t51lkBFAAKwfdnv4J7//78/7axiWwwhoKda99BEAeCSRjDEMT2PBLygo3jYTgEoahjb/wN5HoI6qIovrHXpG9DCOJu4I2zJjaetwHynu3+ZZ7k4tkYlMQDiCThAFnDkAcyBCOeR2AE5qI4DNmkY6MOStrOt61JDAx7evj0aA7f16PIHIk3R397cTAErOSRRqCeL3q1XDsYjDva3lnWmF+gpy0jaoqaBVrirwPrcKyGXGMolBJwxYGON2x7stg0zsaDdT+GKkMpE6vILDHqeG4eTWu/iy3anTK1gWma3tdMucbSceli2YhMMZPCSUfhRKFq4SaIRNHA0/1gp8GyE019p3fz/dVdzBW0DZpoq+RF6S5zzkg5NkzLTSkYG76YTgq9KcqA48OldiD3LLZaBnbpK3kdo9JGKK+1MlxH0T6OImJHF6U0L0IRHFqM4IU1Z4CsHji5Qw2LpU8xe2auhoUS9O7aOccDaZdybp4pNSxqfccG2SBs0fFsWqgR3sot3Knj9n68rTvhIBBwUCOmuTnUzMnh6zXm5TiErfItLDa4H9xuq1GVgnUqsLYp0tKSu6B6fYwN3lbrTKYjHsmcpXDNizPhivFYFFqw63euowunILN2dSxds2x3ZSkzpLkGCSYkl3KcPet7S1Q0FiMPrIRPNH8ftsM2bvcqF1uwYKPJxbAqQabgTjq0Era8gDLmJlz16mW5STHHlFa0dvJrIon7nW8i3ZWjzbRTaEZcUSwd8/WRTXTRE9OOS/lkr5E8KRxRSrepcGD3Otqxxa2hlmv5rktEi1kRqsX6keV3I74rkpTJlC3UaDvxSPKSnvrd9oJaaCtGosMz4lFiVvu4LaG+W90OW440mYwo3UqMxcKvplR0lP311kU6icSKpQVSlJ1SWzUz0zhhhWuoUZKKOD+clgIfpbkYbKV0zIaShCZpAzG3IOoBU+SGvjLP++3Npm9U4quHQV8q5FbXiK3UIk1k3N0qNJgdbNCXc0vVJ/go0Bf8WJp3VVRvlZJUEVNzYme1kGmj1x2LC2cEEVe0sYfFBNUJSiVKGTGulyRcsfaKuuDaDhHS2Otjizk1y+naqLaCn9b3yKilZhQxi1d7TmGUE3GAwo2K1CpSxG5AiXeSDnYrLRBX5zVml6ROXJIGVjVoZaw4B9/wm0wmlgBphDukLKeldVeikrh1BL+fDqlhF8neko8TFRutej4c7JhWhEJEmpsE6129vqISFTOEauAHfGjoKaDscRCv0eq6TzYyJ06kxRrwWdTON/IIj4fRTDLK0izxXDR0XUq6dj2pozjeFMoTZDRXbptARn0a7bb4aV/2IXU9IBNn4J1FZiys5/SthAe/XFE7hT+vTKS0dgLUp9U1GZxMDdupPJmXidTHgsiDk3AIMtmLzJ023FHIGUNCoALTqAytHJl65SX8luYg69DnOUFMl5HKXa6MSMyw9mdpd2rvUnxT82Zz4HpufQZrKcOFt37IkljZ0cq9NbFSXa4BjkNMdRlIOozE/TGKRNjejF1xMiWlXW8bbqtOOA91BDF6tn2lb9wyXVo2bLlwmQVYSsQZPLmtQLRORJRN1avSFIoskhKmu299qFunLWclLBS7WwQo93AkNybUXrKGISrkSB63QRx460w5sOqwYdCMZVHrGiCm0jdqL4ZG0G23VoENOS4yg8ySHcUVLicunYxRt2HkJiwemW7onILhWmcFOAQk0t7O2OAAtUd/pBAJBVAnxnJxOh0UZamZPBPc10qEcnS5bfVJ36jr/CKub/IE3appzMKTd4L3aIIy0h3JSo5YAfReLpvl4OPcao9jZi30ZNQyy71UcIwmKYxHoGihSl2hr64CaquSUVq1Gh7h8tSycuoPa1rlG8HX2RUf7xGOGw7b6xLPaYdZQcm5PQmx2Kg7Lenzxm7iHekHm60xZs6Un65yqVI7xhGubuBxwkVLikPp8aIm14p1Nh2eExKJ2YgpiGknrPai1fdszdeehTP+XhjTc8hdDwce94xCrRRt0zoNNUCndhffrNbSiL6rzbA0HerYnndtJetpLSrrmsV8UWhK+7bBiaV8aXHXcE5J0zSDjm0Fk9yl59hYVS6k6S7O8ZV0W07tKEybIMYoZ+OfeUdXw36q5M1qcIIo0NEgQpbLZeoR5MogW3NTaQYiDdNqMJrQ2IKSDYWL1xOkqNBQct3F8MW4MkizOecdQjnsSDlLdGQqLEXi9cl2JsvUAOH1jgtfdhSeM3Js6AasI8yRJfZZFPTGVrZQ+gZjHKNW3HjX6SuAim25K2xzw9GasDpd0lLZRsJWuo60fiwlC+FLlroUS2x1a293az9MBky5Oyh0rfsG1a+3PX6MTX8zZOaywzxDNnqfokjpMIoVEnfitc31eptulS5n0ZYKL0R66/VbLooje9VM3O9ynGKvJFJqqhAFCIr2q968+/1GJjNviENvG/ex7PTFQah8Xu9AId/sehWnWxQXnd1W97jLvjSWyW1KEnmfprvjivIHRvbDO3cteDG67KqDKUFcaZz28qmJFKGxtjoAzX4FOy1oWlrrlDWwVuKumrjDTj5Tk7sITKsxGd+TjG4xl8UMSDOACaqfYoapxikgiEQ0glgImSVw2Ehs/wCV7Xp3k/te9PtQdNiOlS2Xk5NDvDVw1mhoJrWMTa2k0pVD9kQbQyaDCqDZKn99Z8KDHykqxKsWndQbRlyKqlEqeGgz1DWSfRurqlQ9O5VxEtoysU1M5FZ6ke0RaS/3tKQgGTjdXe/J5pCOOUVok2Jcrv3ePgtWI0JDiCYpLCzV6SyY/FjYqSFCZ3k4nfvIHYr1dZkETMAVW2UPL9uItDUrDpVM1LX8JoFRmqRWu6JKz8aeJAL0vIOJ/MieWqQunNxuO1/eXu3RkE/S+lLeNRPhz/CuW7OdlmzL4M4vcVnXDFf2YF0qYJ1aagAWDktozVKRh4eHU8UbNnYvjH2RFVmSnEr2SpNyFiGlIkGFsxYaAaJ2rRGTkgHBbZis3N1EGeYJwwJhLU20KN8O3GhAk8v58rLVmMYsSRAx87hdUmxUCtX9sitzgtkmyUBP447vVZE8AiTamyOXo8sldwqHJrfGs+BXHt0ixZ7g9pINbUqyMT3rLJ9Z8kQ1nVj58W3pHuOtvNleh9Iz0L3d85BO3pdKCacnx72dPKsnjCqnIcPDliOmllNa+NeBcKU0VZkEHk/enlNdkTSFzhzLVUAgQuk31x4q6XUrdBY0mX1RJVTKmzKn8ofqRHv6anOcCqqSthK8yXnTvgY+FvHjVKJr0j7mokezxQoxHG80hTN1oQtKheWOgXd3+QxJU6qeGCK81/VtaR0wdMPpURgqfmTCapuVgGEa8ZAbR3rIIJpU82uhnFSNUgb6dDRoardEMTkvY64Uj6K/8+4VAdEQVa4QV0TOI+yoDt0YxnKCwYAsYFappVh3EOKiKrRS31lKAe8Fwaohs8SvO8TI9QFZLS/OuJTzZPSXhL7hh/Gi3LH8puzSndkc9201WNnaO5v4wQhMFDA7cVH3SSmxGu7ut4YUk+ERR20XGowDnmUVn8WWi0VbPBzZ22havNfpIQcbWHjeqy5Yz1vcOhGLzDatSN8yS3iNMQSFGOceTN4bJ9a254KB+7PAcVN5POY39LK/I4pHG/pRyLhw3Om821fyOsQvfSyQEBPWPJfZis+HlXosuao+BwrBOSAXBtTd2qV/z2+bOxLgcn3m2qEU5B6+3SKEJAxlK6u5dBuqweHXVSnXFyxBOMw47CjBrO07dYLhnhIPPrW98W4EZnhU89RiN0odNByTMS/JvSunR89TwHAT4/IFJ3CF4/eUfewtPRxPR2FrZszVrHfhvjgKekXXhqfJm2XpqfeU80/aXtvdNu4YCSu+XK6CYAOnLnI/Xmh7G+WHqyGs99X6DvDbIFEjMWkZMs5XxtbWZBMeh9FtsiWNM1xtbitTtHc6WUh7TS2r1jwckvw01m6ZnuVSLApGoMHxYixQizaEHDUUfDguOT7tGeRQ9LpIYMPkqxvVgYY6OCpCyjeg+I6Ziw+ULW2TnVudygnFSFbUwvLCXPbK0UDvq33hTzQ4Zd1oXs1y7OqMbjImPUkMCHmtibLyOLOoRgxMKfvKgzG0Y3ZSf78oYgAFBUoc2cnKSThrseJ45YwBEeKEiVa4jOG7Ng33XrKC5LtoHtvSlg70arsVeaI3eHWnK6YWqae1w6Fi6tzHa+GuL+A86dOby0q53BhuW5IxVE69Spfe3RFOGMwQ7X0Ud1tyA7HnocM0MTktYWc3Fksw0waDm52xOG7HDVSjMZQdxjjVnK3GW9cl1yYSbA9m5RgteQsOUjdwGZwbeZB0YuRax6mmSHVVpgghJSSmwzvhTB6oA3U9ybe7dK2TDeFHVx9qU0/fsz5x3HABYE/Qi5ubELJEeDUOV1NtUUelu2ScioOFa8ExzRAvg3dlsOKxaY1cTO2Qo6w4ZcdV4Z3vY8nLmr3euX557Hy38LAIL8zi6PH73RYOMlWGjVQnGzmisdqnkOmW1gCndt6lpfjRP6DtGEHwbVxu46HdkBGp3ZtLcXEmlMXho493u/X62EzRFVqPGzC6yUYGMVN4h0cy31hZGxK6rMqt5w34Jc4144Lrst3VmzVLhwmRGUc/kzzIO23jaTKiNUC7S860EYGfauPItIaHqGTHycYq2gz3wre6+nBHlipv39cnw/Jk2rrspksi0BHBXtZKe+oxbN156f4gXgCH6eSBuYo2vNJypjo7lhNcVqZ8NL0VhvMVC5M95t9bD8M2mXK875pTIR16xI3q/pqO5O2K3Sgb0wOAfCtivyJMe4gyqw1q9LDiAypZHkmnRv3N5YZid5pKOTqgtS3OajJfdCwkc+7tgBX5jVydYMiX9/BOMv2k56TCsWPBH8LlVkrU0/VwuzGTZk1Xt7UtTpvMqauOcerIVYsocr+2jDPbrCL2YN5ves7lkgsj4UBenWEM8vt+e95UMe/SV3GSJ/F0YJ0tcSNlj4TT62gN8n7yevWIwOXmmLDONbAOu2qY1NUhQ3LF3F9wvzSvq1NmwDhS7aMJXR7OiY8nlbIuME27rN2VHTU+G9H7mFrtw62+D5EgkG25w48qokEjG8BwS57CuswQB7Qa2ZD2en3fNyYWVTm325Y3v2+r4669+zfznhzTnBd6dmXgYjKxOKGmUMvH3L3ReNPR2LM47MbeWpUAl0OpWo/0SSKuZRR4vi+eiXR/PK4FHjN6j73Kqm9Hx9A7Xk6ADGrHjHBBvV/iFIy/d/mQM7BFRQd02qRuWRvERJ5vA7Hy/T2a30u6OQuqcLF6czQmf5DdaSrIQa4yREd4YiqI6VBl/X1ymMyILSaYoKV0z32ZYhoHOVQhpuAc5I2gCW/OyQ2RhltLt9zLpWNTY22DymmZ8JJIwkh1vUPuAE+Xyylt0tZG0dpCKlaWlHoKt2Te63c1WkeeekEIdhylDV/mjLbxV6lgr8u6ZjKbyo+yRVa9bGXlfh3zxzN83pEstCXKVtQF6ez6OcP6l4Mh3y8r+9qd2LCKVwXe4QZ8Y5tQmdQlAIYk444Wc7I3slR02B7Lr/qYYOh1TVWbhvKvXq44tHoPMs9e2lPVlqCVkxMuSxtPVF13uVYUrzI3Mu/UMjvx0+BiptPhl2yQhbAi11WlgNPM5LUrcPrYGBpJroa15+db89J2RoUa3naD8Wyp50pJ10zPrSg8ta7xuMbyyEEbh4MEvD5XF1croOlSo0wch8Ton5by4AUd5q5JzBnQtAb8EJTUZncN90Z8vWF9qt0dxr85UcYKgxg48g1PpCnOl8s7Sx3OW1NcLjWHRSqIWambkx6vvO3J7O8hmRl7Pr+QZp9u81uuXtWltSNxLr00fjzqa3TY4325ziDnphJgHsEAvjjetdow5i2jy8v6bN+2loIWNXa4M/6qKdSGWusXrnLCnOX2OeWI+FZfGYy/2cLHdV+yTimOkhHcJtLrFd0ndzAXpKnecVttfXcuVkmW3SYVxEsgRixs9ZEY196mzeB05wcjnNTOMbOqXCeyc5y0IXnpCiu5LTeH68RVjLOXrFtQnNUQ78h9AqNYcgkOZx2cPPzWPu87Cbpny6PLsfZZV+zsvnY6GEIJYlrvHYy8HuXkzkK0d+4wPawkp/b0O9ooTFO2dhZpfrLxd7zchXBy9e/OAa5dpAwOPgCNnWWs6np/rpb6aldfInTEB7zoCXtVNoN0gytl3J4GEeX9WJ16WjMYbAMY/Q7dc0CPiMAvxaLvWA+jx+xS+7t9Dq8sLb/KbU80be4rsVa5o88P5oF0Sf7WISVT7/xiG19IBfWiQW9QvWWo1lELu2BNGIPbc7aSjt29gSUO59HQyCY8xQ82SUa+dQvbUdszRs9EbmbcbHRil/b22Hq5vqHrlXqDQmG7derscKLVq4USAn5QcnCQpE44OOdsnD2cO9Ol3KwYRlqy/l7PezQosDyu5Ra+X+nlYZn1535Y35aH6aScfS7AsPg+h8Sc4LbPbTBdLjd1oARlfdE1ZEKDVUET4foIzAYnBOt68bdBEKOJRBkQ4XtZh6N0FSFV1J2Lu3NUOoU/1DhgBP4aSG7QOrLnD5UZdsTOn6SsPOO3c7tu9Atz5w7EOGmNp2MZi3P8beNoEg9nZ8Xxj9i1tm/Bsq3iu3KPaF4L+sQWotOJMerL2EC9alIqS6yN84nD3I3H1z0iHuShbs/nJt4jWLhBPUlt9/DpXOUFInNb3yA02wjyS37AiUrw/Dt8hHWHPgYwvgLs0LRbMuAVpTtKLV6dUQUL3eKgbYbu7oGh4zTyvdA3kGxU8SHjr6wpn08y2bX2gJyDFYESu5TCm62aKwi0U6pYN5x9IGLmkBOa7A3T/cwkO3DYwnTy4twKe7Uld+0uVBGIpSjq739/+fAyP/x6ew773//Qa3508//sCdLzYc/7Dzkejxl92/v00PXp37Dllw8vtRvPljyeizVpF749TPrDU7GPf/lAb942Pn8t9f44+flkurXD+ffCL3HudU1bj1+aIn38cAPscLpm/qVhM/8Y1QXv3z8Z/Wr2HNl3w9viy9sT0ziff5Dhe7Hd+m9fw7fng2DvCPIQu82XDYZ+8etydvDtFwDAr80r9Api9n8B2/C7custAAA= -->
