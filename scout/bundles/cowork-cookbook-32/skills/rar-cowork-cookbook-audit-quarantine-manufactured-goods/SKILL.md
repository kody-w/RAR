---
name: "rar-cowork-cookbook-audit-quarantine-manufactured-goods"
description: "Runs a read-only completeness and policy audit of quarantine manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_quarantine_manufactured_goods", "rar_sha256": "0c84b0c533ee2a56501224fd19d81975f7c46a7ddda461e8e425a718e665f21c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
