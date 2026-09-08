---
name: "rar-cowork-cookbook-demo-data-manage-the-initial-synchronization-of-data"
description: "Generates 25 realistic demo records for initial data synchronization in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data", "rar_sha256": "b9d5646a3bbce7602049a7eb015a0c403e4e40df3493204f0cd6e3cef0d21e1d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
