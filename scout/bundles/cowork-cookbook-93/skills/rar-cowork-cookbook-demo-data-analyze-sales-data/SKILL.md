---
name: "rar-cowork-cookbook-demo-data-analyze-sales-data"
description: "Generates 25 realistic sales-analysis demo records against a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sales_data", "rar_sha256": "9f6266c2827f444797f975e9b45d5f386455456a5edfa44addec60e68fe8b5c0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_sales_data`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_sales_data_agent.py` and in the RCI capsule.

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

Analyze sales data Demo Data Generator — Generates 25 realistic sales-analysis demo records against a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sales-data
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-analyze-sales-data-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_sales_data_agent.py` and embedded as the fenced Python below (sha256 9f6266c2827f4447…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_sales_data_agent.py` first:

```bash
python3 demo_data_analyze_sales_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_sales_data_agent.py   # or on stdin
python3 demo_data_analyze_sales_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sales data Demo Data Generator — Generates 25 realistic sales-analysis demo records against a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sales-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_sales_data',
    "version": '3.0.3',
    "display_name": 'Analyze sales data Demo Data Generator',
    "description": "Generates 25 realistic sales-analysis demo records against a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-sales-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-sales-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78929d17074d526a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-analyze-sales-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-analyze-sales-data-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic analyze sales data data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for analyze sales data. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-analyze-sales-data-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic analyze sales data records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic sales-analysis demo records against a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo sales records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-analyze-sales-data-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training sales data created in a sandbox D365 legal entity; never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAnalyzeSalesData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeSalesData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-analyze-sales-data-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAnalyzeSalesData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
