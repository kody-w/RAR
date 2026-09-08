---
name: "rar-cowork-cookbook-vendor-invoice-three-way-match-status"
description: "Read-only report of open vendor invoices posted in the last 30 days whose three-way match is partial or none; returns an Excel workbook grouped by vendor plus an unsent draft email to AP."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_three_way_match_status", "rar_sha256": "2ad732c67447fae36416cbe09fa6073b8499852701ef92951e1258799e4846e6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_invoice_three_way_match_status`. The original RAPP
agent is preserved byte-for-byte in `vendor_invoice_three_way_match_status_agent.py` and in the RCI capsule.

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

Vendor Invoice Three-Way Match Status Report — Read-only report of open vendor invoices posted in the last 30 days whose three-way match is partial or none; returns an Excel workbook grouped by vendor plus an unsent draft email to AP.

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status
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
    "date_range": {
      "description": "Posting date window for invoices to review; defaults to the last 30 days.",
      "type": "string"
    },
    "email_recipients": {
      "description": "AP team recipients for the draft summary email (draft only, not sent).",
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
    "output_folder": {
      "description": "OneDrive Cowork output folder where the workbook is saved.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_three_way_match_status_agent.py` and embedded as the fenced Python below (sha256 2ad732c67447fae3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_three_way_match_status_agent.py` first:

```bash
python3 vendor_invoice_three_way_match_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_three_way_match_status_agent.py   # or on stdin
python3 vendor_invoice_three_way_match_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Three-Way Match Status Report — Read-only report of open vendor invoices posted in the last 30 days whose three-way match is partial or none; returns an Excel workbook grouped by vendor plus an unsent draft email to AP.

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_three_way_match_status',
    "version": '3.0.3',
    "display_name": 'Vendor Invoice Three-Way Match Status Report',
    "description": 'Read-only report of open vendor invoices posted in the last 30 days whose three-way match is partial or none; returns an Excel workbook grouped by vendor plus an unsent draft email to AP.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'vendor-invoice-three-way-match-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c90c6c5b01666328',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/vendor-invoice-three-way-match-status', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'vendor-invoice-query', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Access to Dynamics 365 F&SCM with the Accounts payable role', 'Prerequisite: Cowork D365 ERP plugin installed and signed in', 'Output matches: - An Excel file `AP-3way-match-status-<YYYY-MM-DD>.xlsx` with:\n  - A **Summary** sheet (counts by mismatch reason, totals by vendor)\n  - One sheet per vendor with mismatch rows highlighted\n- A draft email to the AP team referencing the workbook.'], 'confidence': 1.0, 'deliverable': '- An Excel file `AP-3way-match-status-<YYYY-MM-DD>.xlsx` with:\n  - A **Summary** sheet (counts by mismatch reason, totals by vendor)\n  - One sheet per vendor with mismatch rows highlighted\n- A draft email to the AP team referencing the workbook.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_range': 'Posting date window for invoices to review; defaults to the last 30 days.', 'email_recipients': 'AP team recipients for the draft summary email (draft only, not sent).', 'output_folder': 'OneDrive Cowork output folder where the workbook is saved.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': '', 'expected_output': '- An Excel file `AP-3way-match-status-<YYYY-MM-DD>.xlsx` with:\n  - A **Summary** sheet (counts by mismatch reason, totals by vendor)\n  - One sheet per vendor with mismatch rows highlighted\n- A draft email to the AP team referencing the workbook.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Access to Dynamics 365 F&SCM with the Accounts payable role', 'Cowork D365 ERP plugin installed and signed in'], 'prompt': 'Using the Dynamics 365 ERP plugin, pull all open vendor invoices posted in the last 30 days that\nare NOT fully matched against a purchase order and goods receipt (i.e., where the three-way match\nstate is "partial" or "none"). For each, list:\n\n- Vendor name and vendor account number\n- Invoice number, invoice date, posting date\n- Invoice total amount and currency\n- Linked PO number (if any) and PO header total\n- Linked goods-receipt status (received qty vs invoiced qty)\n- Reason the three-way match is incomplete (missing PO, missing receipt, qty mismatch, price mismatch)\n\nGroup the results by vendor. Use the Excel skill to produce a workbook named\n`AP-3way-match-status-<YYYY-MM-DD>.xlsx` with one sheet per vendor and a summary sheet.\nApply conditional formatting that highlights mismatches in red. Save the file to my\nOneDrive Cowork output folder.\n\nThen draft an email (do not send) to the AP team summarizing how many invoices are in each\nmismatch reason, with the workbook attached.\n\nDo not modify any data in Dynamics 365. This is a read-only validation report.', 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork engaged the D365 ERP plugin and queried `VendorInvoiceHeader` / `VendInvoiceInfoTable` - USMF has **zero** vendor-invoice header records. The agent ran a cross-tenant scan and reported real data in USSI (35 headers, 8 lines, latest 2016-11-26), USRT (2 headers, 0 lines, 2016-11-23), and several smaller entities (BRMF/FRSI/INMF/JPMF/MXMF/THMF) - but every record across all tenants shows `MatchStatus = NotPerformed`. Cowork also identified that `VendInvoiceJour` (the posted vendor-invoice journal where match status is computed) is NOT exposed as a queryable OData entity in this build. Rather than fabricate, Cowork stopped and offered three actionable next directions: (1) check a different legal entity, (2) pull the same view via the F&O UI route (Invoice matching details form), or (3) rebuild the report around received-not-invoiced quantities. This is a textbook example of honest agent behavior - read the screenshot for the agent's cross-tenant evidence table.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': '1. Queries the Dynamics 365 F&SCM accounts payable subledger for the last 30 days of vendor invoices.\n2. For each invoice, resolves the linked PO header and the goods receipt status.\n3. Computes the three-way match state and the reason for any mismatch.\n4. Builds an Excel workbook grouped by vendor with conditional formatting.\n5. Drafts an email to the AP team summarizing the findings.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only report of open vendor invoices posted in the last 30 days whose three-way match is partial or none; returns an Excel workbook grouped by vendor plus an unsent draft email to AP.', 'example_request': 'Run the three-way match status report for open vendor invoices from the last 30 days and draft the AP email.', 'inputs': [{'description': 'Posting date window for invoices to review; defaults to the last 30 days.', 'name': 'date_range'}, {'description': 'OneDrive Cowork output folder where the workbook is saved.', 'name': 'output_folder'}, {'description': 'AP team recipients for the draft summary email (draft only, not sent).', 'name': 'email_recipients'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when AP needs to review vendor invoices not fully matched to POs and goods receipts over a recent period, without changing Dynamics 365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class VendorInvoiceThreeWayMatchStatus(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceThreeWayMatchStatus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_range': {'description': 'Posting date window for invoices to review; defaults to the last 30 days.', 'type': 'string'}, 'email_recipients': {'description': 'AP team recipients for the draft summary email (draft only, not sent).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_folder': {'description': 'OneDrive Cowork output folder where the workbook is saved.', 'type': 'string'}},
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
    print(VendorInvoiceThreeWayMatchStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
