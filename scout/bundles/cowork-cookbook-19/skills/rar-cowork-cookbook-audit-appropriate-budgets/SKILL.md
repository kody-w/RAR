---
name: "rar-cowork-cookbook-audit-appropriate-budgets"
description: "Audits appropriate budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_appropriate_budgets", "rar_sha256": "a87f57ac196a6dc19bd70cdc751f45f9b49ad7b3a90273b43111554c49b6a777", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_appropriate_budgets`. The original RAPP
agent is preserved byte-for-byte in `audit_appropriate_budgets_agent.py` and in the RCI capsule.

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

Appropriate budgets Completeness Audit — Audits appropriate budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-appropriate-budgets
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
      "description": "D365 legal entity to audit; defaults to USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-appropriate-budgets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_appropriate_budgets_agent.py` and embedded as the fenced Python below (sha256 a87f57ac196a6dc1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_appropriate_budgets_agent.py` first:

```bash
python3 audit_appropriate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_appropriate_budgets_agent.py   # or on stdin
python3 audit_appropriate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Appropriate budgets Completeness Audit — Audits appropriate budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-appropriate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_appropriate_budgets',
    "version": '3.0.2',
    "display_name": 'Appropriate budgets Completeness Audit',
    "description": 'Audits appropriate budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one',
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
        "upstream_slug": 'audit-appropriate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-appropriate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d000205360b01fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/appropriate-budgets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-appropriate-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-appropriate-budgets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit appropriate budgets records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to appropriate budgets. Output an Excel workbook 'audit-appropriate-budgets-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no appropriate budgets data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads appropriate budgets records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits appropriate budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one', 'example_request': 'Audit appropriate budgets in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-appropriate-budgets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of appropriate budgets records in D365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAppropriateBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAppropriateBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-appropriate-budgets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAppropriateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
