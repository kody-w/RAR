---
name: "rar-cowork-cookbook-demo-data-write-off-bad-debt"
description: "Generates 25 realistic write-off bad debt demo records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_write_off_bad_debt", "rar_sha256": "7670e787ca0c9756be403945fcc299824e9144f9c7ae0e8db95e60e5bb920bfa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
