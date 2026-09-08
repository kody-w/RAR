---
name: "rar-cowork-cookbook-demo-data-appropriate-budgets"
description: "Generates 25 realistic demo records for appropriate budgets in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_appropriate_budgets", "rar_sha256": "e972cfac9e4391491afad761c5bf609f017da630c317e7499b0f57a7c7810de2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_appropriate_budgets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_appropriate_budgets_agent.py` and in the RCI capsule.

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

Appropriate budgets Demo Data Generator — Generates 25 realistic demo records for appropriate budgets in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-appropriate-budgets
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
      "description": "Excel staging file name, e.g. demo-data-appropriate-budgets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_appropriate_budgets_agent.py` and embedded as the fenced Python below (sha256 e972cfac9e439149…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_appropriate_budgets_agent.py` first:

```bash
python3 demo_data_appropriate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_appropriate_budgets_agent.py   # or on stdin
python3 demo_data_appropriate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Appropriate budgets Demo Data Generator — Generates 25 realistic demo records for appropriate budgets in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-appropriate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_appropriate_budgets',
    "version": '3.0.3',
    "display_name": 'Appropriate budgets Demo Data Generator',
    "description": "Generates 25 realistic demo records for appropriate budgets in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-appropriate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-appropriate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f50f4cbed6c0d4c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/appropriate-budgets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-appropriate-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-appropriate-budgets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic appropriate budgets data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for appropriate budgets. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-appropriate-budgets-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic appropriate budgets records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for appropriate budgets in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo appropriate budgets records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-appropriate-budgets-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or pilot data for appropriate budgets in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAppropriateBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAppropriateBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-appropriate-budgets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAppropriateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
