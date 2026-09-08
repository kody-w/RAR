---
name: "rar-cowork-cookbook-audit-perform-service-tasks"
description: "Runs a read-only completeness and policy audit of perform service tasks records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of coun"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_service_tasks", "rar_sha256": "fe1f4f29205f4ebda169eaa205ac56ba8580a3ac89cb2095630cefeea5d5fe30", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
