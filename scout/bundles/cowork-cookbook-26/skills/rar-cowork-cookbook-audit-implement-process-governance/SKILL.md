---
name: "rar-cowork-cookbook-audit-implement-process-governance"
description: "Audits implement process governance records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_process_governance", "rar_sha256": "8ba2c7672a6f9c90139d7fc3d7ef094b0842b82775a72cbde469e2ba7e2a0df0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
