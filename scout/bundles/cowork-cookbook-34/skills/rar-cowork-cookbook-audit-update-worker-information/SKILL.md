---
name: "rar-cowork-cookbook-audit-update-worker-information"
description: "Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_update_worker_information", "rar_sha256": "c6f5ed36ae5a4a99870807d9e84301c622829e1912e6b36ec5d9458f375247c9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_update_worker_information`. The original RAPP
agent is preserved byte-for-byte in `audit_update_worker_information_agent.py` and in the RCI capsule.

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

Update worker information Completeness Audit — Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-update-worker-information
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
      "description": "Name of the Excel workbook to produce, e.g. audit-update-worker-information-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 c6f5ed36ae5a4a99…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_update_worker_information_agent.py` first:

```bash
python3 audit_update_worker_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_update_worker_information_agent.py   # or on stdin
python3 audit_update_worker_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update worker information Completeness Audit — Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-update-worker-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_update_worker_information',
    "version": '3.0.3',
    "display_name": 'Update worker information Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet.',
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
        "upstream_slug": 'audit-update-worker-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-update-worker-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '196b762a7284217d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/update-worker-information'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-update-worker-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-update-worker-information-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit update worker information records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to update worker information. Output an Excel workbook 'audit-update-worker-information-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no update worker information data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update worker information records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of update worker information records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook of findings by category plus a summary sheet.', 'example_request': 'Audit update worker information records in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-update-worker-information-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants update worker information records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditUpdateWorkerInformation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditUpdateWorkerInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-update-worker-information-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditUpdateWorkerInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
