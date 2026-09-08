---
name: "rar-cowork-cookbook-audit-audit-financial-transactions"
description: "Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_financial_transactions", "rar_sha256": "d5615d7ae6488bf11ec537ed399d08d2e6084f73d3060036cb7299e805b888a8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_audit_financial_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_audit_financial_transactions_agent.py` and in the RCI capsule.

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

Audit financial transactions Completeness Audit — Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-financial-transactions
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
      "description": "Name of the Excel workbook to produce, e.g. audit-audit-financial-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 d5615d7ae6488bf1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_audit_financial_transactions_agent.py` first:

```bash
python3 audit_audit_financial_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_audit_financial_transactions_agent.py   # or on stdin
python3 audit_audit_financial_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial transactions Completeness Audit — Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-financial-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_audit_financial_transactions',
    "version": '3.0.2',
    "display_name": 'Audit financial transactions Completeness Audit',
    "description": 'Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-audit-financial-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-audit-financial-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8016fcdb344728d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-audit-financial-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-audit-financial-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit audit financial transactions records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to audit financial transactions. Output an Excel workbook 'audit-audit-financial-transactions-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no audit financial transactions data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads audit financial transactions records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb', 'example_request': 'Audit financial transactions in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-audit-financial-transactions-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance review of D365 financial transactions with an Excel findings workbook and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAuditFinancialTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAuditFinancialTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-audit-financial-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAuditFinancialTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWJbnV9G8jpjMamyDACFwR0UMCCEJxCJAgChXONn3fZVy6rvPRXp2Oquzurom5q+Rww8B9579/M45gl/fnKGPq/bt85sWOOXq4OR5Egftyin91a6aqjYDhypzwf+VV5V9m7hDX7Xd24c3P+i8Nqn7pCrBdjVw/I9Vmd9XzuAn/aoKV2FSOqWXOPmqb52yc7xl6aoNvKr1u1VSrpwVey+dIvG6FUZsVtz/1HbiKg8isCMo+6S/f1iFuRNFSRmtiqTrlmOYBLnffVh1vZMHK9/pA3Di5k6ZrX4QCFwDzAHDMfj4IgX4hkEblN6yftGurvLEu6/GpMqd9y3V0NdDv3I6sGC1n70gXy0WcIGywewUdR50b5//8tcPbwn4/vb51zcvdzpw6Y1eVH7+4b7prP+m8mIsIGAEFtZ3YO0SnNdBG1ZtAS75Qbh6P/u5C/Lww+rf/z2bnDbq/vT5S7l6/3x5W/6pQ7nq42DVV07XB/7Kc2rHTXKg3qcVnU/OvQNq9kNbAg2AhVpgsE+vnb9RqurVn5d7P7+YfIqC/ucvbxUQ4WmGL29/WlUt4NcOy/dPC5X65z99yqspaH/+0290usFNA69fiAGpP319P38nCxb+tjQJV181Zb975wUiIKkDQPwH/ZbPS/R3cu8m+fpa/HNVf1j9MeVFnz8DeV/edwHdPyYLbAB2vn1Kq6T8+Z1HW43B4q/g5z/9I7JeHHhZnnT9f4vuX16EY5AMwFrvJvnTh6f7/rqC3nX7TvMfs61BwPwrmoDl39h9N9Q/ov307N+RzpMy6L778g/J/dEG6M+rv/xD3f6rDSCzv7yxQQ4StHXcPPi8+vUZIn/5yf/t4k9//Rsg/U/JaNXQek8KXwunTMKg679+/ctP3fPyT3/9y09DDaI4cIqvQ5v/Ec0/suuTz+8s+L7q59/vBfyvZVZWU7n6nkOrX6v6f7R/+7QynDzxf7vefV79mInLB1otSnxj+jLBD9nYAVl/sOOf3v4GwKcE2gzvyPL57d/+bSUmXlt1VdivNA9g2Ao4uE+KYBFejxMAtd0TNdoA2LVLgGHf14H4Xzy8SAzg+pf/5T0B/6P3DvjwE8m/vv5+B/OvP4B598unlQ4oV20CQBrAtkorypfSiQDmLlzrNuiCdgRI5d774CNI6I/LlwX7f/nnxL8+6Xyq7788ATt5YZ+6Oy241w158GnR0IyD8l0fD8B2MAfeAFjklQfkCZN8wXsgRpWPADcXa3RZkucrPwHIAirZ/UkbWOzzQuyXX35xnS7+Ur6AGlu9KkoHgwXfxVl9/AgUC/MkivsvZeDF1eqnX//20+p/r/6rXU/iCw8F1Ix3fwAJeU2WViC/hgIsW6oiAHbHf/rj17+9mxeQKUFNBt5LQPl7bQbxmQX+N1trR/ojuiFWbgBsDOxb1FXbL+Uy6T+tTuHqu7yA6XJrqQ9x1fWgZtZB6YOyeAdUHaDOd0uWVb/qQBB2ISjDQxc8uf7its5TxAIkutP/shJ3CqhGFSjx1SLmcxHYXJUJMP/3SHhdB0Tan7oV843Ep5W0ROSqdlqnjlvnnUfovPwCqtC37YC4syqD6Uu5VN5gMdUzPV7mAYuAZbx3l35cfA56lQJgwavN6L+tcZaaqT9rZ/ul7N5D32mDZ1MCRLmvoiHxl4LwH+8h1cXVkPtP+wFJF0rvXvDfvfKMwWfp/+N+pwP90yJzDwQAfn+t/DKgyBpf/f/cMz3Ncjio+wOt79nVXtLV28tdSxu5uPXVeS5sQMy+UvO3fuYbZn2D7i9lnoDYa+//8Vr5dPL7mhccDi3wiUqrT/ogwoC7FrrPBFgCum2X1HG+lN9qBFBp9QREYGCAFiCbliD+xnC5+03SGEDCcv5bv/DukcUoIMhX9eACw6zCIPBdx8uAVO2SxO9uBtkQLL6d4sSLf6fV4jIQdID+CgiRgLQEdeTTd9x+3f0m+u82vtqiZcuzZRxADrdPAkCOxWFPd01JD6DM6V9dO9Dz85MIUKOo+0V3F3gRaPq6CDzdDEmXPKPjZdegBnj9cTm+NF2uBnMNEgcY6+X5T6+EeoYbaHqADCCmQH4VSQmaAGCUdyM8CTrFgg4Afd+71BfF5+V3hYJnFi7V69vGRZFlz9IQrEIgOrhy/xFE9D8KE0CvWFY8+f59pH3nttBegLQDYAg4frv76hw+vYr/q7tYfaP7+T+NRT//a5PTs5xffx8An1dx39fdZxh+leBvFfgTgDH4JWv3qsYfX3+/w8THH6Hmd5RfSn9e/WvS/Y7Ee3Z8Xq0/IZ+Q5db5PbreP8AYu4/M7SO+3P1SqsFvMAvYVwUIr8V1d1D+v9fEb0tAYYxagFtg8atGdktpnUA1fxYF4Icv5Y/hvqQbqDlltIRnV/0AA8/mAIT+y23faxe4VfaAt7+0k1HwaZnCFvG74O1zOeT5hzeAo8F/a3pbKlSxRHW3TH0gf0B/1ifB8+wJEnO/fP39RCw/vzj5pxUbAEDKux8j772uLHX1hwR5qQnU8wCHDy+kXuogUHNhviSX04FoBYG6qNPf60X+16C3tIbLhq9TUvrV9J/lYcHNVbsYcMG5xa5P2PaGtl1Abuxe9eE/VldN5EASF9UigLOgbAFaBWBJ7gYk3f4h52cF+voqG3/AeilVPxapRYJnJH9YBZ+iT0+Wf0j3eyf8n4maoAFZ6PjV56UWf3jHNXAEle3D6vsg8mH1bTRcOATlAKbuvyxD0OLY55blC9gDDt83ff99ww3e/vpHcj3B7+sSf68o+nvppAXUAOgvbv2hLC75BmQGfP3BC961/+eZ/RFFUOIjsvmI4p/mvJv/wFZAqCeAgzK46Peb4X4Tv3oOdIv4QN3+9fvDr28gsJ3F0e+h/T4RgOUA7z52SxcEg/wHDMH5K1PBvf+LWeGdQhc7oFNdfvjYEOuNv3UCAidJN1yvA2+DbQMfoygfIX00IBASD7eYjyEEgmCE525RigpIZOOSJOmQgN4r478uzV6ySLWIBIwBTBcEv90Gl/x3dV7iL7b6Pposar9r9eubS+Bg5RHvTvTrs4OptQuhW/cuWbCFkPNx6q/XZFTR4J7HPk+ioipz0cHBPFbu8wSnUzFR57PFiWU+3zbNQY5Zii63vIL64kO5ZsKp46kR6bK9pkG6WOhKCaV9OdfbkrW3xtW487b9EKTTnJ+aelc3V7F5xGcNOzhuyO8NrTZsrUTuR5jcBnBiiXlVNBZvZDGUJ9h2d4t3sZGpucbLsaqW6Fod8Ja+lhi8rq10Q+Cjvr7zqkDOF0c1LBTPb3wprJNeNoAuuaZDVndtEi85C1piC+qZ16Azf7KPVX7KzYNqT49iVi71ZI5rQ9Ontj4bToTUyv6eXrWAtw445/tznkUP3hnaUSD2Z5ajx2MUNpnu2aJl3FIGpzoE29whKAhddLZznAwwl5wpkrScXuWTPKPFYi1dCQFNVNtwTk6MWqda21jihVc8GdtVCqA9CbwesDyHX7s+gpCLbImuHccFQx8Ne11p/AwPd+/udbhxMfVU68NRqOlhFyfMBT8eNuVBWxsmeiJwIzP4KUPvJN08GmK2037jKH1wtyQFG8Vk4IL8cDDRy4W2cSsho/2Wuwp5eyLpioyu5z2RoQ+D52SXsufhsO3jtWq4pwKlaWmOVRJrdPI2CpZPWIG5oW5IyzzKJHEqm81UX23qqAlYxjjpApQVbX9jTcPgRiHmNV0u6BDHgqvpWhmzRgUe2ikWZIh+/tg58QZ0Q4R52tY2RKpWU2GD17Q7OmvNdSXWUj5rt+IEnY5+rtW3WC5FlTiOx67g0/Ay7CfNo3G/DswoMBu06tiLUdHxbMuncK5GjmKnffJI78aNPBOMJp51le+19a5nHYRmgq7orce13stVqTdroROJucA2tm3dLkIXh0mUkoKGXQ/93dDnCu6cioNvpRbfZD2MzhTOent9DvCLGHdmyDnXG8WSY4PNhRFbhrGV9WyzK+PECSzi5l5xpIKuPIPLNdxCPLMWseqc7KmbXeKdhHv37KZuEv4Bz0c4kUnIkWd+FI9RmvjKSMVQZARstzV2xaHLDhfJZFt34uvTbT3MKF35Glnp8l2lT7vqUjzo2/F+2CEdhJF0QM7NKYNxrkUh1cCNphAe54NYyl7p2qzfEGtGlXiEmDTeIHLOduT9WRY4V69O6kmJuh0RqLtTDfHohR+ne0lLIswVoDfPygyyS1XpUH6sqClpdgV0tNBR0oV107PVDragNO0YY6Z2F/F0yoSaYvMT3JP3aCARdaC3456BHCHupsGIZcPCzmjHjeacoVtYZx/9KLaDVs0QdrrV6710obqDbduTwczyfGTUGy5ePJyNdrvNOWjclD+imjnaSSNfLYPLLw07tRBXeNd21q+XeUZlqL3krZDZ3J3eZcemS44eKV0S5dC2Uqrl9bRhPRFe2yftxrFc0npShjdxJCbQBmP8huUvhG70rrS9qQ1xYR2GnNURHZNbq6zLkxgRawLLC0KA98XdMaBA8EECMpyotE3pZ5ekm6zTbgMHF1bU55jCr49DcXIR+XzFAz2/xV7aiTyy68hzizDODOrC4KQpL5yvHMphuUl6+RFxH4fhuA7rEY+CYLyvG8kvKASS2YLDJRnBtxhDlaVDpVKKpMRdiKPQ3ztloOVXCrjQFDYxomBbTE8JmCCVx2XAab3UU3AUb8pGdZTUNantpLRsOTiTSEeSeibi0UFuqepUCQ0q3qM7GdeOZ/UrfCQZnONmIfbuyOkYMDl/YrTdmRSYMypKu1Y46cG4brYBxJTV4XjPeFe45uJ9ku51jkQXlCnsc+3zjBjhIZqnV16j9xY91JcuEct9ZvQebe+LOl6X5C5A7jFo0429erL89iEJxsbypGibBVMkGql+oXpWpaKmXU+j6VU53T/4eTtoiH25lslddUuGNeWwTBtKtLA1QSLyvn5sGYXhTaVCKkQYM0jbKtKxugYCctllOx8dFSpNbgy2oWJG3hCXy9WEQ1i3DbKbzPIBzWoAB/C8PZCtyAsQ/2Afj9C7mvGRPqD2OYw2gyUmmcH4Bj7cHqzcFOhE5RCzJ6K6u0E0tuPEGxkq4aaBhvRMBOLoeFrRJvGGcS9sjE7yiK83wwlzrojeC1ejLy9kJV1UjqmusmBblcyCEaLJeQaTysPO9LB8X4q1xVMNLJB+7HHXXXyY2j0P+wS5nsqTHTs3RTl6ki1fFW1ABzdzM1xwsAnOKdOxhvWDujE3Oq3ymbOD+Zrvim3nxz1z6+P8Dsccqx1cJoBu+7YzYtuqNzKlIuYZvyj7QyVI9OliSeQ4tQM/nIJ9epwpQ7qn4s0z9lPD6mXIjKzYNCCb2HNXeqhiHES6XZtZeRZGt+myaedM7TGyOfS6Zk2OQEcfbvKjdJWR+yXkShHSErXZCbvjmhEd0yFA7zE+/Na8cKShO1F7ON/pmW7ciZmVIy7Vuz5IrrrpuBFKHVj84PPWMQnoifEMgw/4PT4c9E7lEml3uApyq+dijhH3R3wQTYy5ng/7ykOiRN0SbRHb50jFK44xLXOQssf62sXQDiqNVN2f87u7kbBTQh1NYpMc7G4QrmD+N1zpdJXjQWQSmjg9SiLlFWPyZCs+znEyXxXBPz6glL+IByjbcYG9PvjNAXoQhXkYlCEROBYSd2afSOjeVGXz1F6vlxt753YWozGhEtNecatkRNVva6xCc+Wh7+v5UB2h9Ahn3XZ/UToVnYUDTkkHdzjMmd41iXvVDCq0fQ4NSmVHR1uE3PMjOgN6+0zbe6ktjnmlEwxvCwrFME1ZMao3HvM5GMoa97fkzla7g+8b6rGTNlIUg3pZrdnmrIt7MUP03SO+nq6Fx0KjqgZaXTieROyNvRml5nBkWU5K4dtGQRgP4TjUoM3odEVtPtuzCQXQOmYJpisTDyZ2sWdfu4fR2H0Lz1PADJEg3rodk8EImmlivpnUVA1LF7/Ihz4iZHO9x0ElGWgmP+tRbZMYaFehzFE7Ws1pJDKvuXF8aDC338SjG4l67+/vpwF38RqCoW13v3cSqld8ZIYOo97JahuEddB0k4CEJyLyxDzXT7tgQ8ukOuZjT2kXgeBhBfWuW0vKndmVPcxyznV32fn8Ibvku0Pvs9YuGvI9Lnc17WZIjDyasA9BP1TvZ9JznLiWBpK2781V30fsw6R4GxNoSdp5rK76TkGzZ3qWOYnXtRyk3TXjIMdlogt2Zx42q62xObN348VtYH7femrmrAH0TEFArBVr2MNHCjjOyuRrsYceQydLkgGsgwdXJZ0pikqH4qGaiGbWoEV4nM9OX7NX4r4njmTuUfteV+0HzdURdBL1kDCniPCSh1vnonrFq5PAMJhR6TySNuHo3GRmHNmQh4xt+RAaSve1SCPmXuddVXfbJinUFjU0ERvLpL+Nui8z15TzLMeDb2e77ZLDPuLHq51NwuN+xWKoTgRPYcuLpdf9jqK7OC8StKwLg65uxW5f8aAHtkOP5S5GrYXDMTvdtUdKwRdhcNS7jHWZfRsJ+o4NMMFiKDvzZ+nu8n5RljvhQIWyKobMac2PI8yEHDoG3SE5G2YHwnEdemmBuDJXIjOTgN4Wgm23V9ld4llxeOH47c2rNn6xrtWOtB1d7tKgjJcfLejTOExbLY8zR0alQzVtMbPwSzs6hiHtlzNIM2cbIpYsj/O0medG8YXNxc3NJj5tjqZacbNoQhl1YnFdPQ+tFMetESSpwii39LCzZDESopw/phvbwTTxeOYICjGFooI9UAvmGB23dYVlWjepp6NiIKizY+m1SRgbF7+N/nXfBLvweBtut6oWYARcOJzOLGpROxW17nYSB4cJRcM6Fepg4x1CHb5vrOaKhUNyoGE6ugQ1FO/HVDKafu85EM+eNpbKcmyqsuj88Paj0TCRxFYyjHEYoo+SdDdP+RWbFCznPJIwKG8OvQCxrvdpvD4GW2FBN2OoRlYYSa5l++1gKpdm4xAXbxcp7N3BT7vbPCKhKPmDfNQM+wg3DpheUCHPmj3NR+g9BWi4H/CQZ7e6dSkvEH+sGofGLqqFecTjbrieSOUXYkYO7bjHsi1nur3IG5GC7cgNFMncuhbALFCH+hkPJWdqLpc15kkITsCgdei0cqPxfHtRuLPjW0Ew7eituz/6FzFrt2hCn21VCY6HE+242RHz8wsgpW1Zec3D8l6bB+HCeW3UbTdn0kBOzUBUZxSuTNhXq7t5yBPKGu48ot5yS3Ng68oTPkvjjBmUlDATrCdvgv1tvbfvtnre6ojvwINDjsqtZOPHKO5R00SO7N6zwv42HQrdvJ+kqkbcYlPH0oCSdjvtyGILxkaZA4UrkFxM6aDIPOBbPoDpuDvs1Pst1Cptc5ZJd88jUSebu3jTnGTQjmDdHX6EGjGYPb4x1bZHYzmbAx4/7to2Fc2cYAJnMqFZVljQ2m1gRSoH93DdPqZi7bEnaJLiySOK1OvHyqeKBKn0dT1CuOdu22O7CfscVoaH5PB2ESQkgW/Te38aSu7SV8S5GMOr0ex0rJrXBIKh6sycjMzMdXL05PIyTsdHM/QaejnqSqygs+XUEJqmbofdy2JE7MaRj4EkQoSgkDYuGCfGzkXyVGbUesP2Z0RlL318KyYwTfpYY603hezuLaTb9haYo4oOQa2u7QLBvZZ7fktI9nkc8O5OotucTIND2vmkwEvNFoU4EK2sj5cwCZswLlC35u4VMuWHcOJSMsrqMTZqdItusk5rfHKfMzACkO0mSwormv4tPV5OFURINzhEBOpYNv6YcpimMnTlaio/bFKIjrJ5vrDKAe6yx/aBuNH6bGybwhUpLui3V7jtK0We8gtsXiTu0kiEhftznPaiKzpu6O3ZOxzRiCeM26lGSPlMpvR0JK/SEQ6o9TrfEP7M5HMYeUfczLFzJhY1Q2gShxs7rlbmwCR1uClMYu3G/oZcx1eLtUbCYC8EWnteq0JlHzYI1B9d8mDI6zt1yOj5lOkzDvEItu1qOcXCvcocmta9BjfNukZ3ye5MDx1S2ykH8mzcoIeQsgjTbVBKTNFwvDQjeb0f4xJvbJwiITfpIf5OXPI5mdE5i7Va4+UbO23EEBHLKud8gWGrg6cgeNqHGCNU0lFNQ0NX1sxRP3iFlO6yicrUar8hNwfSlqGdcMs7Ld4GIJrizalT9GDPT4+a30K1tUUIhUsxOFwzU9vuUDULbUFFt+t5E0sBuz0UkaWfpnCSWVgeGp2F20yxj5LLhQeXrEOvq5XGEyabSuVztc3P4myuqw0zEefGPgajvHE2usQ6eyrkir0okOg1FS0fcrebtK7ukIZKJlxdMlmQBaV9RMzjNlnjHK9jX7VwT05vhZsiehlg6ZhnDmVX7tHfgZwkH62ubqtdUQQ7D3VVG6vywie2Xp4Ix1PgXXNPUW1vvBQbj7ILnN1zV9MXfHwzTDcuYyFCgW5zUFQn/RSwOI7fW6KyGlMNCqrhXGx3DiambtHt7WZKW2TdYqDLlnzFaxAYe7SSZe2tozLqD9jJ/UeKEiJzeZCQFRiWMuCGyD2iNTkWZqM/7qF4rltii250zZSxB4KutxVHhUqVtvXAYWHlqWvJg/IG9FFniME4jovYsnDy4aL3x0OImL0BzYc0KkqZPkrSxu5gm/S0DecTmxlDLipVtgIDBZsdGLmvpXBqhYCXru667ez1ROyuQa64vU0JwhnfkiKndjsiZ7MMw4VEU3ovfJAnbhMEdXaa4YjRCCF92NPhwKSlVqmQfVgjoNyaekLYR0/UGOrg3/wdjoacOgwZlUlQJ7pYyHQ9o6L2/YLWqahQTVscRiHAxorPGGpvnYo0UXdOYtB+G0bxugkUnUOVGauvgVvshGuIwRM0QXPVH9Z5WCLl45q6KIeaIcH2nMbkWFGp2wynAZtxu3649/J8IDtbQB924WxQuN7f6vNNXG+Lw+0Ej3dUnJ1ofdcPN3jLRbcDBddigR0bxiAD3hKpqr11nBsC1YkTh5vqaSOzpATGuQKLzHmiR3ediM4F1iNa6tkpA0Pihq4g4QASvNhzA4Hw5x20t8ejcvIuxIh5cWqkDrTWC3tLubpiHIt0vzk2NxKatn4ReAkVkBGAOOgqtpJf02KCkBfvdEYtOaB1M3Lli3ecYQ2iFEq06RFFDz2Sj7Rp3ClbnSgCBZMzYa+P2Bl0WmVtWEzXRqRhPizF3xMUnlNqeaVnfZt0xJThGlGhc2lK0SwWmgQd+co6YAeLugeYNBN7uwuLsw4KlUZSHWrGUw6BOnmbWPVSiI8bwbbYbd5UHoahzNkjjicxyFj2dAYt5J4uTfl+2VFwiofRka6Mgd3AfWa5/aaaqFFNs3AD78AIFwCImx/r0txiFQPtjhp+vjmFCnPxJbROuxQaq5YIIem0RSlkRnPT3yYofILr1tKu+KbrYTH3xMOojawbU0eHw6abNJP3PYMgU+Cbw5baNTnexLVZje5ZgWC6bbcZ8kgcxfPC3j3IBb52Jg0CI6jk33sMNMhEWAxyYFt4iea3w2MuIikew1Y8TuRc33pju7WTofWxk2vmMGzYp+pG6hDLqllD02thTZaSuLcunBocGuHEwrw7pAguclypjqPZ7i5RIOMcLNisVB1qGr8e9YkUVJLOzA26TQxsx4Q9EvTj43xLMWEDr7cUwPmKmtkQS9nRx3PCiTeKoNgXeV2CuJlLL3+cwv1wLKg1XyV1jDK9niPHHWRRHnlWYMgntRJMYqyNHQndtKrkcbNrhIty0YHjNCP8Toq2Ulch2gMxlLENQOedR6062f2Opuk/v314++1B2tu/8GLY8ozn/9njpNdToW9veDyfEQaO//nJ6/O/ItRfP7y1XgJEej026/Ihen/89HcPzT7+8wd/y/77632rb8+ZX8+ueydaXkZ+S0p/6Pr2/rWr8uc7HmCHO3TL24vd8oKrB44/Puh8MlsexT0fNX/tq6+vN8LelhcLl/c2Aj8BM9f7afT+DPHDm//+1tFXjNh8Ddp60fL9/QCgHPYJ+YS+/e3/ANfAXHFPLgAA -->
