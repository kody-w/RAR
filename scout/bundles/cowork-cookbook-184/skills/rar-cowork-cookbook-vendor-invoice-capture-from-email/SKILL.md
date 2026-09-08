---
name: "rar-cowork-cookbook-vendor-invoice-capture-from-email"
description: "Scans the mailbox for emails with PDF attachments that look like vendor invoices, extracts header and line fields, matches the vendor in USMF, and creates pending vendor invoice records in D365 F&O, skipping duplicates."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_from_email", "rar_sha256": "eefb44368fcdc70c35a1570f3702061a81099b9eaa123086a9912f92023e6122", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_invoice_capture_from_email`. The original RAPP
agent is preserved byte-for-byte in `vendor_invoice_capture_from_email_agent.py` and in the RCI capsule.

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

Vendor Invoice Capture from Email — Scans the mailbox for emails with PDF attachments that look like vendor invoices, extracts header and line fields, matches the vendor in USMF, and creates pending vendor invoice records in D365 F&O, skipping duplicates.

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-capture-from-email
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
    "legal_entity": {
      "description": "The D365 F&O legal entity to create pending vendor invoices in; USMF in this recipe.",
      "type": "string"
    },
    "mailbox": {
      "description": "The signed-in mailbox/inbox to scan for emails with PDF invoice attachments.",
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
    "processed_message_ids": {
      "description": "Record of message IDs already handled in prior runs so the same email is not processed twice.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_capture_from_email_agent.py` and embedded as the fenced Python below (sha256 eefb44368fcdc70c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_capture_from_email_agent.py` first:

```bash
python3 vendor_invoice_capture_from_email_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_capture_from_email_agent.py   # or on stdin
python3 vendor_invoice_capture_from_email_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Capture from Email — Scans the mailbox for emails with PDF attachments that look like vendor invoices, extracts header and line fields, matches the vendor in USMF, and creates pending vendor invoice records in D365 F&O, skipping duplicates.

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-capture-from-email
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_capture_from_email',
    "version": '3.0.3',
    "display_name": 'Vendor Invoice Capture from Email',
    "description": 'Scans the mailbox for emails with PDF attachments that look like vendor invoices, extracts header and line fields, matches the vendor in USMF, and creates pending vendor invoice records in D365 F&O, skipping duplicates.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'vendor-invoice-capture-from-email',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-capture-from-email',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8530ce0f820300bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-05', 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/vendor-invoice-capture-from-email', 'uses_skills': {'custom': ['vendor-invoice-capture'], 'ootb': ['Email', 'PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_get_entity_metadata', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}, {'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Cowork session signed in with mailbox access (Outlook plugin)', 'Prerequisite: Cowork D365 ERP plugin enabled and pointed at USMF', 'Prerequisite: PDF parsing skill enabled in the session', 'Prerequisite: Optional - Cowork scheduled task to run this prompt hourly so capture is unattended', 'Output matches: A run summary of the form:\n\n> **Vendor invoice intake — INV-2026-05193**\n> - **1 new invoice email found** — Contoso Office Supplies, Inc. (vendor US-111), invoice INV-2026-05193 dated 2026-06-04.\n> - **1 record created in USMF** — pending vendor invoice header `INV-2026-05193-US111` plus all 6 line items, with quantities, unit prices, and descriptions captured from the PDF.\n> - **0 skipped as new** (prior copies were already booked and were skipped as duplicates, as expected).\n\nSubsequent runs with no new invoices return only:\n\n> `No new vendor invoices — same invoices already captured in USMF.`'], 'confidence': 1.0, 'deliverable': 'A run summary of the form:\n\n> **Vendor invoice intake — INV-2026-05193**\n> - **1 new invoice email found** — Contoso Office Supplies, Inc. (vendor US-111), invoice INV-2026-05193 dated 2026-06-04.\n> - **1 record created in USMF** — pending vendor invoice header `INV-2026-05193-US111` plus all 6 line items, with quantities, unit prices, and descriptions captured from the PDF.\n> - **0 skipped as new** (prior copies were already booked and were skipped as duplicates, as expected).\n\nSubsequent runs with no new invoices return only:\n\n> `No new vendor invoices — same invoices already captured in USMF.`', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'The D365 F&O legal entity to create pending vendor invoices in; USMF in this recipe.', 'mailbox': 'The signed-in mailbox/inbox to scan for emails with PDF invoice attachments.', 'processed_message_ids': 'Record of message IDs already handled in prior runs so the same email is not processed twice.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Shrinks vendor-invoice intake from a manual data-entry chore to an unattended inbox scan. Each captured PDF becomes a pending invoice in USMF with header + lines pre-filled, so AP only reviews and approves instead of keying. Duplicate detection and message-ID tracking keep the same invoice from being booked twice.', 'expected_output': 'A run summary of the form:\n\n> **Vendor invoice intake — INV-2026-05193**\n> - **1 new invoice email found** — Contoso Office Supplies, Inc. (vendor US-111), invoice INV-2026-05193 dated 2026-06-04.\n> - **1 record created in USMF** — pending vendor invoice header `INV-2026-05193-US111` plus all 6 line items, with quantities, unit prices, and descriptions captured from the PDF.\n> - **0 skipped as new** (prior copies were already booked and were skipped as duplicates, as expected).\n\nSubsequent runs with no new invoices return only:\n\n> `No new vendor invoices — same invoices already captured in USMF.`', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Cowork session signed in with mailbox access (Outlook plugin)', 'Cowork D365 ERP plugin enabled and pointed at USMF', 'PDF parsing skill enabled in the session', 'Optional - Cowork scheduled task to run this prompt hourly so capture is unattended'], 'prompt': 'Check the inbox for emails that have PDF attachments and look like vendor invoices. For each invoice PDF:\n\n1. Download the PDF attachment.\n2. Extract every available field from the invoice — vendor name, vendor account, invoice number, invoice date, due date, currency, PO reference, line items (item, description, quantity, unit price, line amount), subtotal, tax, freight/charges, and invoice total.\n3. Match the vendor against existing USMF vendors in Dynamics 365 (by vendor account if present, otherwise by name). If no confident match exists, skip the create for that invoice and record the reason.\n4. When the vendor is matched, create a pending vendor invoice record in the USMF legal entity in Dynamics 365 F&O using the D365 ERP data tools. Populate the header and lines with every value captured from the PDF — do not invent fields that are not present on the invoice.\n5. Avoid duplicates: before creating, check whether a pending vendor invoice already exists in USMF for that vendor + invoice number, and skip if so. Also track processed message IDs across runs so the same email is not handled twice.\n6. At the end of the run, summarize: how many invoice emails were found, how many records were created, and how many were skipped (with the reason).\n\nIf no invoice emails with PDF attachments are found, exit quietly with a one-line "no new vendor invoices" note.', 'steps': ['Open a fresh Cowork task and paste the prompt body verbatim.', '(Optional) Configure a Cowork scheduled task — `Hourly vendor invoice intake` is the pattern used in the verification run — so the recipe runs unattended every hour.', 'Approve the always-allowed actions list on the first run (Send email, Update record). After approval the recipe runs unattended.', 'Inspect the Output panel for the extracted PDF copy and the run summary card.', 'Open USMF → Accounts payable → Vendor invoices → Pending vendor invoices and confirm the new header and lines.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-05', 'what_it_does': 'On every run the recipe:\n\n1. Scans the connected mailbox for emails with PDF attachments that look like vendor invoices.\n2. Downloads each PDF and extracts vendor identity, header dates and totals, currency, PO reference, and full line detail (item, description, quantity, unit price, line amount).\n3. Matches the extracted vendor against USMF vendors in D365 (by vendor account first, then by name). If no confident match exists, the create is skipped and the reason recorded.\n4. Creates a pending `VendorInvoiceHeader` plus matching `VendorInvoiceLine` rows in USMF — populating only fields actually present on the PDF.\n5. Guards against duplicates two ways — a pre-create lookup on vendor + invoice number, and a persisted set of processed message IDs across runs.\n6. Emits a run summary: emails found, records created, and skips with reasons.\n\nIf the inbox has no new invoice emails the recipe exits with a one-line `no new vendor invoices` note so scheduled runs stay quiet.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scans the mailbox for emails with PDF attachments that look like vendor invoices, extracts header and line fields, matches the vendor in USMF, and creates pending vendor invoice records in D365 F&O, skipping duplicates.', 'example_request': 'Check my inbox for new vendor invoice PDFs and create the pending vendor invoices in USMF.', 'inputs': [{'description': 'The signed-in mailbox/inbox to scan for emails with PDF invoice attachments.', 'name': 'mailbox'}, {'description': 'The D365 F&O legal entity to create pending vendor invoices in; USMF in this recipe.', 'name': 'legal_entity'}, {'description': 'Record of message IDs already handled in prior runs so the same email is not processed twice.', 'name': 'processed_message_ids'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants unattended or on-demand capture of vendor invoices arriving as PDF email attachments into pending vendor invoices in USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open a fresh Cowork task and paste the prompt body verbatim.', '(Optional) Configure a Cowork scheduled task — `Hourly vendor invoice intake` is the pattern used in the verification run — so the recipe runs unattended every hour.', 'Approve the always-allowed actions list on the first run (Send email, Update record). After approval the recipe runs unattended.', 'Inspect the Output panel for the extracted PDF copy and the run summary card.', 'Open USMF → Accounts payable → Vendor invoices → Pending vendor invoices and confirm the new header and lines.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class VendorInvoiceCaptureFromEmail(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceCaptureFromEmail'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'The D365 F&O legal entity to create pending vendor invoices in; USMF in this recipe.', 'type': 'string'}, 'mailbox': {'description': 'The signed-in mailbox/inbox to scan for emails with PDF invoice attachments.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'processed_message_ids': {'description': 'Record of message IDs already handled in prior runs so the same email is not processed twice.', 'type': 'string'}},
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
    print(VendorInvoiceCaptureFromEmail().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
