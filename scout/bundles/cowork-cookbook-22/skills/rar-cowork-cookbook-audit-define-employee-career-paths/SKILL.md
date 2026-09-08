---
name: "rar-cowork-cookbook-audit-define-employee-career-paths"
description: "Audits employee career path records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of count"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_employee_career_paths", "rar_sha256": "ba1d96022e5459f5febf20eff9339a0c94e6ec54fc3c20202de23b291d81ef23", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
