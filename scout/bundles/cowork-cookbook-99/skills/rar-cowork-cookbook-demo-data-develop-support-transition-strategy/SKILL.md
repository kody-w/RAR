---
name: "rar-cowork-cookbook-demo-data-develop-support-transition-strategy"
description: "Generates 25 realistic demo records for a develop-support-transition-strategy scenario in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_support_transition_strategy", "rar_sha256": "a0ae25467b5d923243c14863d393057150930e04fbd3bae07f65611f308239c2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
