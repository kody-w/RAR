---
name: "rar-cowork-cookbook-audit-analyze-and-mitigate-risks"
description: "Audits analyze-and-mitigate-risks records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_and_mitigate_risks", "rar_sha256": "bb3750f30cee7468adcf425923646439aea2964fac75fe3f8215a622dcfb605c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_and_mitigate_risks`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_and_mitigate_risks_agent.py` and in the RCI capsule.

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

Analyze and mitigate risks Completeness Audit — Audits analyze-and-mitigate-risks records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks
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
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017.",
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
      "description": "Excel workbook name, e.g. audit-analyze-and-mitigate-risks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_and_mitigate_risks_agent.py` and embedded as the fenced Python below (sha256 bb3750f30cee7468…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_and_mitigate_risks_agent.py` first:

```bash
python3 audit_analyze_and_mitigate_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_and_mitigate_risks_agent.py   # or on stdin
python3 audit_analyze_and_mitigate_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and mitigate risks Completeness Audit — Audits analyze-and-mitigate-risks records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_and_mitigate_risks',
    "version": '3.0.2',
    "display_name": 'Analyze and mitigate risks Completeness Audit',
    "description": 'Audits analyze-and-mitigate-risks records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-analyze-and-mitigate-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-and-mitigate-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6244862ae0cdea28',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/analyze-and-mitigate-risks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-analyze-and-mitigate-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; the recipe uses USMF.', 'output_filename': 'Excel workbook name, e.g. audit-analyze-and-mitigate-risks-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze and mitigate risks records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze and mitigate risks. Output an Excel workbook 'audit-analyze-and-mitigate-risks-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze and mitigate risks data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze and mitigate risks records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits analyze-and-mitigate-risks records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit our analyze and mitigate risks records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-analyze-and-mitigate-risks-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of analyze and mitigate risks records in D365 ERP via Cowork, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeAndMitigateRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeAndMitigateRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-analyze-and-mitigate-risks-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeAndMitigateRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
