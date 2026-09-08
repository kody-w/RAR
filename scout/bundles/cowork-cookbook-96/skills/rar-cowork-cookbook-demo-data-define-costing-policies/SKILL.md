---
name: "rar-cowork-cookbook-demo-data-define-costing-policies"
description: "Generates 25 realistic demo records for define costing policies in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_costing_policies", "rar_sha256": "ea7d33e6a25bc1e47a1e88418f363e348f47688c76c720434081f9b3171e0692", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_costing_policies`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_costing_policies_agent.py` and in the RCI capsule.

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

Define costing policies Demo Data Generator — Generates 25 realistic demo records for define costing policies in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-costing-policies
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF.",
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
      "description": "Excel staging file name, e.g. demo-data-define-costing-policies-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_costing_policies_agent.py` and embedded as the fenced Python below (sha256 ea7d33e6a25bc1e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_costing_policies_agent.py` first:

```bash
python3 demo_data_define_costing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_costing_policies_agent.py   # or on stdin
python3 demo_data_define_costing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define costing policies Demo Data Generator — Generates 25 realistic demo records for define costing policies in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-costing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_costing_policies',
    "version": '3.0.3',
    "display_name": 'Define costing policies Demo Data Generator',
    "description": "Generates 25 realistic demo records for define costing policies in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-define-costing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-costing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e75b0b31f8d46b93',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-costing-policies'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-define-costing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-costing-policies-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define costing policies data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define costing policies. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-costing-policies-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define costing policies records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for define costing policies in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo define costing policies records in the USMF sandbox, stage them in Excel, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-costing-policies-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for define costing policies in a D365 F&SCM sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineCostingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineCostingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-costing-policies-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineCostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
