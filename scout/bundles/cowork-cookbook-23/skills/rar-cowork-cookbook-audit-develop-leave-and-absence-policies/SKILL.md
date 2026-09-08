---
name: "rar-cowork-cookbook-audit-develop-leave-and-absence-policies"
description: "Audits leave and absence policy records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, and retu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_leave_and_absence_policies", "rar_sha256": "9b0bd7c043f405e3aa0be6dfab17eca57d27a6c47ae91558d6cea2ef1e2be9b6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
