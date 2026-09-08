---
name: "rar-cowork-cookbook-audit-merge-cases"
description: "Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_merge_cases", "rar_sha256": "cdf9bf8aff11e5b24ffca50f75a7785a77373e461b532f90a69d30fbbd57b458", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_merge_cases`. The original RAPP
agent is preserved byte-for-byte in `audit_merge_cases_agent.py` and in the RCI capsule.

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

Merge cases Completeness Audit — Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
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
      "description": "Name of the Excel workbook to produce, e.g. audit-merge-cases-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_merge_cases_agent.py` and embedded as the fenced Python below (sha256 cdf9bf8aff11e5b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_merge_cases_agent.py` first:

```bash
python3 audit_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_merge_cases_agent.py   # or on stdin
python3 audit_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Completeness Audit — Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_merge_cases',
    "version": '3.0.3',
    "display_name": 'Merge cases Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4540898d97c53d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-merge-cases-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit merge cases records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to merge cases. Output an Excel workbook 'audit-merge-cases-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no merge cases data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads merge cases records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of merge cases records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit merge cases in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-merge-cases-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants merge cases records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMergeCases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMergeCases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-merge-cases-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
