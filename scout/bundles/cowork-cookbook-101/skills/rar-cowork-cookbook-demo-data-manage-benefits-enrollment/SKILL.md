---
name: "rar-cowork-cookbook-demo-data-manage-benefits-enrollment"
description: "Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_benefits_enrollment", "rar_sha256": "bdd023f1f38de5e9c6edfe45189cae4060e6d173cb3c18196a52b7effe2684cf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_benefits_enrollment`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_benefits_enrollment_agent.py` and in the RCI capsule.

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

Manage benefits enrollment Demo Data Generator — Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-benefits-enrollment-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_benefits_enrollment_agent.py` and embedded as the fenced Python below (sha256 bdd023f1f38de5e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_benefits_enrollment_agent.py` first:

```bash
python3 demo_data_manage_benefits_enrollment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_benefits_enrollment_agent.py   # or on stdin
python3 demo_data_manage_benefits_enrollment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage benefits enrollment Demo Data Generator — Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_benefits_enrollment',
    "version": '3.0.3',
    "display_name": 'Manage benefits enrollment Demo Data Generator',
    "description": "Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-benefits-enrollment',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a132d15468021f8c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-benefits-enrollment'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-manage-benefits-enrollment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-benefits-enrollment-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage benefits enrollment data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage benefits enrollment. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-benefits-enrollment-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage benefits enrollment records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo benefits enrollment records in USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-benefits-enrollment-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for benefits enrollment in a D365 sandbox tenant; never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageBenefitsEnrollment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageBenefitsEnrollment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-benefits-enrollment-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageBenefitsEnrollment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
