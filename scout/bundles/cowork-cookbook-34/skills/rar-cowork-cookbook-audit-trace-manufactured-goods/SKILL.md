---
name: "rar-cowork-cookbook-audit-trace-manufactured-goods"
description: "Runs a read-only completeness and policy audit of trace manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of count"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_trace_manufactured_goods", "rar_sha256": "517fe665072619cba778b9cc879a09348d97abce015d2b4fa3b393b9003d827f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_trace_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_trace_manufactured_goods_agent.py` and in the RCI capsule.

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

Trace manufactured goods Completeness Audit — Runs a read-only completeness and policy audit of trace manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of count

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-trace-manufactured-goods
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
      "description": "Name of the Excel workbook to produce, e.g. audit-trace-manufactured-goods-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_trace_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 517fe665072619cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_trace_manufactured_goods_agent.py` first:

```bash
python3 audit_trace_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_trace_manufactured_goods_agent.py   # or on stdin
python3 audit_trace_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Trace manufactured goods Completeness Audit — Runs a read-only completeness and policy audit of trace manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of count

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-trace-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_trace_manufactured_goods',
    "version": '3.0.3',
    "display_name": 'Trace manufactured goods Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of trace manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of count',
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
        "upstream_slug": 'audit-trace-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-trace-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7281b6ed7171a72e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/trace-manufactured-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-trace-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-trace-manufactured-goods-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit trace manufactured goods records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to trace manufactured goods. Output an Excel workbook 'audit-trace-manufactured-goods-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no trace manufactured goods data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads trace manufactured goods records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of trace manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of count', 'example_request': 'Audit trace manufactured goods in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-trace-manufactured-goods-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to audit trace manufactured goods records in D365 for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditTraceManufacturedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTraceManufacturedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-trace-manufactured-goods-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditTraceManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
