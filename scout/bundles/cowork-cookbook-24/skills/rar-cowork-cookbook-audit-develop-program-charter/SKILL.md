---
name: "rar-cowork-cookbook-audit-develop-program-charter"
description: "Audits develop program charter records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Exc"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_program_charter", "rar_sha256": "615da6ab1cdd5a55963ce2931959dc2b80c22e3629895796150722749193cdd1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_program_charter`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_program_charter_agent.py` and in the RCI capsule.

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

Develop program charter Completeness Audit — Audits develop program charter records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Exc

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-program-charter
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-program-charter-2026-05-24.xlsx.",
      "type": "string"
    },
    "record_type": {
      "description": "The record set to audit, e.g. develop program charter.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_program_charter_agent.py` and embedded as the fenced Python below (sha256 615da6ab1cdd5a55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_program_charter_agent.py` first:

```bash
python3 audit_develop_program_charter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_program_charter_agent.py   # or on stdin
python3 audit_develop_program_charter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop program charter Completeness Audit — Audits develop program charter records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Exc

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-program-charter
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_program_charter',
    "version": '3.0.2',
    "display_name": 'Develop program charter Completeness Audit',
    "description": 'Audits develop program charter records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Exc',
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
        "upstream_slug": 'audit-develop-program-charter',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-program-charter',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee354ec540a87a1f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-program-charter'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-develop-program-charter', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-program-charter-2026-05-24.xlsx.', 'record_type': 'The record set to audit, e.g. develop program charter.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop program charter records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop program charter. Output an Excel workbook 'audit-develop-program-charter-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop program charter data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop program charter records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits develop program charter records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Exc', 'example_request': 'Audit develop program charter records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The record set to audit, e.g. develop program charter.', 'name': 'record_type'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-program-charter-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of develop program charter records in a D365 legal entity, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopProgramCharter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopProgramCharter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-program-charter-2026-05-24.xlsx.', 'type': 'string'}, 'record_type': {'description': 'The record set to audit, e.g. develop program charter.', 'type': 'string'}},
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
    print(AuditDevelopProgramCharter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
