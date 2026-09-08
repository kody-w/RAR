---
name: "rar-cowork-cookbook-audit-define-human-resources-policies"
description: "Audits human resources policy records in Dynamics 365 F&SCM (read-only) for a given legal entity, flagging missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_human_resources_policies", "rar_sha256": "77f6daa3aeabbde1f47a718637be31a0e86e4c3234e4afa06a4e87d1fe3ae6d9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
