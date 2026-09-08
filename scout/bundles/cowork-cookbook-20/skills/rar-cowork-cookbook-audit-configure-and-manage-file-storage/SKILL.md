---
name: "rar-cowork-cookbook-audit-configure-and-manage-file-storage"
description: "Runs a read-only completeness and policy audit of file storage configuration records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_file_storage", "rar_sha256": "aa4f22d801281095cf22ee6b0a8132471eaec97be2c11042ebe1689f6439de25", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_file_storage`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_file_storage_agent.py` and in the RCI capsule.

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

Configure and manage file storage Completeness Audit — Runs a read-only completeness and policy audit of file storage configuration records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-file-storage
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
      "description": "Date range used to judge stale records; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "The D365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-configure-and-manage-file-storage-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 aa4f22d801281095…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_file_storage_agent.py` first:

```bash
python3 audit_configure_and_manage_file_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_file_storage_agent.py   # or on stdin
python3 audit_configure_and_manage_file_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage file storage Completeness Audit — Runs a read-only completeness and policy audit of file storage configuration records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-file-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_file_storage',
    "version": '3.0.2',
    "display_name": 'Configure and manage file storage Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of file storage configuration records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of',
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
        "upstream_slug": 'audit-configure-and-manage-file-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-file-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '826863cd50123fdb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/configure-and-manage-file-storage'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-file-storage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'legal_entity': 'The D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-file-storage-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit configure and manage file storage records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to configure and manage file storage. Output an Excel workbook 'audit-configure-and-manage-file-storage-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no configure and manage file storage data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads configure and manage file storage records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of file storage configuration records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of', 'example_request': 'Audit configure and manage file storage records in USMF for completeness and give me the Excel workbook.', 'inputs': [{'description': 'The D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-file-storage-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to check Dynamics 365 file storage configuration records for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConfigureAndManageFileStorage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageFileStorage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'The D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-file-storage-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConfigureAndManageFileStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
