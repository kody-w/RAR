---
name: "rar-cowork-cookbook-audit-conduct-a-business-impact-analysis"
description: "Read-only audit of business impact analysis records in Dynamics 365 F&SCM (legal entity USMF) that returns an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inactive re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_a_business_impact_analysis", "rar_sha256": "f7ff74cc4218a7062b8eab9ad93a0762efcee7e8c937f228e2f5ab21be9c6d91", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
