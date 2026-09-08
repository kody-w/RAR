---
name: "rar-cowork-cookbook-audit-troubleshoot-reported-incidents"
description: "Runs a read-only completeness audit of troubleshoot reported incidents records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_troubleshoot_reported_incidents", "rar_sha256": "14fc2f4f2dacfab41db75366440979deed495067ff5776a6a078fbfb0f714f59", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
