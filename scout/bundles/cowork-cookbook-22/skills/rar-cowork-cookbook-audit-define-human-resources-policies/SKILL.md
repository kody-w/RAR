---
name: "rar-cowork-cookbook-audit-define-human-resources-policies"
description: "Audits human resources policy records in Dynamics 365 F&SCM (read-only) for a given legal entity, flagging missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_human_resources_policies", "rar_sha256": "77f6daa3aeabbde1f47a718637be31a0e86e4c3234e4afa06a4e87d1fe3ae6d9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_human_resources_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_define_human_resources_policies_agent.py` and in the RCI capsule.

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

Define human resources policies Completeness Audit — Audits human resources policy records in Dynamics 365 F&SCM (read-only) for a given legal entity, flagging missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, and

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-human-resources-policies
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
      "description": "Dynamics 365 legal entity code to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-human-resources-policies-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_human_resources_policies_agent.py` and embedded as the fenced Python below (sha256 77f6daa3aeabbde1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_human_resources_policies_agent.py` first:

```bash
python3 audit_define_human_resources_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_human_resources_policies_agent.py   # or on stdin
python3 audit_define_human_resources_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define human resources policies Completeness Audit — Audits human resources policy records in Dynamics 365 F&SCM (read-only) for a given legal entity, flagging missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, and

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-human-resources-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_human_resources_policies',
    "version": '3.0.2',
    "display_name": 'Define human resources policies Completeness Audit',
    "description": 'Audits human resources policy records in Dynamics 365 F&SCM (read-only) for a given legal entity, flagging missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, and',
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
        "upstream_slug": 'audit-define-human-resources-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-human-resources-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '178db401edcbe045',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-human-resources-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-define-human-resources-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity code to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-human-resources-policies-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define human resources policies records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define human resources policies. Output an Excel workbook 'audit-define-human-resources-policies-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define human resources policies data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define human resources policies records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits human resources policy records in Dynamics 365 F&SCM (read-only) for a given legal entity, flagging missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, and', 'example_request': 'Audit HR policy records in D365 for legal entity USMF and give me an Excel completeness audit workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity code to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-human-resources-policies-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of HR policy records in Dynamics 365 F&SCM, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineHumanResourcesPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineHumanResourcesPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo tenants where data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity code to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-human-resources-policies-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineHumanResourcesPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
