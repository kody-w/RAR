---
name: "rar-cowork-cookbook-demo-data-write-off-bad-debt"
description: "Generates 25 realistic write-off bad debt demo records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_write_off_bad_debt", "rar_sha256": "7670e787ca0c9756be403945fcc299824e9144f9c7ae0e8db95e60e5bb920bfa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_write_off_bad_debt`. The original RAPP
agent is preserved byte-for-byte in `demo_data_write_off_bad_debt_agent.py` and in the RCI capsule.

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

Write off bad debt Demo Data Generator — Generates 25 realistic write-off bad debt demo records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-write-off-bad-debt-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_write_off_bad_debt_agent.py` and embedded as the fenced Python below (sha256 7670e787ca0c9756…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_write_off_bad_debt_agent.py` first:

```bash
python3 demo_data_write_off_bad_debt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_write_off_bad_debt_agent.py   # or on stdin
python3 demo_data_write_off_bad_debt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Write off bad debt Demo Data Generator — Generates 25 realistic write-off bad debt demo records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_write_off_bad_debt',
    "version": '3.0.3',
    "display_name": 'Write off bad debt Demo Data Generator',
    "description": "Generates 25 realistic write-off bad debt demo records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-write-off-bad-debt',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-write-off-bad-debt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4a6b20fd142c7ea2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/write-off-bad-debt'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-write-off-bad-debt', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to generate records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-write-off-bad-debt-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic write off bad debt data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for write off bad debt. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-write-off-bad-debt-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic write off bad debt records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic write-off bad debt demo records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 write off bad debt demo records in sandbox USMF, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-write-off-bad-debt-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or training data for write off bad debt in a sandbox D365 F&SCM legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataWriteOffBadDebt(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataWriteOffBadDebt'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-write-off-bad-debt-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataWriteOffBadDebt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
