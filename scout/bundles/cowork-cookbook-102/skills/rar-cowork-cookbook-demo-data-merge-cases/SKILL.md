---
name: "rar-cowork-cookbook-demo-data-merge-cases"
description: "Generates 25 realistic demo merge-case records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_merge_cases", "rar_sha256": "abee098ff0d2eaa4e76991bfc1cad17220e62521db63fecf4547910fe9a6eeeb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_merge_cases`. The original RAPP
agent is preserved byte-for-byte in `demo_data_merge_cases_agent.py` and in the RCI capsule.

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

Merge cases Demo Data Generator — Generates 25 realistic demo merge-case records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-merge-cases
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
      "description": "Sandbox D365 legal entity to write to; defaults to USMF.",
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
      "description": "Number of demo merge-case records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-merge-cases-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_merge_cases_agent.py` and embedded as the fenced Python below (sha256 abee098ff0d2eaa4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_merge_cases_agent.py` first:

```bash
python3 demo_data_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_merge_cases_agent.py   # or on stdin
python3 demo_data_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Demo Data Generator — Generates 25 realistic demo merge-case records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_merge_cases',
    "version": '3.0.3',
    "display_name": 'Merge cases Demo Data Generator',
    "description": "Generates 25 realistic demo merge-case records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c427a668c6ace6a4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to; defaults to USMF.', 'record_count': 'Number of demo merge-case records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-merge-cases-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic merge cases data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for merge cases. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-merge-cases-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic merge cases records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo merge-case records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo merge cases in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Number of demo merge-case records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-merge-cases-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training merge-case data created in a D365 F&SCM sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMergeCases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMergeCases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo merge-case records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-merge-cases-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
