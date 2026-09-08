---
name: "rar-cowork-cookbook-demo-data-migrate-to-new-versions-of-software"
description: "Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_migrate_to_new_versions_of_software", "rar_sha256": "d7facdf8523ba5f4ad60f5375fd353a180e5ae4c6b34da591b9cc22df389b3cf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_migrate_to_new_versions_of_software`. The original RAPP
agent is preserved byte-for-byte in `demo_data_migrate_to_new_versions_of_software_agent.py` and in the RCI capsule.

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

Migrate to new versions of software Demo Data Generator — Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software
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
      "description": "Sandbox D365 legal entity to write into (default USMF); must not be production.",
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
    "scenario": {
      "description": "The demo topic/scope, here: migrate to new versions of software.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_migrate_to_new_versions_of_software_agent.py` and embedded as the fenced Python below (sha256 d7facdf8523ba5f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_migrate_to_new_versions_of_software_agent.py` first:

```bash
python3 demo_data_migrate_to_new_versions_of_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_migrate_to_new_versions_of_software_agent.py   # or on stdin
python3 demo_data_migrate_to_new_versions_of_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Migrate to new versions of software Demo Data Generator — Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_migrate_to_new_versions_of_software',
    "version": '3.0.3',
    "display_name": 'Migrate to new versions of software Demo Data Generator',
    "description": "Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-migrate-to-new-versions-of-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc3e7311aee0b567',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/migrate-to-new-versions-of-software'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-migrate-to-new-versions-of-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'scenario': 'The demo topic/scope, here: migrate to new versions of software.', 'workbook_name': 'Excel staging file name, e.g. demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic migrate to new versions of software data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for migrate to new versions of software. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic migrate to new versions of software records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for software-version migration in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo records for software version migration in sandbox USMF, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx.', 'name': 'workbook_name'}, {'description': 'The demo topic/scope, here: migrate to new versions of software.', 'name': 'scenario'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need sandbox-only demo/training data for a migrate-to-new-software-versions scenario in Dynamics 365 F&SCM. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMigrateToNewVersionsOfSoftware(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMigrateToNewVersionsOfSoftware'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'scenario': {'description': 'The demo topic/scope, here: migrate to new versions of software.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-migrate-to-new-versions-of-software-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMigrateToNewVersionsOfSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
