---
name: "rar-cowork-cookbook-audit-develop-chart-of-accounts-strategy"
description: "Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_chart_of_accounts_strategy", "rar_sha256": "c6d72a802ef05deef5d437b6061906ddd8882d8734426a088ff6611fef52b6bd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_chart_of_accounts_strategy`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_chart_of_accounts_strategy_agent.py` and in the RCI capsule.

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

Develop chart of accounts strategy Completeness Audit — Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy
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
      "description": "Date range used to judge stale records; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_chart_of_accounts_strategy_agent.py` and embedded as the fenced Python below (sha256 c6d72a802ef05dee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_chart_of_accounts_strategy_agent.py` first:

```bash
python3 audit_develop_chart_of_accounts_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_chart_of_accounts_strategy_agent.py   # or on stdin
python3 audit_develop_chart_of_accounts_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop chart of accounts strategy Completeness Audit — Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_chart_of_accounts_strategy',
    "version": '3.0.2',
    "display_name": 'Develop chart of accounts strategy Completeness Audit',
    "description": 'Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work',
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
        "upstream_slug": 'audit-develop-chart-of-accounts-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-chart-of-accounts-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bd71e090e5059b3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-chart-of-accounts-strategy'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-develop-chart-of-accounts-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop chart of accounts strategy records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop chart of accounts strategy. Output an Excel workbook 'audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop chart of accounts strategy data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop chart of accounts strategy records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits chart of accounts strategy records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel work', 'example_request': 'Audit chart of accounts strategy records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of chart of accounts strategy records in D365 ERP via the Cowork plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopChartOfAccountsStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopChartOfAccountsStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-chart-of-accounts-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopChartOfAccountsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
