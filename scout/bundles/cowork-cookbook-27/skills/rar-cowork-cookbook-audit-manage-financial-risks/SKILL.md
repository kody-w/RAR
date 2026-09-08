---
name: "rar-cowork-cookbook-audit-manage-financial-risks"
description: "Read-only audit of manage-financial-risks records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, delivered as an Excel w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_financial_risks", "rar_sha256": "8862c4e838604442ef7dff128cefba4c9f371ecae5d45142a3be56953ed9aa9f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_financial_risks`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_financial_risks_agent.py` and in the RCI capsule.

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

Manage financial risks Completeness Audit — Read-only audit of manage-financial-risks records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, delivered as an Excel w

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-financial-risks
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
      "description": "Excel workbook name, e.g. audit-manage-financial-risks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_financial_risks_agent.py` and embedded as the fenced Python below (sha256 8862c4e838604442…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_financial_risks_agent.py` first:

```bash
python3 audit_manage_financial_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_financial_risks_agent.py   # or on stdin
python3 audit_manage_financial_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage financial risks Completeness Audit — Read-only audit of manage-financial-risks records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, delivered as an Excel w

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-financial-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_financial_risks',
    "version": '3.0.3',
    "display_name": 'Manage financial risks Completeness Audit',
    "description": 'Read-only audit of manage-financial-risks records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, delivered as an Excel w',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-financial-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-financial-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd58acfc26e1580b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/manage-financial-risks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-manage-financial-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit (e.g. USMF).', 'output_filename': 'Excel workbook name, e.g. audit-manage-financial-risks-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage financial risks records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage financial risks. Output an Excel workbook 'audit-manage-financial-risks-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage financial risks data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage financial risks records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of manage-financial-risks records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, delivered as an Excel w', 'example_request': 'Audit manage financial risks records in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-manage-financial-risks-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance check of manage financial risks records in D365 ERP, with findings exported to Excel and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageFinancialRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageFinancialRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-manage-financial-risks-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageFinancialRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
