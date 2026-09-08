---
name: "rar-cowork-cookbook-audit-define-employee-career-paths"
description: "Audits employee career path records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of count"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_employee_career_paths", "rar_sha256": "ba1d96022e5459f5febf20eff9339a0c94e6ec54fc3c20202de23b291d81ef23", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_employee_career_paths`. The original RAPP
agent is preserved byte-for-byte in `audit_define_employee_career_paths_agent.py` and in the RCI capsule.

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

Define employee career paths Completeness Audit — Audits employee career path records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of count

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-employee-career-paths
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
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-employee-career-paths-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_employee_career_paths_agent.py` and embedded as the fenced Python below (sha256 ba1d96022e5459f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_employee_career_paths_agent.py` first:

```bash
python3 audit_define_employee_career_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_employee_career_paths_agent.py   # or on stdin
python3 audit_define_employee_career_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define employee career paths Completeness Audit — Audits employee career path records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of count

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-employee-career-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_employee_career_paths',
    "version": '3.0.2',
    "display_name": 'Define employee career paths Completeness Audit',
    "description": 'Audits employee career path records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of count',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-employee-career-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-employee-career-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb9e081d966b58a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-employee-career-paths'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-define-employee-career-paths', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-employee-career-paths-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define employee career paths records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define employee career paths. Output an Excel workbook 'audit-define-employee-career-paths-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define employee career paths data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define employee career paths records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits employee career path records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of count', 'example_request': 'Audit define employee career paths in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-employee-career-paths-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of define employee career paths data in D365 ERP via the Cowork plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineEmployeeCareerPaths(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineEmployeeCareerPaths'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-employee-career-paths-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineEmployeeCareerPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
