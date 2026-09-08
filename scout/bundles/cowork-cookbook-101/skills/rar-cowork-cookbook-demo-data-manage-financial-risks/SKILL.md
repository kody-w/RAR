---
name: "rar-cowork-cookbook-demo-data-manage-financial-risks"
description: "Generates 25 realistic demo records for manage financial risks in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_financial_risks", "rar_sha256": "3dd7486e3f0a8ea46b573e9c9f4306b41184859d7e212bfb014f9a6b9ed8b649", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_financial_risks`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_financial_risks_agent.py` and in the RCI capsule.

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

Manage financial risks Demo Data Generator — Generates 25 realistic demo records for manage financial risks in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-financial-risks
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
      "description": "Excel staging file name, e.g. demo-data-manage-financial-risks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_financial_risks_agent.py` and embedded as the fenced Python below (sha256 3dd7486e3f0a8ea4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_financial_risks_agent.py` first:

```bash
python3 demo_data_manage_financial_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_financial_risks_agent.py   # or on stdin
python3 demo_data_manage_financial_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage financial risks Demo Data Generator — Generates 25 realistic demo records for manage financial risks in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-financial-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_financial_risks',
    "version": '3.0.3',
    "display_name": 'Manage financial risks Demo Data Generator',
    "description": "Generates 25 realistic demo records for manage financial risks in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-financial-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-financial-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f405ee74aa612e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/manage-financial-risks'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-manage-financial-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-financial-risks-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage financial risks data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage financial risks. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-financial-risks-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage financial risks records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for manage financial risks in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo manage-financial-risks records in sandbox USMF, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-financial-risks-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for manage financial risks in a sandbox D365 legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageFinancialRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageFinancialRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-financial-risks-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageFinancialRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
