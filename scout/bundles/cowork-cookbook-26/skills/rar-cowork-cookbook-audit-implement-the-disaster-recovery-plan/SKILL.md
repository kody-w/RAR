---
name: "rar-cowork-cookbook-audit-implement-the-disaster-recovery-plan"
description: "Runs a read-only completeness and policy audit of disaster recovery plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of count"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_the_disaster_recovery_plan", "rar_sha256": "441f87853d7c0fe9e32ded509b27346f49504ede9d6b419b5a631289c3537df4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_implement_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `audit_implement_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Implement the disaster recovery plan Completeness Audit — Runs a read-only completeness and policy audit of disaster recovery plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of count

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-the-disaster-recovery-plan
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
      "description": "Name of the Excel workbook to produce, e.g. audit-implement-the-disaster-recovery-plan-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 441f87853d7c0fe9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_the_disaster_recovery_plan_agent.py` first:

```bash
python3 audit_implement_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_implement_the_disaster_recovery_plan_agent.py   # or on stdin
python3 audit_implement_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement the disaster recovery plan Completeness Audit — Runs a read-only completeness and policy audit of disaster recovery plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of count

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_implement_the_disaster_recovery_plan',
    "version": '3.0.2',
    "display_name": 'Implement the disaster recovery plan Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of disaster recovery plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of count',
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
        "upstream_slug": 'audit-implement-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-implement-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1569cfeedd20cc2a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-the-disaster-recovery-plan'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-implement-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-implement-the-disaster-recovery-plan-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit implement the disaster recovery plan records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to implement the disaster recovery plan. Output an Excel workbook 'audit-implement-the-disaster-recovery-plan-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no implement the disaster recovery plan data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads implement the disaster recovery plan records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of disaster recovery plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of count', 'example_request': 'Audit the disaster recovery plan records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-implement-the-disaster-recovery-plan-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants disaster recovery plan records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditImplementTheDisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditImplementTheDisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-implement-the-disaster-recovery-plan-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditImplementTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
