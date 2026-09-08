---
name: "rar-cowork-cookbook-demo-data-process-project-change-requests"
description: "Generates 25 realistic demo project change request records against a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prim"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_project_change_requests", "rar_sha256": "1c04540b45e173016874f0ae7794037345abf70ae50d8aee139a81e7220dad67", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
