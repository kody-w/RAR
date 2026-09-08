---
name: "rar-cowork-cookbook-audit-manage-and-implement-encryption"
description: "Runs a read-only completeness and policy audit of manage-and-implement-encryption records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary she"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_and_implement_encryption", "rar_sha256": "2ceaaef780c3791b4c938ec0901c9616e1f09b18e5b9fc4066ec62819f63e57d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_and_implement_encryption`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_and_implement_encryption_agent.py` and in the RCI capsule.

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

Manage and implement encryption Completeness Audit — Runs a read-only completeness and policy audit of manage-and-implement-encryption records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary she

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption
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
      "description": "Name of the Excel workbook to produce, e.g. audit-manage-and-implement-encryption-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_and_implement_encryption_agent.py` and embedded as the fenced Python below (sha256 2ceaaef780c3791b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_and_implement_encryption_agent.py` first:

```bash
python3 audit_manage_and_implement_encryption_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_and_implement_encryption_agent.py   # or on stdin
python3 audit_manage_and_implement_encryption_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage and implement encryption Completeness Audit — Runs a read-only completeness and policy audit of manage-and-implement-encryption records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary she

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_and_implement_encryption',
    "version": '3.0.3',
    "display_name": 'Manage and implement encryption Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of manage-and-implement-encryption records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary she',
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
        "upstream_slug": 'audit-manage-and-implement-encryption',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c6bdc2d001da7210',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-and-implement-encryption'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-manage-and-implement-encryption', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-manage-and-implement-encryption-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage and implement encryption records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage and implement encryption. Output an Excel workbook 'audit-manage-and-implement-encryption-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage and implement encryption data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads manage and implement encryption records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of manage-and-implement-encryption records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary she', 'example_request': 'Audit encryption management records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-and-implement-encryption-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants encryption-management records in D365 F&SCM checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageAndImplementEncryption(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageAndImplementEncryption'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-and-implement-encryption-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageAndImplementEncryption().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
