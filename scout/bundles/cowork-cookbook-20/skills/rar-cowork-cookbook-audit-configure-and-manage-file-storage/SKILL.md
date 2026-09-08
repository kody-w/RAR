---
name: "rar-cowork-cookbook-audit-configure-and-manage-file-storage"
description: "Runs a read-only completeness and policy audit of file storage configuration records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_file_storage", "rar_sha256": "aa4f22d801281095cf22ee6b0a8132471eaec97be2c11042ebe1689f6439de25", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
