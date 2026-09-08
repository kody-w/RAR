---
name: "rar-cowork-cookbook-demo-data-manage-financial-risks"
description: "Generates 25 realistic demo records for manage financial risks in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_financial_risks", "rar_sha256": "3dd7486e3f0a8ea46b573e9c9f4306b41184859d7e212bfb014f9a6b9ed8b649", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
