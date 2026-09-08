---
name: "rar-cowork-cookbook-demo-data-reopen-a-case"
description: "Generates 25 realistic demo 'reopen a case' records in a sandbox D365 F&SCM legal entity, stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_reopen_a_case", "rar_sha256": "68ac01ce6a915a431046836077b6351c2010ef6a90885d45f7c21cb8db302c27", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_reopen_a_case`. The original RAPP
agent is preserved byte-for-byte in `demo_data_reopen_a_case_agent.py` and in the RCI capsule.

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

Reopen a case Demo Data Generator — Generates 25 realistic demo 'reopen a case' records in a sandbox D365 F&SCM legal entity, stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-reopen-a-case
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-reopen-a-case-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_reopen_a_case_agent.py` and embedded as the fenced Python below (sha256 68ac01ce6a915a43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_reopen_a_case_agent.py` first:

```bash
python3 demo_data_reopen_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_reopen_a_case_agent.py   # or on stdin
python3 demo_data_reopen_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reopen a case Demo Data Generator — Generates 25 realistic demo 'reopen a case' records in a sandbox D365 F&SCM legal entity, stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-reopen-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_reopen_a_case',
    "version": '3.0.3',
    "display_name": 'Reopen a case Demo Data Generator',
    "description": "Generates 25 realistic demo 'reopen a case' records in a sandbox D365 F&SCM legal entity, stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-reopen-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-reopen-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '10c3ff675ba53bfa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/reopen-a-case'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-reopen-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-reopen-a-case-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic reopen a case data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for reopen a case. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-reopen-a-case-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic reopen a case records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo 'reopen a case' records in a sandbox D365 F&SCM legal entity, stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo reopen-a-case records in sandbox USMF, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-reopen-a-case-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo data for reopen-a-case training or pilot scenarios in a sandbox tenant — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataReopenACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReopenACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-reopen-a-case-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataReopenACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
