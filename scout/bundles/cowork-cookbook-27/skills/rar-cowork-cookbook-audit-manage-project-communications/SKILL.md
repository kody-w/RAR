---
name: "rar-cowork-cookbook-audit-manage-project-communications"
description: "Runs a read-only completeness and policy audit of manage project communications records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_project_communications", "rar_sha256": "8ec2ed9e54fb1065363262ca3958a576d8bbb7b5da091aac3b7567c2e1bce043", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_project_communications`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_project_communications_agent.py` and in the RCI capsule.

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

Manage project communications Completeness Audit — Runs a read-only completeness and policy audit of manage project communications records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-project-communications
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
      "description": "Name of the Excel workbook to produce, e.g. audit-manage-project-communications-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_project_communications_agent.py` and embedded as the fenced Python below (sha256 8ec2ed9e54fb1065…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_project_communications_agent.py` first:

```bash
python3 audit_manage_project_communications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_project_communications_agent.py   # or on stdin
python3 audit_manage_project_communications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project communications Completeness Audit — Runs a read-only completeness and policy audit of manage project communications records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-project-communications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_project_communications',
    "version": '3.0.3',
    "display_name": 'Manage project communications Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of manage project communications records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet',
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
        "upstream_slug": 'audit-manage-project-communications',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-project-communications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c56396bd888d8b50',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-communications'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-manage-project-communications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-manage-project-communications-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage project communications records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage project communications. Output an Excel workbook 'audit-manage-project-communications-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage project communications data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage project communications records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of manage project communications records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet', 'example_request': 'Audit manage project communications records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-project-communications-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants manage project communications records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageProjectCommunications(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageProjectCommunications'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-project-communications-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageProjectCommunications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
