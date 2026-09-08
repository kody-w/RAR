---
name: "rar-cowork-cookbook-audit-allocate-budgets"
description: "Runs a read-only completeness and policy audit of allocate budgets records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and returns an Excel workbook with one sheet per finding category plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_allocate_budgets", "rar_sha256": "1c1c7cc8893e08f6faec1800faaba6b75311de6504ff0b519991a9cb1eb11cac", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_allocate_budgets`. The original RAPP
agent is preserved byte-for-byte in `audit_allocate_budgets_agent.py` and in the RCI capsule.

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

Allocate budgets Completeness Audit — Runs a read-only completeness and policy audit of allocate budgets records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and returns an Excel workbook with one sheet per finding category plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-allocate-budgets
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
      "description": "Dynamics 365 legal entity to audit; defaults to USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. 'audit-allocate-budgets-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_allocate_budgets_agent.py` and embedded as the fenced Python below (sha256 1c1c7cc8893e08f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_allocate_budgets_agent.py` first:

```bash
python3 audit_allocate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_allocate_budgets_agent.py   # or on stdin
python3 audit_allocate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate budgets Completeness Audit — Runs a read-only completeness and policy audit of allocate budgets records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and returns an Excel workbook with one sheet per finding category plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-allocate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_allocate_budgets',
    "version": '3.0.2',
    "display_name": 'Allocate budgets Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of allocate budgets records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and returns an Excel workbook with one sheet per finding category plus a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-allocate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-allocate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b691d330e558f40',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/allocate-budgets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-allocate-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit; defaults to USMF.', 'output_filename': "Name of the Excel workbook to produce, e.g. 'audit-allocate-budgets-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit allocate budgets records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to allocate budgets. Output an Excel workbook 'audit-allocate-budgets-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no allocate budgets data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads allocate budgets records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of allocate budgets records in Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and returns an Excel workbook with one sheet per finding category plus a', 'example_request': 'Audit allocate budgets in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': "Name of the Excel workbook to produce, e.g. 'audit-allocate-budgets-2026-05-24.xlsx'.", 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants allocate budgets records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAllocateBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAllocateBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': "Name of the Excel workbook to produce, e.g. 'audit-allocate-budgets-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(AuditAllocateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
