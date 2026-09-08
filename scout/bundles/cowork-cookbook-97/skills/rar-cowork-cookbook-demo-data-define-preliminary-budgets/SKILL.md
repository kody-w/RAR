---
name: "rar-cowork-cookbook-demo-data-define-preliminary-budgets"
description: "Generates 25 realistic demo budget-planning records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_preliminary_budgets", "rar_sha256": "3fa580be4b5c48907901f5bc6720cbe2eab85d3a1d493f0add58837243109fce", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_preliminary_budgets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_preliminary_budgets_agent.py` and in the RCI capsule.

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

Define preliminary budgets Demo Data Generator — Generates 25 realistic demo budget-planning records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets
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
      "description": "Sandbox D365 legal entity to target (defaults to USMF); must not be production.",
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
      "description": "Number of demo records to generate (defaults to 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-define-preliminary-budgets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_preliminary_budgets_agent.py` and embedded as the fenced Python below (sha256 3fa580be4b5c4890…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_preliminary_budgets_agent.py` first:

```bash
python3 demo_data_define_preliminary_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_preliminary_budgets_agent.py   # or on stdin
python3 demo_data_define_preliminary_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define preliminary budgets Demo Data Generator — Generates 25 realistic demo budget-planning records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_preliminary_budgets',
    "version": '3.0.3',
    "display_name": 'Define preliminary budgets Demo Data Generator',
    "description": "Generates 25 realistic demo budget-planning records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-define-preliminary-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9c64756907a5cb17',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/define-preliminary-budgets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-define-preliminary-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (defaults to USMF); must not be production.', 'record_count': 'Number of demo records to generate (defaults to 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-preliminary-budgets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define preliminary budgets data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define preliminary budgets. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-preliminary-budgets-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define preliminary budgets records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo budget-planning records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo preliminary budget records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (defaults to USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (defaults to 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-preliminary-budgets-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': "Call when you need demo or training data for 'define preliminary budgets' in a sandbox D365 legal entity — never against production."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefinePreliminaryBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefinePreliminaryBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (defaults to USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (defaults to 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-preliminary-budgets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefinePreliminaryBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
