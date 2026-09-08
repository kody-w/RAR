---
name: "rar-cowork-cookbook-demo-data-define-implementation-strategy"
description: "Generates 25 realistic demo records for define implementation strategy in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_implementation_strategy", "rar_sha256": "972fc947da6244c772b3b1b724257620cbd3c58826da6e6e8769846681c03302", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
