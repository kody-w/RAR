---
name: "rar-cowork-cookbook-audit-implement-process-governance"
description: "Audits implement process governance records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_process_governance", "rar_sha256": "8ba2c7672a6f9c90139d7fc3d7ef094b0842b82775a72cbde469e2ba7e2a0df0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_implement_process_governance`. The original RAPP
agent is preserved byte-for-byte in `audit_implement_process_governance_agent.py` and in the RCI capsule.

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

Implement process governance Completeness Audit — Audits implement process governance records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-process-governance
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
      "description": "Date range for stale-date checks; adjust for demo data that is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-implement-process-governance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_process_governance_agent.py` and embedded as the fenced Python below (sha256 8ba2c7672a6f9c90…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_process_governance_agent.py` first:

```bash
python3 audit_implement_process_governance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_implement_process_governance_agent.py   # or on stdin
python3 audit_implement_process_governance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement process governance Completeness Audit — Audits implement process governance records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-process-governance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_implement_process_governance',
    "version": '3.0.3',
    "display_name": 'Implement process governance Completeness Audit',
    "description": 'Audits implement process governance records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-implement-process-governance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-implement-process-governance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '62ec7588fea71589',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-process-governance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-implement-process-governance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; adjust for demo data that is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-implement-process-governance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit implement process governance records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to implement process governance. Output an Excel workbook 'audit-implement-process-governance-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no implement process governance data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads implement process governance records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits implement process governance records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel', 'example_request': 'Audit implement process governance records in USMF for completeness and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; adjust for demo data that is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-implement-process-governance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of implement process governance records in Dynamics 365 F&SCM, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditImplementProcessGovernance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditImplementProcessGovernance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; adjust for demo data that is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-implement-process-governance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditImplementProcessGovernance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
