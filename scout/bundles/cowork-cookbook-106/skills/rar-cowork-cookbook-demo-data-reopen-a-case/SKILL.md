---
name: "rar-cowork-cookbook-demo-data-reopen-a-case"
description: "Generates 25 realistic demo 'reopen a case' records in a sandbox D365 F&SCM legal entity, stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_reopen_a_case", "rar_sha256": "68ac01ce6a915a431046836077b6351c2010ef6a90885d45f7c21cb8db302c27", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
