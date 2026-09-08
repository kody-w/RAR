---
name: "rar-cowork-cookbook-demo-data-refine-the-training-program"
description: "Generates 25 realistic demo records for refining the training program in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_refine_the_training_program", "rar_sha256": "d6fb7b15d537f5672e95cd224d37eac24b155ab7c15a2c7e883ee1e11c6f4e64", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
