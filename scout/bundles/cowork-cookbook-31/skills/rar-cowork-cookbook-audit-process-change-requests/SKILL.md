---
name: "rar-cowork-cookbook-audit-process-change-requests"
description: "Runs a read-only completeness and policy audit of Dynamics 365 process change request records for a given legal entity and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_change_requests", "rar_sha256": "c9fe7a01d8258797d845ef53fcc77fec4f2922f1648c57c7824119bc724b8f4c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
