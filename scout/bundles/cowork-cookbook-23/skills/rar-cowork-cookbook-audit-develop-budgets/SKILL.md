---
name: "rar-cowork-cookbook-audit-develop-budgets"
description: "Audits develop budgets records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workb"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_budgets", "rar_sha256": "e0ab436768065a936ddd7e94815bb3dbf31dabeb963955101246505a2eeb72b2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
