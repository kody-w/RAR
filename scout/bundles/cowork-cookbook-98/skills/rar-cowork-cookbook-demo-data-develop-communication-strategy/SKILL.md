---
name: "rar-cowork-cookbook-demo-data-develop-communication-strategy"
description: "Generates 25 realistic demo records for develop communication strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_communication_strategy", "rar_sha256": "f8db59f3333e1534c8c116e6f6b8be2acc7ea9c5dcfd6bc87b9d4e7035dfaae0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
