---
name: "rar-cowork-cookbook-audit-manage-data"
description: "Audits Dynamics 365 F&SCM manage data records in a given legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_data", "rar_sha256": "4aa7ddd85d768e6490895ab1a2795109dddfcd79320197b898eb31f9df773bd9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
