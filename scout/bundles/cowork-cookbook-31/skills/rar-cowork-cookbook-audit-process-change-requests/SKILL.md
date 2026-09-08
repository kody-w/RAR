---
name: "rar-cowork-cookbook-audit-process-change-requests"
description: "Runs a read-only completeness and policy audit of Dynamics 365 process change request records for a given legal entity and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_change_requests", "rar_sha256": "c9fe7a01d8258797d845ef53fcc77fec4f2922f1648c57c7824119bc724b8f4c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_change_requests`. The original RAPP
agent is preserved byte-for-byte in `audit_process_change_requests_agent.py` and in the RCI capsule.

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

Process change requests Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 process change request records for a given legal entity and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-change-requests
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
      "description": "Name of the Excel workbook to produce, e.g. audit-process-change-requests-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_change_requests_agent.py` and embedded as the fenced Python below (sha256 c9fe7a01d8258797…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_change_requests_agent.py` first:

```bash
python3 audit_process_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_change_requests_agent.py   # or on stdin
python3 audit_process_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change requests Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 process change request records for a given legal entity and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_change_requests',
    "version": '3.0.3',
    "display_name": 'Process change requests Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of Dynamics 365 process change request records for a given legal entity and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f473ce3f144cea5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-process-change-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-process-change-requests-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit process change requests records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to process change requests. Output an Excel workbook 'audit-process-change-requests-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no process change requests data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process change requests records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of Dynamics 365 process change request records for a given legal entity and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit process change requests in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-process-change-requests-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants process change request records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProcessChangeRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessChangeRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-process-change-requests-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProcessChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
