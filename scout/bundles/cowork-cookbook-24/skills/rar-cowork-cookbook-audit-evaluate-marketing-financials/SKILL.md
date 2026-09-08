---
name: "rar-cowork-cookbook-audit-evaluate-marketing-financials"
description: "Runs a read-only completeness and policy audit of marketing financials records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_marketing_financials", "rar_sha256": "5b7036512e75c0bc43dd8af2409f443b24e518b97bf47213362a28eb1db57480", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
