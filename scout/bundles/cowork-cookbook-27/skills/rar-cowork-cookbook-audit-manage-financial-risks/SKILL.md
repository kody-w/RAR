---
name: "rar-cowork-cookbook-audit-manage-financial-risks"
description: "Read-only audit of manage-financial-risks records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, delivered as an Excel w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_financial_risks", "rar_sha256": "8862c4e838604442ef7dff128cefba4c9f371ecae5d45142a3be56953ed9aa9f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
