---
name: "rar-cowork-cookbook-demo-data-define-costing-policies"
description: "Generates 25 realistic demo records for define costing policies in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_costing_policies", "rar_sha256": "ea7d33e6a25bc1e47a1e88418f363e348f47688c76c720434081f9b3171e0692", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
