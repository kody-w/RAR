---
name: "rar-cowork-cookbook-audit-label-received-goods"
description: "Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_label_received_goods", "rar_sha256": "0b67ace1985b0f058e76b87d35ffeec607e0ce56455b0b6f75770e5512be38ae", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_label_received_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_label_received_goods_agent.py` and in the RCI capsule.

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

Label received goods Completeness Audit — Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-label-received-goods
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
      "description": "Date range to treat as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-label-received-goods-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_label_received_goods_agent.py` and embedded as the fenced Python below (sha256 0b67ace1985b0f05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_label_received_goods_agent.py` first:

```bash
python3 audit_label_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_label_received_goods_agent.py   # or on stdin
python3 audit_label_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Label received goods Completeness Audit — Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-label-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_label_received_goods',
    "version": '3.0.3',
    "display_name": 'Label received goods Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-label-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-label-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06d33612d5c026b2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/label-received-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-label-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-label-received-goods-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit label received goods records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to label received goods. Output an Excel workbook 'audit-label-received-goods-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no label received goods data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads label received goods records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of label received goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit label received goods in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-label-received-goods-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants label received goods records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditLabelReceivedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditLabelReceivedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-label-received-goods-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditLabelReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
