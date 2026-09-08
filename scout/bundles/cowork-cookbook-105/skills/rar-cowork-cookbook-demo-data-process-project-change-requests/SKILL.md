---
name: "rar-cowork-cookbook-demo-data-process-project-change-requests"
description: "Generates 25 realistic demo project change request records against a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prim"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_project_change_requests", "rar_sha256": "1c04540b45e173016874f0ae7794037345abf70ae50d8aee139a81e7220dad67", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_process_project_change_requests`. The original RAPP
agent is preserved byte-for-byte in `demo_data_process_project_change_requests_agent.py` and in the RCI capsule.

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

Process project change requests Demo Data Generator — Generates 25 realistic demo project change request records against a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prim

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-process-project-change-requests
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Number of demo change request records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-process-project-change-requests-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_process_project_change_requests_agent.py` and embedded as the fenced Python below (sha256 1c04540b45e17301…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_process_project_change_requests_agent.py` first:

```bash
python3 demo_data_process_project_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_process_project_change_requests_agent.py   # or on stdin
python3 demo_data_process_project_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process project change requests Demo Data Generator — Generates 25 realistic demo project change request records against a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prim

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-process-project-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_process_project_change_requests',
    "version": '3.0.3',
    "display_name": 'Process project change requests Demo Data Generator',
    "description": "Generates 25 realistic demo project change request records against a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prim",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-process-project-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-process-project-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '460d9f9241126729',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/process-project-change-requests'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-process-project-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo change request records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-process-project-change-requests-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic process project change requests data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for process project change requests. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-process-project-change-requests-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic process project change requests records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo project change request records against a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prim", 'example_request': 'Generate 25 demo project change requests in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo change request records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-process-project-change-requests-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo project change request data in a D365 sandbox for training or pilot scenarios. Sandbox only — never a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataProcessProjectChangeRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataProcessProjectChangeRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo change request records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-process-project-change-requests-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataProcessProjectChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
