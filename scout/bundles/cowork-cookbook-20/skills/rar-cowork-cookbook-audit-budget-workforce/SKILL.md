---
name: "rar-cowork-cookbook-audit-budget-workforce"
description: "Runs a read-only completeness and policy audit of Dynamics 365 budget workforce records for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_budget_workforce", "rar_sha256": "3823440eb6483e1b027c087a68afd09272f20f476ebe26036852984e8311a3ca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
