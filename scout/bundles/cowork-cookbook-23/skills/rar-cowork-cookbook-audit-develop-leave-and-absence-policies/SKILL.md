---
name: "rar-cowork-cookbook-audit-develop-leave-and-absence-policies"
description: "Audits leave and absence policy records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, and retu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_leave_and_absence_policies", "rar_sha256": "9b0bd7c043f405e3aa0be6dfab17eca57d27a6c47ae91558d6cea2ef1e2be9b6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_leave_and_absence_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_leave_and_absence_policies_agent.py` and in the RCI capsule.

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

Develop leave and absence policies Completeness Audit — Audits leave and absence policy records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, and retu

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit; the recipe uses USMF.",
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
      "description": "Excel workbook name, e.g. audit-develop-leave-and-absence-policies-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_leave_and_absence_policies_agent.py` and embedded as the fenced Python below (sha256 9b0bd7c043f405e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_leave_and_absence_policies_agent.py` first:

```bash
python3 audit_develop_leave_and_absence_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_leave_and_absence_policies_agent.py   # or on stdin
python3 audit_develop_leave_and_absence_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop leave and absence policies Completeness Audit — Audits leave and absence policy records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, and retu

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_leave_and_absence_policies',
    "version": '3.0.2',
    "display_name": 'Develop leave and absence policies Completeness Audit',
    "description": 'Audits leave and absence policy records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, and retu',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-leave-and-absence-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec8c4bc58e4ec0d5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/develop-leave-and-absence-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-develop-leave-and-absence-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; the recipe uses USMF.', 'output_filename': 'Excel workbook name, e.g. audit-develop-leave-and-absence-policies-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop leave and absence policies records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop leave and absence policies. Output an Excel workbook 'audit-develop-leave-and-absence-policies-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop leave and absence policies data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop leave and absence policies records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits leave and absence policy records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, and retu', 'example_request': 'Audit USMF leave and absence policy records for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-develop-leave-and-absence-policies-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and compliance audit of D365 leave and absence policy records delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopLeaveAndAbsencePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopLeaveAndAbsencePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-develop-leave-and-absence-policies-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopLeaveAndAbsencePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
