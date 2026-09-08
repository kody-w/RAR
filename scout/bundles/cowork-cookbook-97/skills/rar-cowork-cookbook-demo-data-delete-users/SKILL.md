---
name: "rar-cowork-cookbook-demo-data-delete-users"
description: "Generates 25 realistic demo 'delete users' records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_delete_users", "rar_sha256": "2a9992c073aa9c7b1d1801dc82c707852f4a06e9ba84734bf3dd6d219efa3c85", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
