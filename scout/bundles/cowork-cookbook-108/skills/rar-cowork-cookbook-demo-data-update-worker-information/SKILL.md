---
name: "rar-cowork-cookbook-demo-data-update-worker-information"
description: "Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_update_worker_information", "rar_sha256": "1a50502eed61218738293dac7ac91e99147f82e72b0a941140e5c1fe3954a8ea", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_update_worker_information`. The original RAPP
agent is preserved byte-for-byte in `demo_data_update_worker_information_agent.py` and in the RCI capsule.

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

Update worker information Demo Data Generator — Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-update-worker-information
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must not be production.",
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
      "description": "Number of demo records to generate; recipe default is 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-update-worker-information-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 1a50502eed612187…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_update_worker_information_agent.py` first:

```bash
python3 demo_data_update_worker_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_update_worker_information_agent.py   # or on stdin
python3 demo_data_update_worker_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update worker information Demo Data Generator — Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-update-worker-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_update_worker_information',
    "version": '3.0.3',
    "display_name": 'Update worker information Demo Data Generator',
    "description": "Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-update-worker-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-update-worker-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aaa48a0f1a3f3bea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/update-worker-information'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-update-worker-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; recipe default is 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-update-worker-information-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic update worker information data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for update worker information. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-update-worker-information-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic update worker information records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo worker information update records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; recipe default is 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-update-worker-information-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training worker update data in a D365 sandbox legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataUpdateWorkerInformation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataUpdateWorkerInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; recipe default is 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-update-worker-information-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataUpdateWorkerInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
