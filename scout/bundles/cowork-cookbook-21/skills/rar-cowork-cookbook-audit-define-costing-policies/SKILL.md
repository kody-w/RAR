---
name: "rar-cowork-cookbook-audit-define-costing-policies"
description: "Read-only audit of define costing policies records in Dynamics 365 F&SCM for a given legal entity; returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_costing_policies", "rar_sha256": "0b363f2f5cc190b1cc0b6b44f08f8d070fdd2865db91b13be8735ed8d0a0e6ca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
