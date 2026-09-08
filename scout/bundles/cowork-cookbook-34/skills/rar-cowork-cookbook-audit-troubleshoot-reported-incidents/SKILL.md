---
name: "rar-cowork-cookbook-audit-troubleshoot-reported-incidents"
description: "Runs a read-only completeness audit of troubleshoot reported incidents records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_troubleshoot_reported_incidents", "rar_sha256": "14fc2f4f2dacfab41db75366440979deed495067ff5776a6a078fbfb0f714f59", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_troubleshoot_reported_incidents`. The original RAPP
agent is preserved byte-for-byte in `audit_troubleshoot_reported_incidents_agent.py` and in the RCI capsule.

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

Troubleshoot reported incidents Completeness Audit — Runs a read-only completeness audit of troubleshoot reported incidents records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-troubleshoot-reported-incidents
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
      "description": "Name of the Excel workbook to produce, e.g. audit-troubleshoot-reported-incidents-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_troubleshoot_reported_incidents_agent.py` and embedded as the fenced Python below (sha256 14fc2f4f2dacfab4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_troubleshoot_reported_incidents_agent.py` first:

```bash
python3 audit_troubleshoot_reported_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_troubleshoot_reported_incidents_agent.py   # or on stdin
python3 audit_troubleshoot_reported_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Troubleshoot reported incidents Completeness Audit — Runs a read-only completeness audit of troubleshoot reported incidents records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-troubleshoot-reported-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_troubleshoot_reported_incidents',
    "version": '3.0.3',
    "display_name": 'Troubleshoot reported incidents Completeness Audit',
    "description": 'Runs a read-only completeness audit of troubleshoot reported incidents records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-troubleshoot-reported-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-troubleshoot-reported-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd764493c9190d392',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/troubleshoot-reported-incidents'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-troubleshoot-reported-incidents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-troubleshoot-reported-incidents-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit troubleshoot reported incidents records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to troubleshoot reported incidents. Output an Excel workbook 'audit-troubleshoot-reported-incidents-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no troubleshoot reported incidents data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Reads troubleshoot reported incidents records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness audit of troubleshoot reported incidents records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit troubleshoot reported incidents in USMF for completeness and give me the Excel workbook with a summary sheet.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-troubleshoot-reported-incidents-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants incident records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditTroubleshootReportedIncidents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTroubleshootReportedIncidents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-troubleshoot-reported-incidents-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditTroubleshootReportedIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
