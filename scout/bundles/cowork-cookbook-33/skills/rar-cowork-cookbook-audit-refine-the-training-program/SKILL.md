---
name: "rar-cowork-cookbook-audit-refine-the-training-program"
description: "Runs a read-only completeness and policy audit of training program records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_refine_the_training_program", "rar_sha256": "7fcedbf6ed35cc169597726ec280891f5023c3f665648813a73e1ed0141abe02", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
