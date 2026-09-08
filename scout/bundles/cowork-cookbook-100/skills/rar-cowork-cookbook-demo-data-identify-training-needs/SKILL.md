---
name: "rar-cowork-cookbook-demo-data-identify-training-needs"
description: "Generates 25 realistic demo records for identify training needs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_identify_training_needs", "rar_sha256": "8b9eb76de7deb31a442eb77e5015cf449d6310f2d07d74734aad6cee573d7b5a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_identify_training_needs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_identify_training_needs_agent.py` and in the RCI capsule.

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

Identify training needs Demo Data Generator — Generates 25 realistic demo records for identify training needs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-identify-training-needs
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
      "description": "Sandbox D365 legal entity to generate records in (default USMF).",
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
      "description": "Excel staging file name, e.g. 'demo-data-identify-training-needs-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 8b9eb76de7deb31a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_identify_training_needs_agent.py` first:

```bash
python3 demo_data_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_identify_training_needs_agent.py   # or on stdin
python3 demo_data_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Demo Data Generator — Generates 25 realistic demo records for identify training needs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_identify_training_needs',
    "version": '3.0.3',
    "display_name": 'Identify training needs Demo Data Generator',
    "description": "Generates 25 realistic demo records for identify training needs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c7d4b3cc95aea894',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to generate records in (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': "Excel staging file name, e.g. 'demo-data-identify-training-needs-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic identify training needs data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for identify training needs. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-identify-training-needs-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic identify training needs records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for identify training needs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo identify-training-needs records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-identify-training-needs-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need sandbox demo/pilot data for identify training needs in Dynamics 365 F&SCM. Sandbox only — never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataIdentifyTrainingNeeds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataIdentifyTrainingNeeds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-identify-training-needs-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
