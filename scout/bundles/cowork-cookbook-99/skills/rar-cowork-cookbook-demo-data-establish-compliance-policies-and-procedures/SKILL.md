---
name: "rar-cowork-cookbook-demo-data-establish-compliance-policies-and-procedures"
description: "Generates 25 realistic demo compliance-policy records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures", "rar_sha256": "05a9db5d090c46054bd543c117593641d14f14f847f4ab67d3bfd13e5210cc6b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures`. The original RAPP
agent is preserved byte-for-byte in `demo_data_establish_compliance_policies_and_procedures_agent.py` and in the RCI capsule.

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

Establish compliance policies and procedures Demo Data Generator — Generates 25 realistic demo compliance-policy records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures
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
      "description": "Excel staging file name, e.g. demo-data-establish-compliance-policies-and-procedures-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_establish_compliance_policies_and_procedures_agent.py` and embedded as the fenced Python below (sha256 05a9db5d090c4605…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_establish_compliance_policies_and_procedures_agent.py` first:

```bash
python3 demo_data_establish_compliance_policies_and_procedures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_establish_compliance_policies_and_procedures_agent.py   # or on stdin
python3 demo_data_establish_compliance_policies_and_procedures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish compliance policies and procedures Demo Data Generator — Generates 25 realistic demo compliance-policy records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures',
    "version": '3.0.3',
    "display_name": 'Establish compliance policies and procedures Demo Data Generator',
    "description": "Generates 25 realistic demo compliance-policy records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-establish-compliance-policies-and-procedures',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-establish-compliance-policies-and-procedures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '26a624157c0e5db2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/establish-compliance-policies-and-procedures'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-establish-compliance-policies-and-procedures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-establish-compliance-policies-and-procedures-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic establish compliance policies and procedures data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for establish compliance policies and procedures. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-establish-compliance-policies-and-procedures-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic establish compliance policies and procedures records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo compliance-policy records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo compliance policy records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-establish-compliance-policies-and-procedures-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for establishing compliance policies and procedures in a D365 sandbox tenant. Sandbox only — never a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataEstablishCompliancePoliciesAndProcedures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataEstablishCompliancePoliciesAndProcedures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-establish-compliance-policies-and-procedures-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataEstablishCompliancePoliciesAndProcedures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
