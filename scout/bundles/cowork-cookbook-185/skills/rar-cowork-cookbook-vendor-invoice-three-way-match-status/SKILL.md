---
name: "rar-cowork-cookbook-vendor-invoice-three-way-match-status"
description: "Read-only report of open vendor invoices posted in the last 30 days whose three-way match is partial or none; returns an Excel workbook grouped by vendor plus an unsent draft email to AP."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_three_way_match_status", "rar_sha256": "2ad732c67447fae36416cbe09fa6073b8499852701ef92951e1258799e4846e6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V7abfaSLblX6Hv+5CZD9tCM3KtWquFACGhCSQ0kK7l1DzPEhqy6793CK6dmVVZr1/16i+NfQ2SIk6cce8Tl/Cvb3bfRWXz9vlN9e1ixdpZFkd+s7ILb8WUQ9mk4K1MHfCzcsuia2Kn78qmffvw5vmt28RVF5cFmH71be9jWWTTqvGrsulWZbAqK79YPfzCK5tVXDzK2PXbVVW2ne+B61UX+avMbrsVull59tSuhqhsfXC78f2Pgz2tcrtzo1UM5thNF9vZCsgpysL/C1ij65uiBWquDqPrZ6tF06eSYVP2FZDvTN9WrrL+ObAvWr/oVl5jB93Kz+04W3XlilY+AVv80c6rzG/fPv/8tw9vMfj89vnXNxdoB2696U9B3MsCbVHPsCdxUU7t7K5fnJHZRQhGVhPwZgGuK78JyiYHtzw/WL1f/dj6WfBh9Z//mQ52E7Y/ff5SrN5fX96WP9f+5ZWutJ9Ocu3KduIs7qZPKzobFh99t3zVgmAU4afXzN8kldXqr8uzH1+LfAr97scvbyAUjb2E6svbT4sbv7w1/fL50yKl+vGnT1k5+M2PP/0mp+2dxHe7RRjQ+tPX9+t3sWDgb0PjYPVVVQ7M+1qN78aVD4T/zr7l9VL9Xdy7S76+Bv9YVh9Wfy55seevQN9XujlA7p+LBT4AM98+JWVc/Pi+RlOCHLAL1//xp38l1o18N83itvtvyf35JTgCyQ689e6Snz48w/e31frdtu8y//WyFUiYf8cSMPzbct8d9a9kPyP7D6KzuAC19y2Wfyruzyas/7r6+V/a9l9N+LAKvrzt/Sx+gLxzMv/z6tdnivz8g/fbzR/+9ncg+v8oRi37xn1K+JrbRRz4bff1688/tM/bP/zt5x/6CmSxb+df+yb7M5l/5tfnOn/w4PuoH/84F6x/K9KiHIrV9xpa/VpW/6P5+6eVbmex99v99vPq95W4vNarxYhvi75c8LtqbIGuv/PjT29/B+hTAGt69/kY4Md//MdKjN2mbEsAW6pb9t0KBLiLc39RXosAPIK/C2o0PvBrGwPHvo8D+b9EeNEYoPEv/9N9AvpH9x3QoRdAfn2H5q9P4P0KUObrE3i/tk9w++XTSgPCyyYO4wJg8JVWlC+FHS5YukBz47d+83gibud/BDX9cfmw4Psv/y35X5+iPlXTL0/SeeeFK8Mt6Nf2mf9psdOIAJW8rHIBlvuj7/Zglax0gUpBDKD7A7C/LbPHQiBArzaNs2zlxQBfAF9NT9nAb58XYb/88otjt9GX4gXX6OpFZC0EBnxXZ/XxI7AtyOIw6r4UvhuVqx9+/fsPq/+1+q9mPYUvayiAOt6jAjTkVVlagSrrczAMBAyEGEDIMyq//v3dw0BMAZgXxDAOYv81GWRp6nvf3K2e6I8ITqwcH7gZuDhfiBZwwCruPq24YPVd33cOXlgCUCrgPB8wsecX7gSk2sCc754sym7VglRsg+nDqn+yr7/6xWnsp4o5KHe7+2UlMgrgpPJJmM07R4HJZRED939Phtd9IKT5oV3tvon4tJKWvFw43K6ixn5fI7BfcQFc9G06EG6vCn/4UiwE7C+uehbJyz1gEPCM+x7Sj0vMQUeSA0Tw2m9rP8fYC3NqTwZtvgDOfxWA3SyhcAEhgEXDPvYWWvjLe0q1Udln3tN/QNNF0nsUvPeoPHPw1Qas3vuA1bMR+Ag6gdWzFVi9eoHV9dX+fOmRDYyt/j9uixaTaZa9HlhaO+xXB0m7Wq9QLI3gMufVO4LuZAXy8VV2v3Us31DpGzh/KbIY5FUz/eU18hnA9zEvwOsboOCVvj7lg+wBoVjkPpN7SdamWcrC/lJ8Y4EPIF+ekAfiC5AAVMqi+rcFl6ffNI1AuS/Xv3UEz2RovAUXQAKvqt7JQHIFvu85tps+vQ0K9D2Ki3eXyA1RDDz/e6tWQDpIKCB/BZSIQckBpvj0HZlfT7+p/oeJr8ZnmfJsCntQn81TANDDXxRcEGuIOwBTdvfqu4Gdn59CgBl51S22O6BCgKWvm37j133cxt2Chi+/+hWA44/L+8vS5a4/VqAogLNA6lc98O6zWBYcyUFbA3QAeAFqJ48LQPPAKe9OeAq086XyAbK+p9pL4vP2u0H+s8IWfvo2cTFkmbNQ/ioAqoM70+8BQvuzNAHy8mXEc91/zLTvqy2yF5BsAdCBFb89ffUGn170/uofVt/kfv6njc2P/97e50nYtz8mwOdV1HVV+xmCXiT7jWM/AYiCXrq273z78b3mP36v6I/Piv744sM/CH/Z/Xn17yn4BxHvBfJ5BX/afNosj4T3BHt/AX8wH3fWR2x5+qW4+r+hKFi+BLotKA8QDGDHN8r7NgTwXtj44TL4RYHtwpwDIOsn5oNQfCl+n/FLxQFKKcIlQ9vyd0jw5H6Q/a/Ifacm8KjowNre0jOG/rJXe9ZH6799Lvos+/BWgNz77+3RFgbKl8xul80dqCHQhXWx/7x6AsXYLR//uK+Vnx/s7NNq7wNQytrfZ987byy8+bsiedkJ7HPBCh8AhoN6XDAa2LksvhSY3YKMBcm62NNN1WLAazu3NIDLhK/N4qR/VkcpX5W6jAHoAGweXiD5jUcWhvYfsT/8BVRxYPdZ97z3j6Typws/0f+1I4uXWP7z8jToA76D13PM95J7EUjbA0YG9fAikh9fNxf++7B6xhNM+elP1/7eEv/zogboQRYbvPLzQscf3uEPvINtzIfV9x0JcPX7HvG5pS96sP3+edkNLbF/Tlk+gDng7fuk77/IcPy3v/2ZXk+M/BqUGcDnP0mPwt83IDe/1eNr+Oo1fCmE5tXufCfipTW1Qbv8J04Aqz0BHNDgovhvHvlNr/K5ZVv0AnZ0r98w/PoGktoGCWG/p/V7zw+GA7z72C4dDgSKHywIrl9lCp793+0G3oW0kQ0aUSAFsT0SRVyCxDAysH2UwGDCdfwNFdjEhkSdLUZRWxwhN7AfUAiFwz6M4FuSonxsixE+AeS9Kv7r0svFi2I4RQYbikICDEY2HkhiBPO8LbElXJxENjbl2LiDU7bz29QU1MG7tS/rFld+35gsXnk3+tc3h8DAyBPWcvTrxUBr3SVQwbk2wnomfCuEZZgXNikuPtjO8nxnYyDkeUKwLDqllaylWbph6JG/MgyNsed7DQu60l7WmEbya6cid+GVvvH8XN+q+oZlEp2IlGKiVJ+71ogeCXRdYuqeh08nSrxk62YLGzkVhKRDKL7PGdAt9486ruJyp1dpZNYoBG2PM04MWsyXGHrGWXa6HfLagvTrmdOZs+6BcS4xnDy9EdTzQxgv2kjUg/RIibzW8V2t2PamaQQz726CuHW4mGK4o1wcVALxrHKKZ/kIsvWIU9vCSJtKaN0KSzOkvvPG7bx+yJKp5ZIa4dbY5DIz6ila8xe/R46pWqqemcRUUZ9MFIbXfd0MkGRe140urf0CJR9We7yvD5G7GaZe0O/n43izussZt0L1FKgkjLPSYQ7OspSxmX+XKoci+KEoijtepaLJqdcuFYdS0XYSGZKKNmbbDLMIbOaj0miSsL3MDXe5PXjCnrbycS4f17bZaw231VhO5wMsu5dS148T1ZlT/ziNR5QS28GzKfbUCB1PpbRpBZTCbIuDHzXj3d6hivJArjt/ODYJcT2zTWdH9x0WaNtzJojSRr+HHDMPMHwT0zuqkb3q4U467tX+VNsWL2e1yCkjfZ8HT2CjeK9NVU3uLMqZ4knkccNg9gfC2kGdV13uve9vDE5wq33hp8E00wqDI0qyH2G5wh/j44I6+MEn0nVFtQWdNjynDgmscCwfBQcVji4XZWoukUsa1nWOW3dN3hHBZ6MGLdvE1muKAKQXD96OBf6WUiyC2B6SSv9wNERbS8z6erH10GY2OSxY582x0egjMTl6oKvphWB6RTDPG7VhnQBP8/v6Wk/6uhaVqRI8m/f5/rJbM+1VGkGLcE+2+pp+mIfTcBUOVCRO7O5OpesrvUHnG6xkbFOmyTy57G4eJUrcQnAKGTuRL4OY66XElJUz5XrtumPE8ZITzTWbRwX2/Vk/X6MgP0cnMlVQzsO3zmU+Q7R0f+wmaH0itzw5t4VfZ1Hp4ffdzpLDo8OpWXeBDhFFioMQcHsZ0XLh7t/Njg8DkDJuEngDYw5s2atMUcHbyTltAWo/mCs587L9oCRkkq5Hy2FU+YCdM1/STXZfcbSK81et4qQ9ck+UhnDku18TvU9eeB7yzHZ3LcpqFlVKHFtUpk9am/hXaC8qLAIRt/KOTLA1XyZxrO/t7Z5vxFiUNE5Lgot0VCWBe1wOm2KMi8GLitS2LDjAC3a8bDw6NjcK5OFDQHLkwcvTuUB8yivISDAV8dHHJ1ffM0lizwqXYuRDP9XJ9uFO6l7htxF0OMiyhmjqIQ7EWHLgq5/kkckLyg2hGEY838mK47QI6SkBEeSIRaZw9PbKfbP2g+SkGV4dsMV9mxy3OWJZiM53Wht0CaGzTD4aEZ6ie0PkjzWtkEUrjdVDvicJpHa1rWP1yaAZgi8Oe6VQIT6iodyMSALLfJkNmoCor2fdJglLESyBTqJbezutd/z2vGlnUfAdU95RMxWimJGzyK7eyHvzts0JZH/ZWZY2sQYQx9Fox7QAT27WrnIsup86F0M3rTXTDzRO7Abj9kVFFdUV79Ax9yJFBdgqcFCPYQRsdeU6tQxQRXtnyA6dWxhBIW7ryI3bpj/cMfLsTdSW9bNQxGC7Y08WmlGHs3wwz9d0QIvTGk/hKUM8TkS0NM35QGttS0/Qgy4pvEvZGH0h/SBTH0HkW9cDPAHM5ZOTy8xzeKC5qg7valQJRIrREimiY692w1zTIake8tjcE717mMr5vuXcWBXxjWHW2WXeEhPfuiEUsWFpjmxTq9Ompvl4f5mImdjrrrer2NsxYlkJtbfqlIbHob7rodyGyjG5XuQTlbdn0xAQtyX4eSf0WWzeTsLYs+6eUdJHuuPu9b7BqODxaHKSNyTdC4tL2ynlptwwPaWBdGpOl9KLogiLTC8cyRbC6YiU5htpHyzd6/aQ74cQ5awtBZ03lFxoPAZBjjyftdO5JsRhVka9vVyiOmVgXCEjnLwZeNXRthDZkblxjlUC3RNXvoHeiCy4Q5Ociu1WOWlbV3yM5TrYcBHM+B5Nn28eLIYxp8L7U44n1BiP/mYaDZRjKsu7ZykTBbeyOMQP9qqd82TPdInNiu3cHpiyixRWUShcVNu74R+sJqsNfifirRtzXUcmh0e8gc9OdhU0XFcqmBjLLJB2/vbObegimpNpmplzLEPNI6QkXm7X9zHQR4wsHjtUJjRtfbT1CnE4HWl1GIVEfO1v2GFHCRclWZPqeZ17hOgIwiyrkr05akqouUg4ns472KppSTB9Pcj0U0L7JaMShWHhrmlFcM6ZMzfzinu9cA/JCkT1YmnXPaaCZidLW5wBjOGX6i4wkLsbIWrI4bpPczQB7brdbcR24t2fHvv9xrpb3CHFQHbK0f12uUdliLVGkl3uJEPT+ZEmElyrBj6/XkcFO1TWcNzH7kGm/WOPzs3tFCQDXGF73kgksiqb4w7aDoIq2lzvP7RT3eGiXhIHmLuMMi3UcYhlusULu2mzfsCXk8a4hHk5FDv/Ml5qcy+XwYFV9n3Ga1uJPQhowB8Od8JYq1iit4oZ63c7XOc8V1pJF91KQ7ww0G1Ph8SO4QJVyc6s2adwGlb4+bEn9YSIMBuTaGEoAtIOjLSwyj0VHxB+60XDI99UiaQiNn0UoYCbGM1J6kE0toeJvZN8p4+b+rCl96kgH4kK1v27nu6aBy9Y484278i2b7JIVRYen89SOgkxs+4vzmQCuqLnK6hWNb+DloSr8hyQcdWBwPdxspUEeXNvkJJTTju2MgtJNJATlaToFZ8vmn5Fty2NsrMluqlutlWpxYKrquhO69RIg1hlq/TXrbFFms6D5NMDvyZcszV3JV3TE63vMvE0xch0zR+ywZ2FgVD0g6rsNH19i0K5olt2whMvm2wIvk/yzUWLG3Qzdqh9ARlDWME+hVjNewwO6JNJaC+tt8h96ylXk4LlWwA1dHMg/REry5p2lbltYPZhrsPBv9SUfWSjZG2pZiPy3qQqgyHuw50H5cgcpefc8UepkjRfoKtQD2NjaHjdxg3M5HRM21pY0Ft6DppcdYIOsMHp6iYUht265g/7mMkRkyPFeOcLqVzubhFBn2JdPukHaT6kJ+aBKMcLlHVHzenLh8iemN4IwkhvQUt0c7l1NmuusaEybJKwznNy9FLFnA66LKtxJmqC7wcaM+s9YzDDVTL2zvEBPwg1pdtkM3gHjtJsmvFM7UYnjHYjJHFaQ7OYSbmxtUWxL9cbtilUTbUI0GXv/NSLdU/TH/plUu9QlNQ14t7MBA6rbjrXOhmLSGpg5Xjfq8VlM/AO4NpC1zuR59cCWW7Y3eMM4FEv9I2RQTp9mBsMN6brtdzLhn6eFLGKE8oU9yN7o7N7fHfqWNrkWh/crjvEWVfijhXMsTyUbcTG2B7WdyZ2IpHyfi7Ge4iui20OGqmit86H3eQfDUvcybe6rww5hMT1CN1rJnCijY4KpEBalm0jUFXSYRvemXIMQAKp1LnyqeSSFcFjD5sxztk5z7s1PadJosDQhcX1Ed+yJd4imSDwdF4yvtAcjlF5EBobbF3EvtPP/mbrCE7cerdRmAF5YMedNl9TZug5AXPia5mGh9skZfnaCulpZ2/Ws6Dv3FrovLnwjjQyEzd+kkl3wGyOItZ79QRvjOk+ZaCPsInthM3iHXQPjxBP5IjGfaPnrLIViFYSEos8ndfIVeAjzrkIwt2YMy4ist1j8JIaXguglesN4/IYqIqqsxALyWvqzgwr6yVTTj182fdDcB+2hZ2SrD+jXMIb0DqCw123QbEgzRiojO2McVt83DZnUUdhIQINgXW5IDQiRNON5e9I49CiXl+09fpYjJdJ94QW8lKmYbf5Aw3Myaqik0lvDuVk3WMxsqpxJ9IQUWPp0XVg5lKSTEsf08sNt+EhF0UfzvZ1458s3s/dG+UpdDjGDY1isYXOg0N7rqU9tjtQYmF9t2+bQrqbQar3O44UGgo6ytZ5iq+xrpPiNpkRCTSNV7ClyobWP2ic6ODl0Vfo4mLxrOFesavEjSPO0QNG4b0vHzzaCTd8xRipOW+vGHKWE4tqprrpj4rO8W58tPbdvUCFGrczttjfawnU9ShFFzg1+cxg0LCq59GdTmUynUGTgg6JyF6o3Q3te+xUnuO851Oh0Y0O3igH3yfb2X+YWieOm8dNLI+HOXPSzrhNmXsJeJGwWoUGm/FWObMnvDcz4sSsVXdoqhPOkPbutu6AW7DdllBxms2pDc2O7WHtXyeL9W0bwN0Mq8M9avGjFxwSIj5XF2PfUdXaQ0Hw6LvySHaHLX4ixBGNbvb2wcWRfqFjpSixQLmWUJCUrhUkVX8tt2iJr+2DZw44HrKy68jFzKjNTsDPoB+PKYxdj8hWFjaz3+9hwivGITih672GbqBhxB/gH6gI0MfshyFfni9zhTvIiY/Rkcm4rrppx4O2hlr6JPuWi5MZ05tTLM5cdzKnUqINGrRDzDY00Yuo7Ym1APkwz/AXGTEOWS5YBRTShxsfX/axLd+xQ38ikv10aGSW4m7q6TLMk1ocU4+6kVcBpsr4MBeCpYKy9mUy6dfN7Qzft3rodYIz4td44/I7fw7Jkdt0Wro1rjuRUS+XM5HeXS21pl15BLXAugpIuHLLxjWLrhnGKIiDWYdmC13iYXvj+mg8+zUlJ16RKKXlK2hBRWRQoxpLX9OCH2wLOYb7QqGVq+oDawahx8T0olbKnnHTPSpBg9hX8Znvy7EMKQxBjHMCJyykY5fhthsnlJpspb2eTYxJWR8CPW9g4ybauhcbw3CpTeW6wsedI+HiudlGmRs2xS6LsPCwMY/73q+wvI5ohI0k0QM9dMIP8GiUNnRnzgYpDTln8NycrUvKpRyoXQdpX0XcFif1yDyS8YzsKiHT2pBJ2n4w8IN4CJwNKwXaFMt8dDht0fPtchs1YQgx4BrNGLJ7OJ21bRQg/H7WwJ7hILaqqCPIzg8sQS3pQlvjRGhUEEqc8t1o9rM42sxhd9JZgKAuv8WtG9jG3CuZz5y8dQPOO+PUoFCx/NgrF0y1QMfcR2ZDeemJ4ppmg6/XJISm8LbeSFF3z661vT8Vm1kAoSmnjmrTwnT6FO0tGW7TeKTl5EhYB92TPfYo94GKGFuBul66x1A+3AMFGVS3X89VCZUI0wveuR3Ih7H29TpoHrmWB1GU0vLA97IcIs5cBVUloGJ3v2JGSbiDnreezmhkSaixdcxLyx55BJpRhxNTK+8zNNkqhmOdVHvHHbac6hNWymGOeGfoaA6Lo31dfvd0QrnJguWt1MrulCudxN3aAzFCgxPdcXeStoSOwGQqwLytiIn3gAltR8sPV5LFEL015CwlN0ukYoRKEQgtDu42G+X7Wa5JhOiduujWJtnsxCCz59rbDTIcYnuCu+0hoSOJh4meaMqXhkEiZ9uNlbxeOx2q1fo26/N4XQj3QsrJomMcA23MAqDFVej2WeK1V9h81BtP7ipLhQlsRK7bfWzJ7NGkCdBijCi2nR6oeN7gQzbRIruG5aiGmmbX5QqctE7RjOFNHuMy747eGaVOUAl5OzE/OBEidmAlLoSCOrRgnoXsDc5BGCpQN/jhmOqEII0Puad73aCJZrmnHMsUOsPbOnV0r9Kc+d4/+guzv1sgcGUZYV4i3vanR44oZgBBJQAZE0mO58kKCqKHYvSYSFK790/13TPVPY8Lpq3SOgUY48YmUS7cWj5CD2LAM4+xmi6gNj2YFlvJu1wBpm/C8bgRT9g+TaXenDs6C2x7bxmS3fPMPR03OoPFt45EjWFjTSkv0KTYDWYuy+nYjny+xdh9BsVXCRYuftuoA/ZQD3tVlW4aSsFI3/anfc9v16fNrnGUDULWez4b+hQCUKPjunwMNKFPHQyn8JvG52ALjNV8NOPrRk19Mq0VeCCT24PA1/dd32cUD+J9SGmYS/cjvsaG2WkrZZS045Vgs7q5SRbKHyLDORZ6UyJGRfZMZrLG9Wb5DWp7+dKCrKcpWo/JQWShjM81fKrWtUwY+whs7KVTw1yr23zmbQNSqJ1MrK/yLb/YuyQ5igI5jrBm7C43Ec2UrtR26C7Pt/6eGyqRvR/so6zY0YPVkliPGQ1xDBd1Tw4dWvp8yfdyemrWj2LGtsoxgVEzownD8d04c9sIJYzrg5IiTQv98XSKNbJHW09j0NGVN47aiAGFRM6JBy0iNkPtOboQ/gbjKWc6IYe8x3r4ePXWG0cOWvR4B9xWeLbUNqXYA/QWRyiHb9cKL8nakzzX3yB3cx/klN8PKSPIGCs1oZAbsRnss2ZvM80AOewomfvw0c3rEFPbOAXbPYRofUvEK+3atcIo3Q5IgzJ42TobY37Yez1jzqfSq2Cexk/HAd43MI7kQipdjldjI1IJ39y8YRC4E7UJUrAtB1srdqBAijdcU/cituEpsVS5xgR9GMlv1vXW92wXCdzNVNvBrXk0gdzOkH5jUDKVffJG9a6MXhoJIN4WhwMtOCr8OX60ucWp5NpIz91+HmNXCnTfvGaGB63F8TEy8YXqCN8zYJGHEUjzb9mDlR7+Tdps1246RVMThFqm6CVgud7PN3WHcDeXhZEUaVMGoz0d9LGdvsYkjVA93j+xt8cdxddp43IjY1XxNiTS7FoYLFWY+5a7xkZAZAX6KJO4w1wh4Zjs2qUFik2xqsgMymKXOcbc8saNQUip9rmY7wPLMkmmBrgizj7oguLSTHyIPpgPtUDY0UuVgV8bObK5It2tGbyobUWsOOPJWUrcYqujor5Fe7fQkM2B2Lug5SrlkYu66yHskcdwoUDHHcVkjuFpJuSM6hcnSYOknBruzrW/mwPpJIIqoapZ3anK34FBjRUNCO6aZ50MYHbTqNdCYKeuQ6q48zzydI1TKZzN3rqHyRoVrHlX74nYmk8nq9vTc+/xKYJRlxkqb4fcbz077WLvDnsOs5VLjaknsF2AznCETs4wBzaNpsTIShykXWi9k4Zi5/vHXUnZzv2syjHJOQZc2uphG6KuLDu35haYnAVbyKMzCA9AWDX38bw7egxx8qlBC+r+FlGQQ0legjVTOiMjaXMzF+mhosp4ulfiw1QrJkJSJDQ8cnn9IDcD0hPZaSudI1/aYKzneL5pR5sIdcC2KSlEYUBug68IdlMgF0/t1G193Wibm78ZIPfMN7Ye30h6EGBsEA1V3hK7zswhxvSbrrMbmGsel1boJ8KfkId/KaagFIKU0UqwpTxOlio1haFvKwyBEV1xzw9K9EOfsRTXTVwmNRgvUM9lgWqBENKYxyqDx3stauAyzoxFqgjVPoKqTgltrVTnruvg3eNKlWfFt+qIOPJbU5cpC/M9HRZczZyjE7J9FAhRz0GsUPvHBvC35uHuI8i79nIMSpNGSL9eV67LQu7jANESL55Ir+wf5VTJ59qGe9BUBNsmXJOY2QWIHExtbJo1bA/X9ckeRArpURa0BwN1vLVDA8vr3DLQIaeP8X4k22G/m7NjtIEK8qRbwfV4RSsdda/Zbii2hzzmb4ddfURx+IBpFX2Ot8eLfjGImymdqsFBhL6ot/Z2x+xKcq+1USHmoZZKdmjL0Fo1UyU+jwW+wac1ur/uG7Qf82EecpT0KETw7P0lMMd5JhNd8Im019YVeuArB0PN/h74jlrMSnTs/bg/1mVU3VO6iqBGQ50mDx4F2o1s4PcXuRDNCiLDXeAd8gENEXHTJNBaoTGRJHc3xYzKrK78IG5FxYcG+SETsnDZpDRN//Wvbx/elgMe78c0/r0joctXvP/Pvml+fSn87fzX82iAb3ufn2t9/jf1+tuHt8aNgVav79XbrA/fv4D+h2/VP/63zvwsIqbXectv51Beh1s6O1z+T8JbXHh92zXT17bMnufAwAynb5czzO1yzN0F778/5fA6bPjbN+Rd+bWyF3fGxXKyy/diu/PfL8P3UwYf3rwJRCl2268ogX/1m2ox8/34ELAO/bT5hL79/X8DHim3ejMyAAA= -->
