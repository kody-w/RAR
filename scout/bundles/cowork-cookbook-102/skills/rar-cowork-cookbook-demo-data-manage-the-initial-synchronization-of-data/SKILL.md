---
name: "rar-cowork-cookbook-demo-data-manage-the-initial-synchronization-of-data"
description: "Generates 25 realistic demo records for initial data synchronization in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data", "rar_sha256": "b9d5646a3bbce7602049a7eb015a0c403e4e40df3493204f0cd6e3cef0d21e1d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_the_initial_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the initial synchronization of data Demo Data Generator — Generates 25 realistic demo records for initial data synchronization in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data
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
      "description": "Sandbox D365 legal entity to target (defaults to USMF).",
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
      "description": "Number of demo records to generate (defaults to 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-the-initial-synchronization-of-data-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_the_initial_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 b9d5646a3bbce760…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_the_initial_synchronization_of_data_agent.py` first:

```bash
python3 demo_data_manage_the_initial_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_the_initial_synchronization_of_data_agent.py   # or on stdin
python3 demo_data_manage_the_initial_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the initial synchronization of data Demo Data Generator — Generates 25 realistic demo records for initial data synchronization in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data',
    "version": '3.0.3',
    "display_name": 'Manage the initial synchronization of data Demo Data Generator',
    "description": "Generates 25 realistic demo records for initial data synchronization in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-the-initial-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fdd1e998388f8f09',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-initial-synchronization-of-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-the-initial-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (defaults to USMF).', 'record_count': 'Number of demo records to generate (defaults to 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-the-initial-synchronization-of-data-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage the initial synchronization of data data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage the initial synchronization of data. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-the-initial-synchronization-of-data-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage the initial synchronization of data records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for initial data synchronization in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo records for initial data synchronization in USMF sandbox, stage them in Excel, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (defaults to USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (defaults to 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-the-initial-synchronization-of-data-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/pilot data for initial data synchronization created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageTheInitialSynchronizationOfData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageTheInitialSynchronizationOfData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (defaults to USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (defaults to 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-the-initial-synchronization-of-data-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageTheInitialSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
