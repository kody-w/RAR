---
name: "rar-cowork-cookbook-audit-evaluate-marketing-financials"
description: "Runs a read-only completeness and policy audit of marketing financials records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_marketing_financials", "rar_sha256": "5b7036512e75c0bc43dd8af2409f443b24e518b97bf47213362a28eb1db57480", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_evaluate_marketing_financials`. The original RAPP
agent is preserved byte-for-byte in `audit_evaluate_marketing_financials_agent.py` and in the RCI capsule.

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

Evaluate marketing financials Completeness Audit — Runs a read-only completeness and policy audit of marketing financials records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials
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
      "description": "Date range treated as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-evaluate-marketing-financials-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_evaluate_marketing_financials_agent.py` and embedded as the fenced Python below (sha256 5b7036512e75c0bc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_evaluate_marketing_financials_agent.py` first:

```bash
python3 audit_evaluate_marketing_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_evaluate_marketing_financials_agent.py   # or on stdin
python3 audit_evaluate_marketing_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate marketing financials Completeness Audit — Runs a read-only completeness and policy audit of marketing financials records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_evaluate_marketing_financials',
    "version": '3.0.2',
    "display_name": 'Evaluate marketing financials Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of marketing financials records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-evaluate-marketing-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0efc26999a357465',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-marketing-financials'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-evaluate-marketing-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-evaluate-marketing-financials-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit evaluate marketing financials records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to evaluate marketing financials. Output an Excel workbook 'audit-evaluate-marketing-financials-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no evaluate marketing financials data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads evaluate marketing financials records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of marketing financials records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit marketing financials completeness in USMF and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-evaluate-marketing-financials-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to audit marketing financials records in D365 for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditEvaluateMarketingFinancials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEvaluateMarketingFinancials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-evaluate-marketing-financials-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditEvaluateMarketingFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
