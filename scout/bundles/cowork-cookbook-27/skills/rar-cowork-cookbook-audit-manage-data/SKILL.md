---
name: "rar-cowork-cookbook-audit-manage-data"
description: "Audits Dynamics 365 F&SCM manage data records in a given legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_data", "rar_sha256": "4aa7ddd85d768e6490895ab1a2795109dddfcd79320197b898eb31f9df773bd9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_data`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_data_agent.py` and in the RCI capsule.

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

Manage data Completeness Audit — Audits Dynamics 365 F&SCM manage data records in a given legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit work

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-data
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
      "description": "Date range used to judge stale dates; adjust for demo data vintage (e.g. FY2017 for USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-manage-data-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_data_agent.py` and embedded as the fenced Python below (sha256 4aa7ddd85d768e64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_data_agent.py` first:

```bash
python3 audit_manage_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_data_agent.py   # or on stdin
python3 audit_manage_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data Completeness Audit — Audits Dynamics 365 F&SCM manage data records in a given legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit work

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_data',
    "version": '3.0.3',
    "display_name": 'Manage data Completeness Audit',
    "description": 'Audits Dynamics 365 F&SCM manage data records in a given legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit work',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-manage-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51ff97f0cdd12bbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-manage-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data vintage (e.g. FY2017 for USMF).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-manage-data-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage data records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage data. Output an Excel workbook 'audit-manage-data-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage data data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads manage data records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits Dynamics 365 F&SCM manage data records in a given legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit work', 'example_request': 'Audit manage data in USMF for completeness and give me audit-manage-data-2026-05-24.xlsx', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data vintage (e.g. FY2017 for USMF).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-data-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of D365 manage data records delivered as a multi-sheet Excel workbook with a summary count sheet.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data vintage (e.g. FY2017 for USMF).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-manage-data-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
