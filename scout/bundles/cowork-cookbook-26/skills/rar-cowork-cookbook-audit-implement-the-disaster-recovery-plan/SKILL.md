---
name: "rar-cowork-cookbook-audit-implement-the-disaster-recovery-plan"
description: "Runs a read-only completeness and policy audit of disaster recovery plan records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of count"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_the_disaster_recovery_plan", "rar_sha256": "441f87853d7c0fe9e32ded509b27346f49504ede9d6b419b5a631289c3537df4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
