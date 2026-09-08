---
name: "rar-cowork-cookbook-audit-onboard-new-employees"
description: "Read-only audit of onboarding-new-employee records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) that flags missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_employees", "rar_sha256": "ef42cab25efe297372c7b2e66722969d9e41aaae5bde9489d6598a04c27d26f8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
