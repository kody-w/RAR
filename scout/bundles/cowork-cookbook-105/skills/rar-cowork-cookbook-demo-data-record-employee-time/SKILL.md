---
name: "rar-cowork-cookbook-demo-data-record-employee-time"
description: "Generates 25 realistic demo employee time records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_employee_time", "rar_sha256": "1759998a313fde087319d4900950234af2fcaef9993b5363b2b42c3ce8d64ad2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_record_employee_time`. The original RAPP
agent is preserved byte-for-byte in `demo_data_record_employee_time_agent.py` and in the RCI capsule.

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

Record employee time Demo Data Generator — Generates 25 realistic demo employee time records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-employee-time
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
      "description": "Sandbox D365 legal entity to target (default USMF).",
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
      "description": "Number of demo time records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-record-employee-time-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_employee_time_agent.py` and embedded as the fenced Python below (sha256 1759998a313fde08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_employee_time_agent.py` first:

```bash
python3 demo_data_record_employee_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_record_employee_time_agent.py   # or on stdin
python3 demo_data_record_employee_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee time Demo Data Generator — Generates 25 realistic demo employee time records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-employee-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_record_employee_time',
    "version": '3.0.3',
    "display_name": 'Record employee time Demo Data Generator',
    "description": "Generates 25 realistic demo employee time records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-record-employee-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-record-employee-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf64231179f18dd3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-time'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-record-employee-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo time records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-record-employee-time-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic record employee time data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for record employee time. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-record-employee-time-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic record employee time records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo employee time records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo employee time records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo time records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-record-employee-time-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training employee time entries in a D365 sandbox legal entity. Sandbox only — never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataRecordEmployeeTime(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecordEmployeeTime'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo time records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-record-employee-time-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataRecordEmployeeTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
