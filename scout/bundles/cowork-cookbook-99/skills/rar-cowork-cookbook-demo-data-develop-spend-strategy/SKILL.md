---
name: "rar-cowork-cookbook-demo-data-develop-spend-strategy"
description: "Generates 25 realistic demo records for develop spend strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_spend_strategy", "rar_sha256": "73d263d5f304d4ed847f0a426afed756d96946f6b26a0dbcad37a2d96bb2f91b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
