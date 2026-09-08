---
name: "rar-cowork-cookbook-audit-analyze-product-profitability"
description: "Runs a read-only completeness and policy audit of product profitability records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_product_profitability", "rar_sha256": "0d004986c1abf668c6efe9ac6278e89489017a051f07aa8d4c81b7d92b304969", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_product_profitability`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_product_profitability_agent.py` and in the RCI capsule.

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

Analyze product profitability Completeness Audit — Runs a read-only completeness and policy audit of product profitability records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-product-profitability
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
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-analyze-product-profitability-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_product_profitability_agent.py` and embedded as the fenced Python below (sha256 0d004986c1abf668…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_product_profitability_agent.py` first:

```bash
python3 audit_analyze_product_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_product_profitability_agent.py   # or on stdin
python3 audit_analyze_product_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product profitability Completeness Audit — Runs a read-only completeness and policy audit of product profitability records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-product-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_product_profitability',
    "version": '3.0.2',
    "display_name": 'Analyze product profitability Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of product profitability records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-product-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-product-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3fc00c46e17440a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-profitability'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-analyze-product-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-analyze-product-profitability-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze product profitability records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze product profitability. Output an Excel workbook 'audit-analyze-product-profitability-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze product profitability data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze product profitability records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of product profitability records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun', 'example_request': 'Audit product profitability records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-product-profitability-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to audit product profitability records in Dynamics 365 for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeProductProfitability(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeProductProfitability'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-product-profitability-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeProductProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
