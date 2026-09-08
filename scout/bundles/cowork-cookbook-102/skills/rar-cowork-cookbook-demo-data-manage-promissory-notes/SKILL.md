---
name: "rar-cowork-cookbook-demo-data-manage-promissory-notes"
description: "Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_promissory_notes", "rar_sha256": "6c4cad3bb1e8bbc2d6d5ebb2fc6d7616e25263a5165e92cbed8ceadc911d4469", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_promissory_notes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_promissory_notes_agent.py` and in the RCI capsule.

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

Manage promissory notes Demo Data Generator — Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF.",
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
      "description": "How many demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-promissory-notes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_promissory_notes_agent.py` and embedded as the fenced Python below (sha256 6c4cad3bb1e8bbc2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_promissory_notes_agent.py` first:

```bash
python3 demo_data_manage_promissory_notes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_promissory_notes_agent.py   # or on stdin
python3 demo_data_manage_promissory_notes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage promissory notes Demo Data Generator — Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_promissory_notes',
    "version": '3.0.3',
    "display_name": 'Manage promissory notes Demo Data Generator',
    "description": "Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-promissory-notes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-promissory-notes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b39d924d46d77c07',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/manage-promissory-notes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-manage-promissory-notes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'record_count': 'How many demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-promissory-notes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage promissory notes data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage promissory notes. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-promissory-notes-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage promissory notes records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic promissory note demo records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo promissory note records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-promissory-notes-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or pilot promissory note data seeded in a sandbox D365 legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManagePromissoryNotes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManagePromissoryNotes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-promissory-notes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManagePromissoryNotes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
