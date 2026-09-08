---
name: "rar-cowork-cookbook-audit-analyze-sales-data"
description: "Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sales_data", "rar_sha256": "e196e36e84f532a660059d44f560769e87864970e8009b1784f2cfb8934b5aeb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_sales_data`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_sales_data_agent.py` and in the RCI capsule.

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

Analyze sales data Completeness Audit — Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sales-data
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
      "description": "Name of the Excel workbook to produce, e.g. audit-analyze-sales-data-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_sales_data_agent.py` and embedded as the fenced Python below (sha256 e196e36e84f532a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_sales_data_agent.py` first:

```bash
python3 audit_analyze_sales_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_sales_data_agent.py   # or on stdin
python3 audit_analyze_sales_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sales data Completeness Audit — Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sales-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_sales_data',
    "version": '3.0.2',
    "display_name": 'Analyze sales data Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-sales-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-sales-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6d89116c061e5308',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-analyze-sales-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-analyze-sales-data-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze sales data records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze sales data. Output an Excel workbook 'audit-analyze-sales-data-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze sales data data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze sales data records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of sales data records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit sales data completeness in USMF for FY2017 and give me the audit Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-sales-data-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants sales data records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeSalesData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeSalesData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-sales-data-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeSalesData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
