---
name: "rar-cowork-cookbook-demo-data-delete-users"
description: "Generates 25 realistic demo 'delete users' records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_delete_users", "rar_sha256": "2a9992c073aa9c7b1d1801dc82c707852f4a06e9ba84734bf3dd6d219efa3c85", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_delete_users`. The original RAPP
agent is preserved byte-for-byte in `demo_data_delete_users_agent.py` and in the RCI capsule.

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

Delete users Demo Data Generator — Generates 25 realistic demo 'delete users' records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-delete-users
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-delete-users-2026-05-24.xlsx', saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_delete_users_agent.py` and embedded as the fenced Python below (sha256 2a9992c073aa9c7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_delete_users_agent.py` first:

```bash
python3 demo_data_delete_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_delete_users_agent.py   # or on stdin
python3 demo_data_delete_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Delete users Demo Data Generator — Generates 25 realistic demo 'delete users' records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-delete-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_delete_users',
    "version": '3.0.3',
    "display_name": 'Delete users Demo Data Generator',
    "description": "Generates 25 realistic demo 'delete users' records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-delete-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-delete-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e51fe4fdefe8d883',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/delete-users'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-delete-users', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': "Excel staging file name, e.g. 'demo-data-delete-users-2026-05-24.xlsx', saved to Documents/Cowork/output/."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic delete users data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for delete users. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-delete-users-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic delete users records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo 'delete users' records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo delete-user records in the USMF sandbox, stage them in Excel first, then create them and list the keys.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-delete-users-2026-05-24.xlsx', saved to Documents/Cowork/output/.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for delete users in a D365 sandbox legal entity (default USMF). Sandbox only — never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDeleteUsers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDeleteUsers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-delete-users-2026-05-24.xlsx', saved to Documents/Cowork/output/.", 'type': 'string'}},
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
    print(DemoDataDeleteUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
