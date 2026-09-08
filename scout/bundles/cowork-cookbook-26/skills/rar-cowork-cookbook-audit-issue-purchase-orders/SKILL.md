---
name: "rar-cowork-cookbook-audit-issue-purchase-orders"
description: "Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_issue_purchase_orders", "rar_sha256": "f680bb401d52d4f8a9049931a11557510634a5de7dd9899369155896e3c1e098", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_issue_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `audit_issue_purchase_orders_agent.py` and in the RCI capsule.

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

Issue purchase orders Completeness Audit — Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-issue-purchase-orders
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
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
      "description": "Excel workbook name, e.g. audit-issue-purchase-orders-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_issue_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 f680bb401d52d4f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_issue_purchase_orders_agent.py` first:

```bash
python3 audit_issue_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_issue_purchase_orders_agent.py   # or on stdin
python3 audit_issue_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue purchase orders Completeness Audit — Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-issue-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_issue_purchase_orders',
    "version": '3.0.3',
    "display_name": 'Issue purchase orders Completeness Audit',
    "description": 'Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-issue-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-issue-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d6cf1dc60d1b4fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-purchase-orders'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-issue-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-issue-purchase-orders-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit issue purchase orders records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to issue purchase orders. Output an Excel workbook 'audit-issue-purchase-orders-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no issue purchase orders data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads issue purchase orders records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits purchase order records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo', 'example_request': 'Audit issue purchase orders in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-issue-purchase-orders-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of issue purchase orders in Dynamics 365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditIssuePurchaseOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIssuePurchaseOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-issue-purchase-orders-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditIssuePurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916+bPaVtrmv8Lcr2qSfNhXC1qQu7pqhHZAArQBilOO9n1Bu8jkf58juNd2utOZ7qr5aXDZgHTOu7/P8x6L317sro3K+uXTi+bbxUKwsyyO/HphF96CKYeyTsFbmTrg78Iti7aOna4t6+blw4vnN24dV21cFmA73Xlx2yyqrnYju/EXZe0BMbXvgg/NIi4W7FTYeew2ixWBL/j/qTHy4sfMD+1s4Rdt3E4LQ5P5n8AO2/tYFtm0CMp6kcdNExchuHrr4tr3FkHsZ17zYdG0duYvPLv1wRcns4t08Z094Fpc2G4b9/7HN+m1H/i1X7jz+tm5qsxid1r0cZnZb1tqv+3qYlYHIsGNrp8t5gA4JXDWH+28yvzm5dPPv3x4icHnl0+/vbiZ3TTvzktN0/nHN/8Ps/tzlIBpIVhRTSDMBfhe+TVwLAeXPD9YvH37sfGz4MPiv/87Hew6bH769LlYvL0+v8x/1K5YtJG/aEu7aUEYXLuynTgDjr0u6Gywp+bN+mZhg9jUwInX585vkspq8ff53o9PJa+h3/74+aUEJjwC8PnlJ5A0oK/u5s+vs5Tqx59es3Lw6x9/+ian6ZzEd9tZGLD69cvb9zexYOG3pXGw+KIdOeZNF6iGuPKB8O/8m19P09/EvYXky3Pxj2X1YfHnkmd//g7sfebdAXL/XCyIAdj58pqUcfHjm4667P3CBtXw40//Sqwb+W6axU37b8n9+Sk4AtULovUWkp8+PNL3y2L55ttXmf9abQUK5j/xBCx/V/c1UP9K9iOz/yA6iwu/+ZrLPxX3ZxuWf1/8/C99+6sNHxbB5xfWz0Br1raT+Z8Wvz1K5OcfvG8Xf/jldyD6/ypGK0G3PSR8ye0iDvym/fLl5x+ax+Uffvn5h64CVezb+Zeuzv5M5p/F9aHnDxF8W/XjH/cC/UaRFuVQLL720OK3svof9e+vC9POYu/b9ebT4vtOnF/LxezEu9JnCL7rxgbY+l0cf3r5HaBOAbzp3MdtgB//9V8LOXbrsimDdqG5ZdcuQILbOPdn4/UoBrDbPFCj9kFcmxgE9m0dqP85w7PFZbD49X+5D6T/6L4hPWTPePYlngHtyzuif3kgevPr60KPZniPQwCx2UKlj8fPhR0CmJ3VVbXf+HUPIMqZWv8j6OSP84eZAH79C6lfHgJeq+nXBzjHT7RTGWlGuqbL/NfZp3PkF28euACi/dF3OyA7K11gSBBn/gPEmzLrAVLO/jdpnGULDzCHC0hresgGMfo0C/v1118du4k+F09oXi2e7NFAYMFXcxYfPwKPgiwOo/Zz4btRufjht99/WPzvxV/tegifdRwBPbxlAFi41Q7KAnRUl4NlMycCKLe9RwZ++/0trkBMAXgT5CsGVPfcDCoy9b33IGsi/RHFiYXjg+CCwOZVWbczacXt60IKFl/tBUrnWzMjRGXTAn6s/MIDFDgBqTZw52ski7JdNKDsmmD6sOga/6H1V6e2HybmoLXt9teFzBwB/5QZ+Gc287EIbC6LGIT/awk8rwMh9Q/NYvMu4nWhzDW4qOzarqLaftMR2M+8AN553w6E24vCHz4XM8n6c6geDfEMD1gEIuO+pfTjnHMwluSg+59DRvu+xp5ZUn+wZf25aN6K3a79x0gCTJkWYRd7MwX87a2kmqjsMu8RP2DpLOktC95bVh41+GD5fxhzGjAjzca2QDNI+GMaWHzuUBjBFv8/z0VzPGhBUDmB1jl2wSm6en3maR4V53w+p8tZz2z1oye/jS7v8PSO0p+LLAZFV09/e658ZPdtzRP5utlVlVYf8kFpgUjOch+VP1dyXc89Y38u3ukA+LR4YB9IPoAJ0EZz9b4rnO++WwqSE83fv40Gb0maowKqG2TQAZFZBL7vObabAqvmlLynGbSBP3fyEMVu9Aev5jSCagPyF8CIuRYAZbx+hejn3XfT/7DxOQHNWx7TYVfMlTMLAHbMGXvka4hbgGF2+5zMgZ+fHkKAG3nVzr47II3A0+dF/1EwTfwoj2dc/Qog9Mf5/enpfNUfK9AxIFigL6oORPfRSXMF5GC+ATaAogKNlccF4HsQlLcgPATa+QwLAHbfBtKnxMflN4f8R/vNRPW+cXZk3jNz/yIApoMr0/foof9ZmQB5+bziofcfK+2rtln2jKANQEGg8f3uc0h4ffL8c5BYvMv99E9Hnx//s9PRg7mNPxbAp0XUtlXzCYKebPtOtq8Av6Cnrc2TeD8+KPLjO2R8fGLMH0Q+vf20+M/M+oOIt7b4tEBe4Vd4vrV/K6u3F4gC83Fz/YjNdz8Xqv8NWIH6Mgd1NedsAkz/lQXflwAqDGsAYmDxkxWbmUwHwN8PGgAJ+Fx8X+dznwFni3Cuy6b8rv8f4wCo+We+vrIVuFW0QLc3j4yh/zqftGbzG//lU9Fl2YcXgKr+Xx/NZjLK5zpu5rMc6BgwfLWx//j2gIWxnT/+8Zx7eHyws9cF6wMIyprva+2NQmYK/a4lnv4Bv1yg4cMTnGfKA/7Nyud2shtQn6A0Zz/aqZoNf57i5rlv3vBliAuvHP7ZHhbcXNRz5B6l/cD/Bws95vHmbw/6AO2al7Nie8bTHEwDIHT8FVhI/qnGB/98eTLEn6icmeoPFDWT9hznDwv/NXx9qPxTuV/H238WegYzxizHKz/NdPvhDcHAOyCxD4uvp4sPi/fz3qzBLzpwlP55PtnMCX1smT+APeDt66av/1vh+C+//JldD5j7Mhfcs2z+0brvWQ801bzozde/6NiPKIwSH2H8I4q9jlkz/klIgO53Cp/d+Bafb1aWj8PYbCXwqn3+38FvL6Bu7Tmfb5X7Ns2D5QDAPjbzPAOBvgYKwfdnB4J7/8mc/7a1iWwwbIK9AbGGHQeDEQ9HPSxY2xSMUdQKsREEx0kcgYkVZuOeT3oetQY3CApcX1OEv3IRH6bWQN6zhb/M81o8m4NTZABTFBpgCAp7nh+gmOetiTXh4iQK25Rj4w5O2c63rSlogjcfnz7NAfx65Jhj8ebqby8OgYGVItZI9PPFQBTiQCjpTPvL8gKvx2z0sTS7bfVagvY3Gubx/nqPt3QzFLEjdfzuTidurI66xbtsnokyfYel4MYF1naJrwdZNXcGKWjOqrgqNO5Iua4U9wbqi01GFomHVZdzpvKYiZnVbetIsVEa54pKcx3RKuN2Rnwe512tWEKtD+XGkpCR0tg1J3Hvb41CQPTumrF7hySoqB/XxbrTs+XesLdnOeJue1+Zditi7R+RKdmkU55bVRNd9vWGcc6HBrv4YrVHTPfGhc0VNzk/3sI7Vc6kLL0FfJrKNayl3jbifC8rdibG39xpf1BqxbkYDGkakVGxQgzp2kG1uNJzXBUBQVF1JjPPqlHvJ1Nzg2E0pZyYsPymsifn2EPQchUUqzu1DAqsuIsUAS3X6YWkvF3Ep7uDpTJmZxA7NDSxOnNH5MbJlb8/7PhiyVuxu73UXNU77HaLGW4UL6mTfJGdazSiDG0aklizR28NBfIltaqRTtIrsr+Qw+3khOX1duZFYUyFeGnuay5wTyvlupHjyZXqO0Pc/SQjCCjmrq0DH7XlZOPmjpHlW8ycpuGo3GhbkCpzr55K64JJOTz4ldKMJ+JyvTmeOnVnqIko1XTKeEXTSkZ71ZEI1zyJVqDKV1Gnu8eda+NlmN7OHCJkFrOGRW06FVm0V1YCLjYxiO+WV82bLZ9WQ7/O9mh/YrpGPt+NI2/etkkbpomOm0eeairIN1o4PSKy6UWMxmemlV24Q03qh5vW7gmVCzj2NFVmcy10QaLYVQLr6diWF8betqpM3baQXWvh0G7MUDtyKVZBwjQYcE/re38vmfvhVvL02CZ0htSnHawkGp0t77bpgLowyJgCJeZdHXPFd94QNIbFQNzmsjaSrpSdtEMTdm2x7I3kbvJ+o/WQ2N95e4j9nWiLqZIP2F5hEli8j6QjWOjWy2pwkLMm7sgK8BoaBhQfrmp/3lZ7eki0XNN5pMm3lQTf1NJLSr1YW0aK7ZFwm2EkC03iUlREArZQlZIwUSewW1AhqxD3d9455pf8lj3ScJsKVqrd0LLmzSqc8c1NOaYzQ4PhT04iAbiDLsNeXW/qPXdjxLum5O2wReHxYkkGYQN5ztWVV7tw21ZCftZS+HIzsqzETvW1NJGDG1EhwQzHbMVJEShxi86hDdxJFuWzx4jX98dqfT8wF6fR3ZGM+Jhv18c+4W65HnsCO4i1dNkQjDT4UWF3mbZRoKGcILmkEnTnbVeSc1DKo37qEYhH3KrLIdzQoza/y/nFIe2T0+KVN1W6SIL2KIzTRUfDK6HdQ5qNvbjbxYN5DfHTZuBy/Obn1kYqCE3t1dCWh363l5Msi0hu5xoI7xqnqO+Wu9spEZAc3+AbspSq9WEfuNEmhqaybEnbHaulg2ZwpZVhvzsfBf9qhOO4WeIUci0OGVspPnK7RK1QRywCjwweWji5wnm1mKY0SY+JbWHesoVix0Kn4Chu8FoO445P8VNQCi1+xukzmELWk7zrCnK3Go5G29DIzZWiGm+pmN/shqFw9+oQd6es4GObIW4HKS1H43K9+JkToCcrXBVJATu45yT0GvL4SrNJD9gnO7DtFSPcsdChM++iVVSCmZoMjVEcfrimW5yit9R5h0fwFiZXdzKDOvqUh9lKSpiCS50Bj60do6j8MJCrNDjQRze7U9phyg2eteByFDgEHEYpa7WtT1gzaNZBX5/3xXA6c9qBysrzFmN32rDBOJ07sbk0Kl2zjpWbc6kpktw0WwvfyamxldXJ3DgQu69Okc3srLry2M0uAenNasNSQ3GkXfWkxIcVZ5gZd1K5vI2QYr1j4ClSrdDkTtLFq+/HnUpcXCQmE38IeT1RT2uSifDIPNej3VxKFGvrbUT6GlwFhK5aUquHCV8c7yPiFzg7BgXPw7vsHFy3672EI1wm3C7rfHexrJJiEiiNMLnRFYqEzgBUVvqlKTfIZtoxvqoshWntqcsDmhBHMSaIM+zlRuFfjBCv0kAjr+GGZaUsGbzVfjJi82qo3TGTQ6KulOFgQc2oYIJt9408bIwW8pNtSyniCp6CgJMTJTO3k3YLRV2X8J41csknDyzCF1tcK1gnKu7bjSGoJ2JLTxGW7uH7zjF6LVDW1slt08BNd71xqWQTSc+EljXWrjLdE8LCTECtkraorW210XCWFXwFEo5B5nXuatep5bkK7ugZrzKvVUtcYOX7mZOIZVwdOK/gSHYnXBz2mPbMTkCPS0ZZexXq3x3NJycvjatVGHvjpgldQ9tMQSfclwemrzpJmtQY67oLzmK2izDjTt+nx01NQ+vbTqmP+0J0OxIRFPqomnSnNB4PeaZRhWq60da61HlsqlzPrDCslpUhISdS5zdr/zqtiC1zkErJMjjv3CAy2+j93byd6T5Roiti6sr1cOpLoZMvCTIwDVaZkrU9CzbcHPEKjva+OdKxShrG9p7r0cgdPO4inaQrHZZVfoNNn1QOaQPKgKuaK5ONkrAPj+eOyOCSuRDpmWdL67pyjuoxZNYCVCS1yu2zwbGUaa8tBWNHJUJVttra1pMsYKVUcLs1H9I76V7k/Q44PAn3iBu3zXoH12MYYVQ1uewmaBmxiD3VPMdBk+yyMY+JVaYCzIq09Kp2Q34/9BFnxzlDH4wsPa4kfr808MmLw6XKKcnFT2wjELq9zmxPG0oIoMrqJNrHEiU/y+N0Fi6GEkuFw7Prm0cSxGSzHXU4c5sNamFXx2njZcBUpSTh/GT5KKVcCL+GL4Sd8MqJiUm/qCjfz21MWa13W70XWFvta4yXD52G0iViWzjX+oKgaXKH06l40zkmOIaVNGpje2bW8ZTuBjWNvapO8o3VrY8o3d32V1tLTxZ+2pm6dxyMxqa3mb10bP12NpdbKZV3dWxt3CXqD2uZ1jQ+N1w2jE3CiY9nTSa2I9QRrcxx7Hnyi+ScrAX8SBkWynB3tFbQgBRXF4slNzR80s6ZSSuga0Q/vLfDWUG72E5vS2G5C3oouh+45QBbXYrC28GqC3EKW5TSPNOms2at8gyBJ3RepquJnuJkT1pX262Ke7305bJAuwuDMFq4b2zPY2JarWo35KTrqhYZEuKbMt0ghZQYcLqtj7rX4oOrhfoFH6xBiZo+pGHTDrkUDOCriq7kgRVOBQ3LnpEzWW+fuYJ3zWF3s9fwdL3gVShuWH0reinoJUdQDbmjt66b7ahAHUMmcBtjL5yxaThjhyWFpHlRCvsVRay7ZITuW2Vf8a2cH2KL99suyqO8ONYqE0G4rqgSbJwdeGOXx4hJ8ZbfnyuDwykMqcTmuEM3dyVYjrAKUUwWHQo3ZqxuQg/xzVTj+667TYAYcv5yHPXUNDUJjMTrybB9cbutm43Po3rssqyD7C4cUxB2TkambGpRe9ebFbrxkp72olYOr1Crk8cMURycF9MSjzfnrXDXN5pCXMw9gXmYP+5j+UhJdSXdJvQSJle9LsUorqBkTUSAFUd5r27lsIOJiDuzy0Dw9x1zru/FpYux/qaaxiE93xoEb1LTg3v+0lPFtYRjMkeE7oxpNGYK16EsGYNyZffadfA9tftrjabgEBhxVpQ3OXN1peSaqdjK7xPydKe39bUdqACl7ydbP24kzA8wyWPL+/6GHTrEuF0kwkg2/lYZYBFhpNiHPZNvlfY0KamCbzPapbXtmEWCAXjD3pP+eneqxL6IEYU1SuWcYBktsmweC9v0zgn1OEC73a1hImXf+VMLOv2C3X0BrozchTpmhcdxtV9b42lzDZve4o0th9Tb655rvCprIF00W3OMmlUOTeblJtdMtdqKccgcjoJ2jBB0QrRIW4VujPrcxZAobbxuKVIDDIH7A7djl9c9hOXLnD41o1Z1IQ8jiLsmcJRIupSsutX6WBxuCQWYYd9I6Q0HcFbJTmIx6mCirKPKdUK45OEmDcfyePSoUFkRV4u/pM6yKmEGoxjfEMOdqY4pRwdcdptU/A7OBZViJGvNOxnpNg+tWjYdVj54dwNFjjG/V/vmzpIhq9QZU4UZyuPDJjxwdSxdPZOsCD1gl4nJ9wQ4kaGtKB7JXFh3xlnTt4q2OWSKWIGpbeQ2YDpdFsJwcOyjIq/PpmigUeI4rmuvIG13vd5tXuG8Tl+7NhvB8FW6XXh1pQUYqAXeqU85uowccosK3lhW3kk0xaS8lTdr6zeEkyv7SxVqSQVpuSdf9uw52kuqksYGQbAeBmBxS+lBRN4HG98mRLxns0pU1qMibkDCwSn5fi8E9XJe0wmD+tsuWp0nsSVWkJuzBOta9kVDlps63HN1PtySU3ZaehiSOuHm6p0yRjeuOtvSR+tyTCjShi5j1Boj2htb5yj2vkrkeeZwFUPGpJZP6AYePaXagEOABzrFEkBUrdSLfCkuMH9zSpYCilz5wcIwBDYK0gOl34h5B47gy4MPHZwN7HrxFV0VlwKM6KIFxYSnb/Se8JgCw08yZecKlQYnJzrztoFnaHWOin6Dwe0lvmHV1SmvpCS2WC/uR5nwLb1HcJuS6PuKI+DdMoF2AaOizHmrK4yAyGDEKaZ9qRtqsOKW/M5HDtvKu+Qu1TCBdu9MNwvkrQIjJASqZydqx6RsN1aIjI0tLylUzJBoKSRNO+w41yPQFluLbbIiwXhI8Q4V19bOvSvqGrpCmHNVWYGkWhi63NToWq9O8R5n8Iuddrjr61Zjh/ZRvi4pWYTRPtV3XXIi7uqtOy83SzrOktM4imtFlNg05yF/3RgQceeCBKlVzD47YNhWG2y3wQ/LcO3IF1yx6A0v1KilZ70sB3gchXfnnvi+SNHJxaqFGtQba0PSIG9SnlWhVeF5FqDv9alyCkw8LjeVB6OCI5/WWyFf76oNuFzsfQuCnUt/pQ72emkP9T6qUXKbl55z6g9mCelxj1iBmbSduC8O2JgwtJUyW3x9pEmHmsxCLQJuI/Nl7Zz9UjMN3pct+eyf/d62i3y5R073+w0QW9TAba4Ibe8lZp9SWS9KAwcp5DZd8eT6ksEt6OK+ibfnVOPOwiiOw/VYOYe8k2/pbnOS19cqCoKlvzsbu10m4OBIurMPsLw6ATpUQpdLT1WLrZRw8BrpAtAlZXOkOK5Y1DpOGYU7Q65dEJKBzBL2jkUfL507flpnaYhZtySk7m2iHty1eJMQC/VOA5l7q/gKYsYvz2si41rzoo3FiFDEHZZvt6ggc/gewAqa5VLvwHKJO/v4KviFgsNoUu8gmzyIglSqeHsVrv2Ju6/uweVkNnlLIPgwOVOJhfeuA6PnxtusBdLlTOsSnigxqtCttqRgoPuS4Nu8dS1UhbdgcSsLS+SgHsptYhw0pWlI2B8ObtvOk75x2DupK+qW3OuEdV1a3bDh+JPiDRWMeOGwl0QIDtZk7PEnXbiuReqe7Ppb5FeWSNhCc2rWUkvKoicVG2K17c89KNkb4SL1KHmF73dReTsEVlIAE8hCbGF28nK8v/ir8727ZXJ71xCkr5AqieJAzqqeINFlxehdT4w1CXN7oibV6kzeSCjy/Gy4wshETFOf0gUuyqfLOdz5VluDiXJw5d60EfHO3zrlijVXMCHtxaIRHa3jHK8LojXH+fh5XAZFd/Logt9OsTAVsW4KlE0KnquEmWDpa7RZIhtu7S9Fhpho3TUnbY/xqiWip6BacgzWHY0Df+2HTaVsVJxYMyxrTpUgY3LiE+YN3R0iTyHXnLqhdoHl8GO6ZO4uIN3UQxuZvHsbt2dUwSStLovlnqpqVOqXS7ItrYa+Bysmd8KCM3cFvd+RGx0yan/aNkFfTdI0mXejhIIEFYdNTsGOY3bWZWMb4g5Fag8plrED6mGrUjasYTbVODuP9JUzXE9jsT9PbYvice0FhHa+nWFWsYkIPR9IuU1ktFHsqpZ9ZVrJLIMhaABmerlfclie+w1lN63mmq1LhrhnqCFiidIJSuzBGXuMDz3aIajr/lAcOZhW9idqO1y6aNgdYja+I+CA53Qtq50uoUCO4yQ0wfbuRolJ2ktET2uScvSjKeYJjY033V0OpEf4bkz5y+EgQEtNLo5KGcqxvD7ZJ7Hs3TVdJPRg3wNoxlkYSu8F3ev95aLi5GgZewAUm1XvODFpHgya6EGV+QTR77f6BiNaovOxEVG47O6IKj3qZFwSdoppdoGOxXkfRZYc2mv/curam9zfVcdZHQsVFM5V2bU+xU5o4Sli7GB7I4tpSqGv+jYpl717FvMQtKvFUfebS4/ESZbClpqOJ0a9kjgt5aVPjYNBRyimFN1Sd7xaOa9kW17XeCA5xytbrZOzLzQEgMmTA58IJkHPu9IftYDP9P7sixfT08UYNHpDoW2BrEzUGc8eBi3PYQBRUDEVy4kPNzUlDEp3GcnyEmzClThKw17TVWpl72tkd9PjW045sdL00A1jOyjW9INSUhG+RBqDuOe1wayGFYrXndlhSO0SHDySowbJLlwzsN/AbOORkBOiIprt2ab3vT2/zjqct0kIccERPUk2LJZ6zKmkRaMu1lYV3nJ6x95N1WICi/Vgv2fD8oZZJHIbUklMuk0woae7vbmdlB1bYT4vLWlm56BOflkxvNtyft/fRScpwEEpW0HXBC6pDRus2GPnAQiyVfywS91StO+j37vTYXudxHEf4albIZwpH4aD7eYhtiKoWqwsCLqvYhhj3dCRMejq9hR3dhJFDhuuTiDUdUVnmOSj5fm76OILV9fT79gGR03dJZanE02/fHj59qDs5d/5Udf8AOf/2XOk5yOf9x9pPB7++bb36aHr079lzS8fXmo3BrY8n5A1WRe+PVT6h+djH//i4d68cXr+Our9UfHzuXNrh/OvhF/iwuuatp6+NGX2+GEG2OF0zfzrwmb+AaoL3r9/ZvnQ9e1RV1t+qew5cnEx/9LC92K79d++hm8PCT+8eG8/HvqyIvAvfl3Nvr092AcurV7h19XL7/8HGYb9bOUtAAA= -->
