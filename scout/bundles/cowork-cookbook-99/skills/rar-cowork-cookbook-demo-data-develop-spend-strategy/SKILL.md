---
name: "rar-cowork-cookbook-demo-data-develop-spend-strategy"
description: "Generates 25 realistic demo records for develop spend strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_spend_strategy", "rar_sha256": "73d263d5f304d4ed847f0a426afed756d96946f6b26a0dbcad37a2d96bb2f91b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_spend_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_spend_strategy_agent.py` and in the RCI capsule.

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

Develop spend strategy Demo Data Generator — Generates 25 realistic demo records for develop spend strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-spend-strategy
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF. Production entities are not allowed.",
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
      "description": "How many demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-develop-spend-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_spend_strategy_agent.py` and embedded as the fenced Python below (sha256 73d263d5f304d4ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_spend_strategy_agent.py` first:

```bash
python3 demo_data_develop_spend_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_spend_strategy_agent.py   # or on stdin
python3 demo_data_develop_spend_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop spend strategy Demo Data Generator — Generates 25 realistic demo records for develop spend strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-spend-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_spend_strategy',
    "version": '3.0.3',
    "display_name": 'Develop spend strategy Demo Data Generator',
    "description": "Generates 25 realistic demo records for develop spend strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-spend-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-spend-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '852b6f4c5a2b0eb5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-spend-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-develop-spend-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF. Production entities are not allowed.', 'record_count': 'How many demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-spend-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop spend strategy data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop spend strategy. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-spend-strategy-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop spend strategy records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for develop spend strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo develop-spend-strategy records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Production entities are not allowed.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-spend-strategy-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for develop spend strategy created in a sandbox D365 legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopSpendStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSpendStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Production entities are not allowed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-spend-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopSpendStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
