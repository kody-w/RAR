---
name: "rar-cowork-cookbook-audit-stage-inventory"
description: "Runs a read-only completeness and policy audit of stage inventory records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_stage_inventory", "rar_sha256": "d4c12d99ea018a282957808d685fbc59b87e4dc2984c74ff76ac0db793783dad", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
