---
name: "rar-cowork-cookbook-demo-data-refine-the-training-program"
description: "Generates 25 realistic demo records for refining the training program in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_refine_the_training_program", "rar_sha256": "d6fb7b15d537f5672e95cd224d37eac24b155ab7c15a2c7e883ee1e11c6f4e64", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_refine_the_training_program`. The original RAPP
agent is preserved byte-for-byte in `demo_data_refine_the_training_program_agent.py` and in the RCI capsule.

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

Refine the training program Demo Data Generator — Generates 25 realistic demo records for refining the training program in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-refine-the-training-program
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
      "description": "Sandbox D365 legal entity to write to (defaults to USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-refine-the-training-program-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_refine_the_training_program_agent.py` and embedded as the fenced Python below (sha256 d6fb7b15d537f567…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_refine_the_training_program_agent.py` first:

```bash
python3 demo_data_refine_the_training_program_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_refine_the_training_program_agent.py   # or on stdin
python3 demo_data_refine_the_training_program_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Refine the training program Demo Data Generator — Generates 25 realistic demo records for refining the training program in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-refine-the-training-program
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_refine_the_training_program',
    "version": '3.0.3',
    "display_name": 'Refine the training program Demo Data Generator',
    "description": "Generates 25 realistic demo records for refining the training program in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-refine-the-training-program',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-refine-the-training-program',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '03c6147c73924af6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/refine-the-training-program'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-refine-the-training-program', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (defaults to USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-refine-the-training-program-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic refine the training program data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for refine the training program. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-refine-the-training-program-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic refine the training program records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for refining the training program in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key", 'example_request': 'Generate 25 demo training program records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (defaults to USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-refine-the-training-program-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/pilot training-program data created in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataRefineTheTrainingProgram(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRefineTheTrainingProgram'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (defaults to USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-refine-the-training-program-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataRefineTheTrainingProgram().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
