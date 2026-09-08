---
name: "rar-cowork-cookbook-demo-data-define-preliminary-budgets"
description: "Generates 25 realistic demo budget-planning records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_preliminary_budgets", "rar_sha256": "3fa580be4b5c48907901f5bc6720cbe2eab85d3a1d493f0add58837243109fce", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
