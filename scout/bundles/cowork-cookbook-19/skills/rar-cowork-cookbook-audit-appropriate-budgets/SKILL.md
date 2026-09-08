---
name: "rar-cowork-cookbook-audit-appropriate-budgets"
description: "Audits appropriate budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook with one"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_appropriate_budgets", "rar_sha256": "a87f57ac196a6dc19bd70cdc751f45f9b49ad7b3a90273b43111554c49b6a777", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
