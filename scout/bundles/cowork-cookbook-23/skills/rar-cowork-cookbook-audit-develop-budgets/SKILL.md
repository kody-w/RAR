---
name: "rar-cowork-cookbook-audit-develop-budgets"
description: "Audits develop budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workb"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_budgets", "rar_sha256": "e0ab436768065a936ddd7e94815bb3dbf31dabeb963955101246505a2eeb72b2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_budgets`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_budgets_agent.py` and in the RCI capsule.

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

Develop budgets Completeness Audit — Audits develop budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-budgets
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
      "description": "Excel workbook name, e.g. audit-develop-budgets-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_budgets_agent.py` and embedded as the fenced Python below (sha256 e0ab436768065a93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_budgets_agent.py` first:

```bash
python3 audit_develop_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_budgets_agent.py   # or on stdin
python3 audit_develop_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgets Completeness Audit — Audits develop budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_budgets',
    "version": '3.0.2',
    "display_name": 'Develop budgets Completeness Audit',
    "description": 'Audits develop budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workb',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c9f90f3e9f50e8c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/develop-budgets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-develop-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Excel workbook name, e.g. audit-develop-budgets-2026-05-24.xlsx, saved to Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop budgets records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop budgets. Output an Excel workbook 'audit-develop-budgets-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop budgets data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop budgets records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits develop budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workb', 'example_request': 'Audit develop budgets in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-develop-budgets-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of develop budgets data in D365 ERP, delivered as an Excel findings workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-develop-budgets-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}},
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
    print(AuditDevelopBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
