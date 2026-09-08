---
name: "rar-cowork-cookbook-audit-define-leasing-policies"
description: "Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_leasing_policies", "rar_sha256": "6266a116bcddc87a90003f128db19f7c1249998137f95d762900c769158d028e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_leasing_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_define_leasing_policies_agent.py` and in the RCI capsule.

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

Define leasing policies Completeness Audit — Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-leasing-policies
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
      "description": "Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-leasing-policies-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_leasing_policies_agent.py` and embedded as the fenced Python below (sha256 6266a116bcddc87a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_leasing_policies_agent.py` first:

```bash
python3 audit_define_leasing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_leasing_policies_agent.py   # or on stdin
python3 audit_define_leasing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define leasing policies Completeness Audit — Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-leasing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_leasing_policies',
    "version": '3.0.2',
    "display_name": 'Define leasing policies Completeness Audit',
    "description": 'Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-leasing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-leasing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bddf356904ffb19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-leasing-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-define-leasing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-leasing-policies-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define leasing policies records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define leasing policies. Output an Excel workbook 'audit-define-leasing-policies-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define leasing policies data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads define leasing policies records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits leasing policy records in Dynamics 365 F&SCM (read-only) for missing required fields, stale dates, blank descriptions, inactive entity references, and policy violations, returning an Excel workbook with one sheet', 'example_request': 'Audit define leasing policies in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-leasing-policies-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'name': 'date_window'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of define leasing policies records in a D365 legal entity, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineLeasingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineLeasingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-leasing-policies-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineLeasingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
