---
name: "rar-cowork-cookbook-demo-data-establish-compliance-policies-and-procedures"
description: "Generates 25 realistic demo compliance-policy records for a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_compliance_policies_and_procedures", "rar_sha256": "05a9db5d090c46054bd543c117593641d14f14f847f4ab67d3bfd13e5210cc6b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
