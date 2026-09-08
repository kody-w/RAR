---
name: "rar-cowork-cookbook-audit-inspect-inventory"
description: "Runs a read-only completeness and policy audit of inspect inventory records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_inspect_inventory", "rar_sha256": "68ced1da5de64c0717fe4777077d3db8de050a11b13845fc8fd246e6065043b0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
