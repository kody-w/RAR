---
name: "rar-cowork-cookbook-demo-data-consolidate-and-eliminate-financials"
description: "Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_and_eliminate_financials", "rar_sha256": "08869653fbdd34907f4bf6fd4fd37ef3a35647190e27bac1ec90f4b5e21ceb90", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_consolidate_and_eliminate_financials`. The original RAPP
agent is preserved byte-for-byte in `demo_data_consolidate_and_eliminate_financials_agent.py` and in the RCI capsule.

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

Consolidate and eliminate financials Demo Data Generator — Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 08869653fbdd3490…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_and_eliminate_financials_agent.py` first:

```bash
python3 demo_data_consolidate_and_eliminate_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_consolidate_and_eliminate_financials_agent.py   # or on stdin
python3 demo_data_consolidate_and_eliminate_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate and eliminate financials Demo Data Generator — Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_consolidate_and_eliminate_financials',
    "version": '3.0.3',
    "display_name": 'Consolidate and eliminate financials Demo Data Generator',
    "description": "Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-consolidate-and-eliminate-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-consolidate-and-eliminate-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1463d78116e7fe7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/consolidate-and-eliminate-financials'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-consolidate-and-eliminate-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic consolidate and eliminate financials data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for consolidate and eliminate financials. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic consolidate and eliminate financials records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for consolidate-and-eliminate financials in a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each record's primary key.", 'example_request': 'Generate 25 demo consolidate-and-eliminate financial records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for consolidate-and-eliminate financials in a sandbox D365 F&SCM legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConsolidateAndEliminateFinancials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConsolidateAndEliminateFinancials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-consolidate-and-eliminate-financials-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConsolidateAndEliminateFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
