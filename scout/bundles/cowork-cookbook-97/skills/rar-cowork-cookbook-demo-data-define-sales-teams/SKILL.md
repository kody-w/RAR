---
name: "rar-cowork-cookbook-demo-data-define-sales-teams"
description: "Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_sales_teams", "rar_sha256": "b13e53500d02bc88b56956f2813a81b6fb58ccdd5a18bb9d7e04f3eb02e7fff2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_sales_teams`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_sales_teams_agent.py` and in the RCI capsule.

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

Define sales teams Demo Data Generator — Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-sales-teams
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-define-sales-teams-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_sales_teams_agent.py` and embedded as the fenced Python below (sha256 b13e53500d02bc88…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_sales_teams_agent.py` first:

```bash
python3 demo_data_define_sales_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_sales_teams_agent.py   # or on stdin
python3 demo_data_define_sales_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales teams Demo Data Generator — Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-sales-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_sales_teams',
    "version": '3.0.3',
    "display_name": 'Define sales teams Demo Data Generator',
    "description": "Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-sales-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-sales-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf8dfdbc6571008e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-teams'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-define-sales-teams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-sales-teams-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define sales teams data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define sales teams. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-sales-teams-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define sales teams records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo sales-team records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo sales team records in sandbox USMF, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-sales-teams-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training sales-team data seeded into a sandbox D365 F&SCM legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineSalesTeams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineSalesTeams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-sales-teams-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineSalesTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
