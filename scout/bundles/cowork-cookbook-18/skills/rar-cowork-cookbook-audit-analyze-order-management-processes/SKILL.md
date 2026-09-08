---
name: "rar-cowork-cookbook-audit-analyze-order-management-processes"
description: "Runs a read-only completeness and policy audit of order management records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_order_management_processes", "rar_sha256": "d23987ecb3edf1110f2d597f2678f0bea21300661de85da1209ab50b719dc151", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_order_management_processes`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_order_management_processes_agent.py` and in the RCI capsule.

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

Analyze order management processes Completeness Audit — Runs a read-only completeness and policy audit of order management records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-order-management-processes
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
      "description": "Name of the Excel workbook to produce, e.g. audit-analyze-order-management-processes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_order_management_processes_agent.py` and embedded as the fenced Python below (sha256 d23987ecb3edf111…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_order_management_processes_agent.py` first:

```bash
python3 audit_analyze_order_management_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_order_management_processes_agent.py   # or on stdin
python3 audit_analyze_order_management_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze order management processes Completeness Audit — Runs a read-only completeness and policy audit of order management records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-order-management-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_order_management_processes',
    "version": '3.0.2',
    "display_name": 'Analyze order management processes Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of order management records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-order-management-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-order-management-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3b388bff30c354f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-order-management-processes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-analyze-order-management-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-analyze-order-management-processes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze order management processes records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze order management processes. Output an Excel workbook 'audit-analyze-order-management-processes-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze order management processes data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze order management processes records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of order management records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit order management records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-order-management-processes-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants order management records audited for missing fields, stale dates, blank descriptions, inactive references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeOrderManagementProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeOrderManagementProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-order-management-processes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeOrderManagementProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
