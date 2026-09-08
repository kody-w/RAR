---
name: "rar-cowork-cookbook-audit-analyze-inventory-levels"
description: "Audits Dynamics 365 F&SCM inventory-level records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_inventory_levels", "rar_sha256": "3e4bbc9113d7aae7c31a7f491c645085942bf326cd8342b1c553ae788fa788d7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_inventory_levels_agent.py` and in the RCI capsule.

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

Analyze inventory levels Completeness Audit — Audits Dynamics 365 F&SCM inventory-level records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-inventory-levels
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
      "description": "Name of the Excel workbook to produce, e.g. audit-analyze-inventory-levels-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 3e4bbc9113d7aae7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_inventory_levels_agent.py` first:

```bash
python3 audit_analyze_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_inventory_levels_agent.py   # or on stdin
python3 audit_analyze_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze inventory levels Completeness Audit — Audits Dynamics 365 F&SCM inventory-level records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_inventory_levels',
    "version": '3.0.2',
    "display_name": 'Analyze inventory levels Completeness Audit',
    "description": 'Audits Dynamics 365 F&SCM inventory-level records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-analyze-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6c498b395d16a53',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/analyze-inventory-levels'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-analyze-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-analyze-inventory-levels-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze inventory levels records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze inventory levels. Output an Excel workbook 'audit-analyze-inventory-levels-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze inventory levels data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze inventory levels records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits Dynamics 365 F&SCM inventory-level records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit inventory levels in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-inventory-levels-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of D365 inventory-level records and an Excel findings workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeInventoryLevels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeInventoryLevels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-inventory-levels-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
