---
name: "rar-cowork-cookbook-audit-migrate-to-new-versions-of-software"
description: "Read-only audit of 'migrate to new versions of software' records in a Dynamics 365 F&SCM legal entity via the Cowork D365 ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_migrate_to_new_versions_of_software", "rar_sha256": "ff58449b44f509581c027e2229ccf26560a8c0d58a3a3fac758277c975222718", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
