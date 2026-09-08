---
name: "rar-cowork-cookbook-audit-analyze-inventory-levels"
description: "Audits Dynamics 365 F&SCM inventory-level records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_inventory_levels", "rar_sha256": "3e4bbc9113d7aae7c31a7f491c645085942bf326cd8342b1c553ae788fa788d7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
