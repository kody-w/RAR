---
name: "rar-cowork-cookbook-audit-inspect-inventory"
description: "Runs a read-only completeness and policy audit of inspect inventory records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_inspect_inventory", "rar_sha256": "68ced1da5de64c0717fe4777077d3db8de050a11b13845fc8fd246e6065043b0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_inspect_inventory`. The original RAPP
agent is preserved byte-for-byte in `audit_inspect_inventory_agent.py` and in the RCI capsule.

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

Inspect inventory Completeness Audit — Runs a read-only completeness and policy audit of inspect inventory records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-inspect-inventory
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
      "description": "Date range used to judge stale records; adjust for demo data vintage (USMF is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-inspect-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_inspect_inventory_agent.py` and embedded as the fenced Python below (sha256 68ced1da5de64c07…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_inspect_inventory_agent.py` first:

```bash
python3 audit_inspect_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_inspect_inventory_agent.py   # or on stdin
python3 audit_inspect_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect inventory Completeness Audit — Runs a read-only completeness and policy audit of inspect inventory records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-inspect-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_inspect_inventory',
    "version": '3.0.3',
    "display_name": 'Inspect inventory Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of inspect inventory records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-inspect-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-inspect-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e465a4c01497b891',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/inspect-inventory'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-inspect-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; adjust for demo data vintage (USMF is mostly FY2017).', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-inspect-inventory-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit inspect inventory records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to inspect inventory. Output an Excel workbook 'audit-inspect-inventory-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no inspect inventory data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads inspect inventory records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of inspect inventory records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit inspect inventory in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; adjust for demo data vintage (USMF is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-inspect-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants inspect inventory records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditInspectInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditInspectInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; adjust for demo data vintage (USMF is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-inspect-inventory-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditInspectInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
