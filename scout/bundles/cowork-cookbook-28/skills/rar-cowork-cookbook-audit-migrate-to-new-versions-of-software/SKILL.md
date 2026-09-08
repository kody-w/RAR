---
name: "rar-cowork-cookbook-audit-migrate-to-new-versions-of-software"
description: "Read-only audit of 'migrate to new versions of software' records in a Dynamics 365 F&SCM legal entity via the Cowork D365 ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_migrate_to_new_versions_of_software", "rar_sha256": "ff58449b44f509581c027e2229ccf26560a8c0d58a3a3fac758277c975222718", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_migrate_to_new_versions_of_software`. The original RAPP
agent is preserved byte-for-byte in `audit_migrate_to_new_versions_of_software_agent.py` and in the RCI capsule.

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

Migrate to new versions of software Completeness Audit — Read-only audit of 'migrate to new versions of software' records in a Dynamics 365 F&SCM legal entity via the Cowork D365 ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-migrate-to-new-versions-of-software
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
      "description": "D365 legal entity to audit (e.g. USMF).",
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
      "description": "Excel workbook name, e.g. audit-migrate-to-new-versions-of-software-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_migrate_to_new_versions_of_software_agent.py` and embedded as the fenced Python below (sha256 ff58449b44f50958…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_migrate_to_new_versions_of_software_agent.py` first:

```bash
python3 audit_migrate_to_new_versions_of_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_migrate_to_new_versions_of_software_agent.py   # or on stdin
python3 audit_migrate_to_new_versions_of_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Migrate to new versions of software Completeness Audit — Read-only audit of 'migrate to new versions of software' records in a Dynamics 365 F&SCM legal entity via the Cowork D365 ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-migrate-to-new-versions-of-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_migrate_to_new_versions_of_software',
    "version": '3.0.3',
    "display_name": 'Migrate to new versions of software Completeness Audit',
    "description": "Read-only audit of 'migrate to new versions of software' records in a Dynamics 365 F&SCM legal entity via the Cowork D365 ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.",
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
        "upstream_slug": 'audit-migrate-to-new-versions-of-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-migrate-to-new-versions-of-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c77bd7597d792cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/migrate-to-new-versions-of-software'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-migrate-to-new-versions-of-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit (e.g. USMF).', 'output_filename': 'Excel workbook name, e.g. audit-migrate-to-new-versions-of-software-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit migrate to new versions of software records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to migrate to new versions of software. Output an Excel workbook 'audit-migrate-to-new-versions-of-software-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no migrate to new versions of software data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads migrate to new versions of software records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Read-only audit of 'migrate to new versions of software' records in a Dynamics 365 F&SCM legal entity via the Cowork D365 ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.", 'example_request': 'Audit migrate-to-new-versions-of-software records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-migrate-to-new-versions-of-software-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a completeness and policy-compliance check of migrate-to-new-versions-of-software records in D365 F&SCM, with no data modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMigrateToNewVersionsOfSoftware(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMigrateToNewVersionsOfSoftware'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-migrate-to-new-versions-of-software-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMigrateToNewVersionsOfSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
