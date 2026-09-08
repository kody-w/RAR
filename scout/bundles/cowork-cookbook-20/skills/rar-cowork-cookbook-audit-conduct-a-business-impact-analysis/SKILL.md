---
name: "rar-cowork-cookbook-audit-conduct-a-business-impact-analysis"
description: "Read-only audit of business impact analysis records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inactive re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_a_business_impact_analysis", "rar_sha256": "f7ff74cc4218a7062b8eab9ad93a0762efcee7e8c937f228e2f5ab21be9c6d91", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_conduct_a_business_impact_analysis`. The original RAPP
agent is preserved byte-for-byte in `audit_conduct_a_business_impact_analysis_agent.py` and in the RCI capsule.

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

Conduct a business impact analysis Completeness Audit — Read-only audit of business impact analysis records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inactive re

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-a-business-impact-analysis
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
      "description": "Excel workbook name, e.g. audit-conduct-a-business-impact-analysis-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_conduct_a_business_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 f7ff74cc4218a706…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_conduct_a_business_impact_analysis_agent.py` first:

```bash
python3 audit_conduct_a_business_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_conduct_a_business_impact_analysis_agent.py   # or on stdin
python3 audit_conduct_a_business_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a business impact analysis Completeness Audit — Read-only audit of business impact analysis records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inactive re

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-a-business-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_conduct_a_business_impact_analysis',
    "version": '3.0.2',
    "display_name": 'Conduct a business impact analysis Completeness Audit',
    "description": 'Read-only audit of business impact analysis records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inactive re',
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
        "upstream_slug": 'audit-conduct-a-business-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-conduct-a-business-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa00e5634d8987f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-business-impact-analysis'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-conduct-a-business-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-conduct-a-business-impact-analysis-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit conduct a business impact analysis records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to conduct a business impact analysis. Output an Excel workbook 'audit-conduct-a-business-impact-analysis-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no conduct a business impact analysis data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads conduct a business impact analysis records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of business impact analysis records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inactive re', 'example_request': 'Audit the business impact analysis records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-conduct-a-business-impact-analysis-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants business impact analysis records in D365 checked for completeness and policy compliance, with findings exported to Excel and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConductABusinessImpactAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConductABusinessImpactAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-conduct-a-business-impact-analysis-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConductABusinessImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
