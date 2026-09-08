---
name: "rar-cowork-cookbook-demo-data-develop-communication-strategy"
description: "Generates 25 realistic demo records for develop communication strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_communication_strategy", "rar_sha256": "f8db59f3333e1534c8c116e6f6b8be2acc7ea9c5dcfd6bc87b9d4e7035dfaae0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_communication_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_communication_strategy_agent.py` and in the RCI capsule.

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

Develop communication strategy Demo Data Generator — Generates 25 realistic demo records for develop communication strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy
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
      "description": "Excel staging file name, e.g. demo-data-develop-communication-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_communication_strategy_agent.py` and embedded as the fenced Python below (sha256 f8db59f3333e1534…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_communication_strategy_agent.py` first:

```bash
python3 demo_data_develop_communication_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_communication_strategy_agent.py   # or on stdin
python3 demo_data_develop_communication_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop communication strategy Demo Data Generator — Generates 25 realistic demo records for develop communication strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_communication_strategy',
    "version": '3.0.3',
    "display_name": 'Develop communication strategy Demo Data Generator',
    "description": "Generates 25 realistic demo records for develop communication strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, then returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-communication-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-communication-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '976ed2c5eeed9f2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-communication-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-develop-communication-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-communication-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop communication strategy data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop communication strategy. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-communication-strategy-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop communication strategy records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for develop communication strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo records for develop communication strategy in USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-communication-strategy-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for develop communication strategy created in a sandbox D365 legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopCommunicationStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopCommunicationStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-communication-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopCommunicationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
