---
name: "rar-cowork-cookbook-audit-manage-project-communications"
description: "Runs a read-only completeness and policy audit of manage project communications records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_project_communications", "rar_sha256": "8ec2ed9e54fb1065363262ca3958a576d8bbb7b5da091aac3b7567c2e1bce043", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
