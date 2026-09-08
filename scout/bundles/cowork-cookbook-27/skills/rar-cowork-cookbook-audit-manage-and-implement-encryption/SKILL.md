---
name: "rar-cowork-cookbook-audit-manage-and-implement-encryption"
description: "Runs a read-only completeness and policy audit of manage-and-implement-encryption records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary she"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_and_implement_encryption", "rar_sha256": "2ceaaef780c3791b4c938ec0901c9616e1f09b18e5b9fc4066ec62819f63e57d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
