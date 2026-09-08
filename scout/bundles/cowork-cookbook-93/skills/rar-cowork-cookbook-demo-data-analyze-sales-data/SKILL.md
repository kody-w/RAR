---
name: "rar-cowork-cookbook-demo-data-analyze-sales-data"
description: "Generates 25 realistic sales-analysis demo records against a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sales_data", "rar_sha256": "9f6266c2827f444797f975e9b45d5f386455456a5edfa44addec60e68fe8b5c0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
