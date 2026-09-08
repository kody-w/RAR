---
name: "rar-cowork-cookbook-demo-data-define-implementation-strategy"
description: "Generates 25 realistic demo records for define implementation strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_implementation_strategy", "rar_sha256": "972fc947da6244c772b3b1b724257620cbd3c58826da6e6e8769846681c03302", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_implementation_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_implementation_strategy_agent.py` and in the RCI capsule.

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

Define implementation strategy Demo Data Generator — Generates 25 realistic demo records for define implementation strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-implementation-strategy
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
      "description": "Excel staging file name, e.g. demo-data-define-implementation-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_implementation_strategy_agent.py` and embedded as the fenced Python below (sha256 972fc947da6244c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_implementation_strategy_agent.py` first:

```bash
python3 demo_data_define_implementation_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_implementation_strategy_agent.py   # or on stdin
python3 demo_data_define_implementation_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define implementation strategy Demo Data Generator — Generates 25 realistic demo records for define implementation strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-implementation-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_implementation_strategy',
    "version": '3.0.3',
    "display_name": 'Define implementation strategy Demo Data Generator',
    "description": "Generates 25 realistic demo records for define implementation strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-define-implementation-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-implementation-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '88508bb6c1c13f7c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-implementation-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-define-implementation-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-implementation-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define implementation strategy data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define implementation strategy. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-implementation-strategy-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define implementation strategy records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for define implementation strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo records for define implementation strategy in USMF sandbox, stage them in Excel, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-implementation-strategy-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for define implementation strategy in a D365 sandbox legal entity. Sandbox only — never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineImplementationStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineImplementationStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-implementation-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineImplementationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
