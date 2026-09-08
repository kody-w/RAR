---
name: "rar-cowork-cookbook-demo-data-develop-support-transition-strategy"
description: "Generates 25 realistic demo records for a develop-support-transition-strategy scenario in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_support_transition_strategy", "rar_sha256": "a0ae25467b5d923243c14863d393057150930e04fbd3bae07f65611f308239c2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_support_transition_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_support_transition_strategy_agent.py` and in the RCI capsule.

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

Develop support transition strategy Demo Data Generator — Generates 25 realistic demo records for a develop-support-transition-strategy scenario in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy
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
      "description": "Excel staging file name, e.g. demo-data-develop-support-transition-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_support_transition_strategy_agent.py` and embedded as the fenced Python below (sha256 a0ae25467b5d9232…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_support_transition_strategy_agent.py` first:

```bash
python3 demo_data_develop_support_transition_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_support_transition_strategy_agent.py   # or on stdin
python3 demo_data_develop_support_transition_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop support transition strategy Demo Data Generator — Generates 25 realistic demo records for a develop-support-transition-strategy scenario in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_support_transition_strategy',
    "version": '3.0.3',
    "display_name": 'Develop support transition strategy Demo Data Generator',
    "description": "Generates 25 realistic demo records for a develop-support-transition-strategy scenario in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-support-transition-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-support-transition-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a2208d0a15a3027',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/develop-support-transition-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-develop-support-transition-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-support-transition-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop support transition strategy data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop support transition strategy. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-support-transition-strategy-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop support transition strategy records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for a develop-support-transition-strategy scenario in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key.", 'example_request': 'Generate 25 demo records for develop support transition strategy in USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-support-transition-strategy-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo/training data for develop support transition strategy in a sandbox D365 legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopSupportTransitionStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopSupportTransitionStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-support-transition-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopSupportTransitionStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
