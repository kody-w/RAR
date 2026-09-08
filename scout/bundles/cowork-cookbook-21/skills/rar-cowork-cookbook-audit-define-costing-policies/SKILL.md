---
name: "rar-cowork-cookbook-audit-define-costing-policies"
description: "Read-only audit of define costing policies records in Dynamics 365 F&SCM for a given legal entity; returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_costing_policies", "rar_sha256": "0b363f2f5cc190b1cc0b6b44f08f8d070fdd2865db91b13be8735ed8d0a0e6ca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_costing_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_define_costing_policies_agent.py` and in the RCI capsule.

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

Define costing policies Completeness Audit — Read-only audit of define costing policies records in Dynamics 365 F&SCM for a given legal entity; returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-costing-policies
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-costing-policies-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_costing_policies_agent.py` and embedded as the fenced Python below (sha256 0b363f2f5cc190b1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_costing_policies_agent.py` first:

```bash
python3 audit_define_costing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_costing_policies_agent.py   # or on stdin
python3 audit_define_costing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define costing policies Completeness Audit — Read-only audit of define costing policies records in Dynamics 365 F&SCM for a given legal entity; returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-costing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_costing_policies',
    "version": '3.0.2',
    "display_name": 'Define costing policies Completeness Audit',
    "description": 'Read-only audit of define costing policies records in Dynamics 365 F&SCM for a given legal entity; returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-define-costing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-costing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f0857e930f896c0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-costing-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-define-costing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-costing-policies-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define costing policies records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define costing policies. Output an Excel workbook 'audit-define-costing-policies-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define costing policies data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads define costing policies records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of define costing policies records in Dynamics 365 F&SCM for a given legal entity; returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit define costing policies in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-costing-policies-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants define costing policies records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineCostingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineCostingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-costing-policies-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineCostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
