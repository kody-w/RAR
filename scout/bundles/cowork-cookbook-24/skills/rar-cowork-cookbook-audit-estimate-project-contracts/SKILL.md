---
name: "rar-cowork-cookbook-audit-estimate-project-contracts"
description: "Runs a read-only completeness and policy audit of estimate project contracts in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_estimate_project_contracts", "rar_sha256": "b3f55abf930df5cc71f4f5ef30576786958a850df144f7525653dc2c2af31011", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
