---
name: "rar-cowork-cookbook-audit-analyze-and-mitigate-risks"
description: "Audits analyze-and-mitigate-risks records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_and_mitigate_risks", "rar_sha256": "bb3750f30cee7468adcf425923646439aea2964fac75fe3f8215a622dcfb605c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
