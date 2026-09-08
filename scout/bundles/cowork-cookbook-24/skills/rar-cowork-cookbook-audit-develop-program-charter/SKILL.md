---
name: "rar-cowork-cookbook-audit-develop-program-charter"
description: "Audits develop program charter records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Exc"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_program_charter", "rar_sha256": "615da6ab1cdd5a55963ce2931959dc2b80c22e3629895796150722749193cdd1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
