---
name: "rar-cowork-cookbook-audit-trace-manufactured-goods"
description: "Runs a read-only completeness and policy audit of trace manufactured goods records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of count"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_trace_manufactured_goods", "rar_sha256": "517fe665072619cba778b9cc879a09348d97abce015d2b4fa3b393b9003d827f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
