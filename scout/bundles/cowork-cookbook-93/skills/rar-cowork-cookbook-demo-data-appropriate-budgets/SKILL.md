---
name: "rar-cowork-cookbook-demo-data-appropriate-budgets"
description: "Generates 25 realistic demo records for appropriate budgets in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_appropriate_budgets", "rar_sha256": "e972cfac9e4391491afad761c5bf609f017da630c317e7499b0f57a7c7810de2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
