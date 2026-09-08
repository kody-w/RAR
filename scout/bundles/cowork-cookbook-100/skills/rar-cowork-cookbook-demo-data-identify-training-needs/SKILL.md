---
name: "rar-cowork-cookbook-demo-data-identify-training-needs"
description: "Generates 25 realistic demo records for identify training needs in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_identify_training_needs", "rar_sha256": "8b9eb76de7deb31a442eb77e5015cf449d6310f2d07d74734aad6cee573d7b5a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
