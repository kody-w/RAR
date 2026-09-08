---
name: "rar-cowork-cookbook-demo-data-manage-data"
description: "Generates 25 realistic demo records for manage data in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_data", "rar_sha256": "9cd4633e5c4e4d7af667d1d28ddb1ddf2d086bb2d70c774c4afc2a113bdca4c2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_data`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_data_agent.py` and in the RCI capsule.

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

Manage data Demo Data Generator — Generates 25 realistic demo records for manage data in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-data
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. 'demo-data-manage-data-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_data_agent.py` and embedded as the fenced Python below (sha256 9cd4633e5c4e4d7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_data_agent.py` first:

```bash
python3 demo_data_manage_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_data_agent.py   # or on stdin
python3 demo_data_manage_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data Demo Data Generator — Generates 25 realistic demo records for manage data in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_data',
    "version": '3.0.3',
    "display_name": 'Manage data Demo Data Generator',
    "description": "Generates 25 realistic demo records for manage data in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bc4b8bb5b8623d47',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': "Excel staging file name, e.g. 'demo-data-manage-data-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage data data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage data. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-data-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage data records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for manage data in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo manage-data records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-manage-data-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data created in a D365 sandbox legal entity for pilots or demos — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-manage-data-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataManageData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
