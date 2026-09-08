---
name: "rar-cowork-cookbook-audit-analyze-product-profitability"
description: "Runs a read-only completeness and policy audit of product profitability records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_product_profitability", "rar_sha256": "0d004986c1abf668c6efe9ac6278e89489017a051f07aa8d4c81b7d92b304969", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
