---
name: "rar-cowork-cookbook-audit-estimate-project-contracts"
description: "Runs a read-only completeness and policy audit of estimate project contracts in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_estimate_project_contracts", "rar_sha256": "b3f55abf930df5cc71f4f5ef30576786958a850df144f7525653dc2c2af31011", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_estimate_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `audit_estimate_project_contracts_agent.py` and in the RCI capsule.

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

Estimate project contracts Completeness Audit — Runs a read-only completeness and policy audit of estimate project contracts in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-estimate-project-contracts
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
      "description": "Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-estimate-project-contracts-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_estimate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 b3f55abf930df5cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_estimate_project_contracts_agent.py` first:

```bash
python3 audit_estimate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_estimate_project_contracts_agent.py   # or on stdin
python3 audit_estimate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate project contracts Completeness Audit — Runs a read-only completeness and policy audit of estimate project contracts in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-estimate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_estimate_project_contracts',
    "version": '3.0.2',
    "display_name": 'Estimate project contracts Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of estimate project contracts in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-estimate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-estimate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d7645178124c4ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/estimate-project-contracts'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-estimate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-estimate-project-contracts-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit estimate project contracts records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to estimate project contracts. Output an Excel workbook 'audit-estimate-project-contracts-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no estimate project contracts data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads estimate project contracts records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of estimate project contracts in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit estimate project contracts in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-estimate-project-contracts-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants estimate project contracts checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditEstimateProjectContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEstimateProjectContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-estimate-project-contracts-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditEstimateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
