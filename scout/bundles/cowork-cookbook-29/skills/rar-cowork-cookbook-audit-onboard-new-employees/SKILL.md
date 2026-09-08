---
name: "rar-cowork-cookbook-audit-onboard-new-employees"
description: "Read-only audit of onboarding-new-employee records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_employees", "rar_sha256": "ef42cab25efe297372c7b2e66722969d9e41aaae5bde9489d6598a04c27d26f8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_onboard_new_employees`. The original RAPP
agent is preserved byte-for-byte in `audit_onboard_new_employees_agent.py` and in the RCI capsule.

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

Onboard new employees Completeness Audit — Read-only audit of onboarding-new-employee records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-employees
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
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
      "description": "Excel workbook name, e.g. audit-onboard-new-employees-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_employees_agent.py` and embedded as the fenced Python below (sha256 ef42cab25efe2973…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_employees_agent.py` first:

```bash
python3 audit_onboard_new_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_employees_agent.py   # or on stdin
python3 audit_onboard_new_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new employees Completeness Audit — Read-only audit of onboarding-new-employee records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_employees',
    "version": '3.0.3',
    "display_name": 'Onboard new employees Completeness Audit',
    "description": 'Read-only audit of onboarding-new-employee records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning',
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
        "upstream_slug": 'audit-onboard-new-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6a04e6e99e7b6607',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-onboard-new-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-onboard-new-employees-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit onboard new employees records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to onboard new employees. Output an Excel workbook 'audit-onboard-new-employees-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no onboard new employees data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads onboard new employees records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of onboarding-new-employee records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning', 'example_request': 'Audit onboarding records in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-onboard-new-employees-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance audit of onboarding records in a D365 legal entity, delivered as an Excel workbook without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditOnboardNewEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-onboard-new-employees-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditOnboardNewEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
