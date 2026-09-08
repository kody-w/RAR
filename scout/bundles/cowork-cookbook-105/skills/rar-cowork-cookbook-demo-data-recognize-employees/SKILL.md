---
name: "rar-cowork-cookbook-demo-data-recognize-employees"
description: "Generates 25 realistic employee-recognition demo records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_recognize_employees", "rar_sha256": "9c64b6620956d3cfea51f537131dd09699e6d4b2236d5bd45fa575654da2396d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_recognize_employees`. The original RAPP
agent is preserved byte-for-byte in `demo_data_recognize_employees_agent.py` and in the RCI capsule.

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

Recognize employees Demo Data Generator — Generates 25 realistic employee-recognition demo records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-recognize-employees
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
      "description": "Excel staging file name, e.g. demo-data-recognize-employees-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_recognize_employees_agent.py` and embedded as the fenced Python below (sha256 9c64b6620956d3cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_recognize_employees_agent.py` first:

```bash
python3 demo_data_recognize_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_recognize_employees_agent.py   # or on stdin
python3 demo_data_recognize_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize employees Demo Data Generator — Generates 25 realistic employee-recognition demo records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-recognize-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_recognize_employees',
    "version": '3.0.3',
    "display_name": 'Recognize employees Demo Data Generator',
    "description": "Generates 25 realistic employee-recognition demo records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-recognize-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-recognize-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bba5f96641301415',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/recognize-employees'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-recognize-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (defaults to USMF); must not be production.', 'record_count': 'Number of demo records to generate (defaults to 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-recognize-employees-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic recognize employees data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for recognize employees. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-recognize-employees-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic recognize employees records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic employee-recognition demo records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo employee recognition records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (defaults to USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (defaults to 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-recognize-employees-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for employee recognition in a D365 F&SCM sandbox — never against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataRecognizeEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecognizeEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (defaults to USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (defaults to 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-recognize-employees-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataRecognizeEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
