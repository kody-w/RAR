---
name: "rar-cowork-cookbook-demo-data-record-employee-time"
description: "Generates 25 realistic demo employee time records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_employee_time", "rar_sha256": "1759998a313fde087319d4900950234af2fcaef9993b5363b2b42c3ce8d64ad2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
