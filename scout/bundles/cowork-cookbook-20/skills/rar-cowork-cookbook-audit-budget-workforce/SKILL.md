---
name: "rar-cowork-cookbook-audit-budget-workforce"
description: "Runs a read-only completeness and policy audit of Dynamics 365 budget workforce records for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_budget_workforce", "rar_sha256": "3823440eb6483e1b027c087a68afd09272f20f476ebe26036852984e8311a3ca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_budget_workforce`. The original RAPP
agent is preserved byte-for-byte in `audit_budget_workforce_agent.py` and in the RCI capsule.

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

Budget workforce Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 budget workforce records for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-budget-workforce
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
      "description": "Date range used to judge stale dates; adjust for demo data eras such as FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-budget-workforce-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_budget_workforce_agent.py` and embedded as the fenced Python below (sha256 3823440eb6483e1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_budget_workforce_agent.py` first:

```bash
python3 audit_budget_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_budget_workforce_agent.py   # or on stdin
python3 audit_budget_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget workforce Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 budget workforce records for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-budget-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_budget_workforce',
    "version": '3.0.2',
    "display_name": 'Budget workforce Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of Dynamics 365 budget workforce records for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-budget-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-budget-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '04e67ffd2b1a7b55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/budget-workforce'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-budget-workforce', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-budget-workforce-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit budget workforce records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to budget workforce. Output an Excel workbook 'audit-budget-workforce-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no budget workforce data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads budget workforce records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of Dynamics 365 budget workforce records for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit budget workforce records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-budget-workforce-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants budget workforce records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditBudgetWorkforce(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditBudgetWorkforce'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-budget-workforce-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditBudgetWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
