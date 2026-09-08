---
name: "rar-cowork-cookbook-demo-data-recognize-employees"
description: "Generates 25 realistic employee-recognition demo records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_recognize_employees", "rar_sha256": "9c64b6620956d3cfea51f537131dd09699e6d4b2236d5bd45fa575654da2396d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
