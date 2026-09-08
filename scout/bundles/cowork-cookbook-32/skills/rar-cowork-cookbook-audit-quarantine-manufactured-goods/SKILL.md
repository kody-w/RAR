---
name: "rar-cowork-cookbook-audit-quarantine-manufactured-goods"
description: "Runs a read-only completeness and policy audit of quarantine manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_quarantine_manufactured_goods", "rar_sha256": "0c84b0c533ee2a56501224fd19d81975f7c46a7ddda461e8e425a718e665f21c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_quarantine_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_quarantine_manufactured_goods_agent.py` and in the RCI capsule.

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

Quarantine manufactured goods Completeness Audit — Runs a read-only completeness and policy audit of quarantine manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods
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
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit; defaults to USMF.",
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
      "description": "Excel workbook name, e.g. audit-quarantine-manufactured-goods-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_quarantine_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 0c84b0c533ee2a56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_quarantine_manufactured_goods_agent.py` first:

```bash
python3 audit_quarantine_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_quarantine_manufactured_goods_agent.py   # or on stdin
python3 audit_quarantine_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine manufactured goods Completeness Audit — Runs a read-only completeness and policy audit of quarantine manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_quarantine_manufactured_goods',
    "version": '3.0.3',
    "display_name": 'Quarantine manufactured goods Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of quarantine manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-quarantine-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-quarantine-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c5a78abec0ce302',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/quarantine-manufactured-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-quarantine-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Excel workbook name, e.g. audit-quarantine-manufactured-goods-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit quarantine manufactured goods records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to quarantine manufactured goods. Output an Excel workbook 'audit-quarantine-manufactured-goods-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no quarantine manufactured goods data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads quarantine manufactured goods records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of quarantine manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit quarantine manufactured goods in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-quarantine-manufactured-goods-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants quarantine manufactured goods records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditQuarantineManufacturedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditQuarantineManufacturedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-quarantine-manufactured-goods-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditQuarantineManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
