---
name: "rar-cowork-cookbook-audit-process-project-change-requests"
description: "Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_project_change_requests", "rar_sha256": "f41ea840ed18647a826316e1937ea2505c49150da16f5aec230a3f076ebcceda", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_project_change_requests`. The original RAPP
agent is preserved byte-for-byte in `audit_process_project_change_requests_agent.py` and in the RCI capsule.

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

Process project change requests Completeness Audit — Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-project-change-requests
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-process-project-change-requests-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_project_change_requests_agent.py` and embedded as the fenced Python below (sha256 f41ea840ed18647a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_project_change_requests_agent.py` first:

```bash
python3 audit_process_project_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_project_change_requests_agent.py   # or on stdin
python3 audit_process_project_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process project change requests Completeness Audit — Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-project-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_project_change_requests',
    "version": '3.0.3',
    "display_name": 'Process project change requests Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-project-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-project-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5a37476854b9583',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/process-project-change-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-process-project-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-process-project-change-requests-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit process project change requests records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to process project change requests. Output an Excel workbook 'audit-process-project-change-requests-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no process project change requests data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process project change requests records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of project change request records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou', 'example_request': 'Audit project change requests in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-process-project-change-requests-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants project change request records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProcessProjectChangeRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessProjectChangeRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-process-project-change-requests-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProcessProjectChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
