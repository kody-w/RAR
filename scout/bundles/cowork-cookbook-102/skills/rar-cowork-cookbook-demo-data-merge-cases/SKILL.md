---
name: "rar-cowork-cookbook-demo-data-merge-cases"
description: "Generates 25 realistic demo merge-case records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_merge_cases", "rar_sha256": "abee098ff0d2eaa4e76991bfc1cad17220e62521db63fecf4547910fe9a6eeeb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
