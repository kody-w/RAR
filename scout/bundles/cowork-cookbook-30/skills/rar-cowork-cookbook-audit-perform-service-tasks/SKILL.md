---
name: "rar-cowork-cookbook-audit-perform-service-tasks"
description: "Runs a read-only completeness and policy audit of perform service tasks records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_service_tasks", "rar_sha256": "fe1f4f29205f4ebda169eaa205ac56ba8580a3ac89cb2095630cefeea5d5fe30", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_perform_service_tasks`. The original RAPP
agent is preserved byte-for-byte in `audit_perform_service_tasks_agent.py` and in the RCI capsule.

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

Perform service tasks Completeness Audit — Runs a read-only completeness and policy audit of perform service tasks records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-service-tasks
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
      "description": "Name of the Excel workbook to produce, e.g. audit-perform-service-tasks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_service_tasks_agent.py` and embedded as the fenced Python below (sha256 fe1f4f29205f4ebd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_service_tasks_agent.py` first:

```bash
python3 audit_perform_service_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_perform_service_tasks_agent.py   # or on stdin
python3 audit_perform_service_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform service tasks Completeness Audit — Runs a read-only completeness and policy audit of perform service tasks records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-service-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_perform_service_tasks',
    "version": '3.0.3',
    "display_name": 'Perform service tasks Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of perform service tasks records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-perform-service-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-perform-service-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6db2da15a8a947dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/perform-service-tasks'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-perform-service-tasks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-perform-service-tasks-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit perform service tasks records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to perform service tasks. Output an Excel workbook 'audit-perform-service-tasks-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no perform service tasks data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform service tasks records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of perform service tasks records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun', 'example_request': 'Audit perform service tasks in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-perform-service-tasks-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants perform service tasks records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPerformServiceTasks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPerformServiceTasks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-perform-service-tasks-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPerformServiceTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
