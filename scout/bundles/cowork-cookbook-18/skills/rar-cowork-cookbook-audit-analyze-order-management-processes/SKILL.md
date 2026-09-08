---
name: "rar-cowork-cookbook-audit-analyze-order-management-processes"
description: "Runs a read-only completeness and policy audit of order management records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_order_management_processes", "rar_sha256": "d23987ecb3edf1110f2d597f2678f0bea21300661de85da1209ab50b719dc151", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
