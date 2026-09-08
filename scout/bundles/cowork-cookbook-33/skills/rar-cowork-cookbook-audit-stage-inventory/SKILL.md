---
name: "rar-cowork-cookbook-audit-stage-inventory"
description: "Runs a read-only completeness and policy audit of stage inventory records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_stage_inventory", "rar_sha256": "d4c12d99ea018a282957808d685fbc59b87e4dc2984c74ff76ac0db793783dad", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_stage_inventory`. The original RAPP
agent is preserved byte-for-byte in `audit_stage_inventory_agent.py` and in the RCI capsule.

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

Stage inventory Completeness Audit — Runs a read-only completeness and policy audit of stage inventory records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-stage-inventory
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
      "description": "Date range used to judge stale dates; adjust for demo data eras such as FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-stage-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_stage_inventory_agent.py` and embedded as the fenced Python below (sha256 d4c12d99ea018a28…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_stage_inventory_agent.py` first:

```bash
python3 audit_stage_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_stage_inventory_agent.py   # or on stdin
python3 audit_stage_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stage inventory Completeness Audit — Runs a read-only completeness and policy audit of stage inventory records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-stage-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_stage_inventory',
    "version": '3.0.3',
    "display_name": 'Stage inventory Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of stage inventory records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-stage-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-stage-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '991f78e0100931f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/stage-inventory'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-stage-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-stage-inventory-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit stage inventory records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to stage inventory. Output an Excel workbook 'audit-stage-inventory-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no stage inventory data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads stage inventory records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of stage inventory records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit stage inventory in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-stage-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants stage inventory records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditStageInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditStageInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-stage-inventory-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditStageInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
