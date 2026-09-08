---
name: "rar-cowork-cookbook-audit-refine-the-training-program"
description: "Runs a read-only completeness and policy audit of training program records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_refine_the_training_program", "rar_sha256": "7fcedbf6ed35cc169597726ec280891f5023c3f665648813a73e1ed0141abe02", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_refine_the_training_program`. The original RAPP
agent is preserved byte-for-byte in `audit_refine_the_training_program_agent.py` and in the RCI capsule.

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

Refine the training program Completeness Audit — Runs a read-only completeness and policy audit of training program records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-refine-the-training-program
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
    "date_window": {
      "description": "Date range used to judge stale dates; adjust for demo data (USMF is mostly FY2017).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. audit-refine-the-training-program-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_refine_the_training_program_agent.py` and embedded as the fenced Python below (sha256 7fcedbf6ed35cc16…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_refine_the_training_program_agent.py` first:

```bash
python3 audit_refine_the_training_program_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_refine_the_training_program_agent.py   # or on stdin
python3 audit_refine_the_training_program_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Refine the training program Completeness Audit — Runs a read-only completeness and policy audit of training program records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-refine-the-training-program
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_refine_the_training_program',
    "version": '3.0.3',
    "display_name": 'Refine the training program Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of training program records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-refine-the-training-program',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-refine-the-training-program',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '56e63ff970ae27a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/refine-the-training-program'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-refine-the-training-program', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data (USMF is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-refine-the-training-program-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit refine the training program records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to refine the training program. Output an Excel workbook 'audit-refine-the-training-program-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no refine the training program data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Reads refine the training program records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of training program records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit the training program records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data (USMF is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-refine-the-training-program-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants training program records in D365 checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditRefineTheTrainingProgram(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRefineTheTrainingProgram'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data (USMF is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-refine-the-training-program-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditRefineTheTrainingProgram().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
