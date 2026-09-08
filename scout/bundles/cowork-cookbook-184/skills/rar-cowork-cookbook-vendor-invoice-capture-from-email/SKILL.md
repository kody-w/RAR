---
name: "rar-cowork-cookbook-vendor-invoice-capture-from-email"
description: "Scans the mailbox for emails with PDF attachments that look like vendor invoices, extracts header and line fields, matches the vendor in USMF, and creates pending vendor invoice records in D365 F&O, skipping duplicates."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_from_email", "rar_sha256": "eefb44368fcdc70c35a1570f3702061a81099b9eaa123086a9912f92023e6122", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/917aZPbSJLlX+FqzLarB5Jwg6TGxmwBEgdBXCQAAmSrTYUbIO77qO3/vgFmSlXVXb0zbbafljKJOCI83D3c33PPDP3ywem7uGw+fPmgB06x4Z0sS+Kg2TiFvzmUY9mk4KtMXfB345VF1yRu35VN++HjBz9ovSapuqQs1umeU7SbLg42uZNkbjltwrLZBOtNuxmTLt5oR27jdJ3jxXlQdOtYp9tkq+AsSYPNEBQ+mJEUQ5l4QftxE0xd43hgYBw4/rtKWVIEmzAJMh8MyJ3Oi4O3RX/M3pi6zH18DfaawOnA+wq8S4ro71bYNIFXNn67zjniFLnh/qf6cdOmSVWtg/2+yhJvnf8Z2BpMTl5lQfvhy1/++vFDAq4/fPnlg5c5LXj04fYSfHqTe3Cqrm8CrilzdrUezM6cIgLDqhm4ugD3VdAA5+TgkR+Em/e7n9ogCz9u/v3f09FpovbPX74Wm/fP1w/rn2tfvEztSqftAmCeUzlukiXd/HlDZ6Mzt8AksDTYBmfTgp0qos9vM3+VVFab/1zf/fS2yOco6H76+qEEKjjrPn798OcN8NDXD02/Xn9epVQ//flzVo5B89Off5XT9u4z8LpVGND687f3+3exYOCvQ5Nw803X2MP7WsDrSRUA4b+xb/28qf4u7t0l394G/1RWHzd/LHm15z+Bvm+x6AK5fywW+ADM/PD5WSbFT+9rNCUICKfwgp/+/M/EgvDy0ixpu/+W3L+8CX4L15/eXfLnj6/t++sGerfth8x/vmwFAuZfsQQM/77cD0f9M9mvnf070WtWtT/28g/F/dEE6D83f/mntv3fJnzchF8/HIMsGUDcuVnwZfPLK0T+8if/14d/+uvfgOj/Uoxe9o33kvAtd4okDNru27e//Kl9Pf7TX//yp74CURw4+be+yf5I5h/59bXO7zz4Puqn388F65tFWpRjsfmRQ5tfyup/NH/7vLk5WeL/+rz9svltJq4faLMa8X3RNxf8JhtboOtv/PjnD38D0FMAa3rv9Rrgx7/920ZOvKZsy7Db6F7ZdxuwwV2SB6vyRpwAeHsDyCYAfm0T4Nj3cSD+1x1eNS7Dzc//y3uh/SfvHe3hN7T89o6W37w3WPsWAlz79oL1nz9vDCC4bJIoKZxsc6U17WvhRADc10WrJmiDZgBA5c5d8Ank86f1YoXbn/9L2d9eYj5X888vJE/ekO96OK2o1/ZZ8Hm1z4qD4t0awD6AMAKvBytkpQfUCZNsZRGgRZkNADVXXwB0z7KNnwBcASQ2v2QDf31Zhf3888+u08ZfizeYxjdv7NbCYMAPdTafPgG7wiyJ4u5rEXhxufnTL3/70+Z/b/5vs17C1zU0wBfvuwE0FHVV2YDs6t/4cN1aAB2v3fjlb+/eBWIKwH1g7xJAe2+TQXSmgf/d1bpAf8JIauMGwMXAvXlVNt3KYEn3eXMKNz/0BYuur1Z2iMu22/jBSoxB4c0vKv5a/PBkUXabFoRgG84fN30bvFb92W2cl4o5SHOn+3kjHzTARWUG/lnVfA0Ck8sC0Gb2IxDengMhzZ/aDfNdxOeNssbjpnIap4ob532N0HnbF8BB36cD4c6mCMavxcq6weqqV3K8uQcMAp7x3rf007rnoEzJARK8EXv3fYyzMqbxYs7ma9G+B77TvJUBQJV5E/WJv9LBf7yHVBuXfea//Ac0fSsyXrvgv+/KKwbfuH/zTv6bd/bfrKG8efH/5muPISix+f+4QFr9QPP8leVpgz1uWMW43t/2Zy0Z1318qzJBqfIy+pWLv5Yv3yHqO1J/LbIEBFsz/8fbyNeuvo95Qz/gYR/gzfUlH4QUMH6V+4r4NYKbZs0V52vxnRKAvZsX/oFNB/AA0meN2u8Lrm+/axoDDFjvfy0P3v2wegxE9abqXWD3JgwC33W8FGjVrFn7vssg/IM1g8c48eLfWbUB0kGUAfkboEQCtg3QxucfMP329rvqv5v4VgWtU14VYl+sm70KAHoEq4LrXq4RBNTr3ip0YOeXlxBgRl51q+0uSBtg6dvDoAnqPmmTbo2jN78GFcDnT+v3m6Xr02CqQKYAZ4F8qHrg3VcGrbufg4gDOgAQAQmVJwXgfOCUdye8BDr5CgcAbt+L0jeJr8fvBgWvtFvJ6vvEV1CCOSv/v6WQU8y/RQ3jj8IEyMvXEa91/z7Sfqz2nh0pSJcSrPj97Vuh8PmN69+Kic13uV/+oQX66V/rkl7sbf4+AL5s4q6r2i8w/Ma43wn3M8At+E3X9p18P71n4qd3gvy0uuTTCzJ+J/jN5i+bf02534l4T44vG/Qz8hlZX0nvwfX+Ab44fGLun4j17dfiGvwKq2D5EkDNCvvZDNj+Bwd+HwKIMGqCaB38xontSqUjYO8XCYBt+Fr8NtrXbAMcU0RrdLblb1DgVQyAyH/btR9cBV4VHVjbX4vHKFg7tldutMGHL0WfZR8/FCDu/hud2spH+RrS7drfgeQBtViXBK+7F0JM3Xr5+9ZXfV042efNMehecP6bsHtnkZVFf5Mdb0YC4zywwseN/4JhEJHAyHXxNbOcFoQqiNLVmG6uVu3fmrq1DMyAN7NvwGgQ6P+o0Jol3xF78xq6eRu6gt4b6P8TzF/B/j9eDPHGnkn7bscfavFOZH+sQJtEReCDEP7Od3BSrKwHVGjXau2P2O878/yGBf9w4R8l8j8uba2kCdbwyy8rTX98R0DwDdqaj5sfHQpw+nvP+Orvix60439Zu6M1Cl5T1gswB3z9mPTjpx5u8OGvf6AXmAh82IIwz8EXCPVvid/+o47XtxAHNPE+bHM6ArrKViJZGaLws+BV9FZNArwElGrf0uAdP19uWxlxDf4fa266EfjuD/wFFHvBPSDN1cZfnferCeWr23uZkDnd2w8nfvkAMsEBoem858J7uwCGA3T81K5FEgzgAiwI7t8SG7z71xuJdwFt7IA6FkgIgtAlCJzahZ7vbREPJx2U3CIhvkUwhEKdHYrs9+4+cBwUw5Ed5ez3KBbuMQTDAwrFMCDvDR++raVgsipF7rchmISFBIohvh+EGOH7O2pHeeQWQ5y965AuuXfcX6emSeG/W/pm2d9e+/ve06weeTf4lw8uRYCRAtGe6LfPAYZQz7Vg71pJkNZAyXMMvac4PvTGfd75/c6ux+eMpoyuT/dnHDByHE/6ieLZu59CvEje4sNYQIQgaHebrELPRG3/IWrH1LoWQjD2g/w8sF3m4zdsMFDTJo2nSvDYneHz/lkpuBPoAtUdpTkpNdQQNRSqyq1pTdBwG0I0KIbKM+ts5pKY6JDBrxMzjeHbuayp2Ksfsi2RNzurKNgqfVG31L3Z3qqgLhLqKJpbTH/o4r2akmpnQ07wJPgGoYeDLWRiJLLirdweVPlAd7eQqlHaaqygERAKDpYiH20iCBI7eOCRLV4Dn7tdAihPA+5oFFOgDkWd2DB8q5tTI53lrvQ4JvMCwwgFbwy0raJQkDYUBUT2CacODbQEbWiHJu/AVWX2p3Suh/PtUQnk3dHsM5VchiwgEyzJRZJrW7Y+I037WLBTidg9+egLuaAfk8M+ooi/GdtRQYEKDZnvYljLjeO9tu2bFxWH4LokhoLGW929yMkkFpNXzKe0NDxFhSd1nJtH8OwwJzxT+zsS7B9FeQIOlJZIitBRU+pIV5vHNeIPOwieRJI+WcdKTAqiSLY3VG/mG4UvZ+6oKsjVvV/k6yTeAtE6Pvil9oejsnVT/DhnrIWUl9EuyVv2OJwco8ZYRbL00zlVRq00GKKr45NQHE/KVoD8zDbK+Obz6vm0O2ramM1lXVZn8wpHj0elcY9UgnexUN3DCDrAiG6wdSPXA40eg+pGXtKdYSHHY3e53BIeMqrz6blgUHiVF647Ehnh3aHgYt5OMlWH1PnAYh0n3E05MSxanvBsYLEs2T3OKrQknO7yUXfujNuhYxxkZIK27uy92ThsQsZ8klkyBkmd3OxZabKp6grfTm59Y7D8hmUQiAh9Hq0HrkbInpHQY3i3G/fa+ffggj2PT2S73OkdEmLxOayz2+PR3pBwDxeJSwUk3FRBtsOsfpZmE0NmE93trohxbwM2vCvKbUdsb1cIUx79oSvVKuijoKd9Ykehljgg8E7lxt1gaekMT95AUwMdx/aVqGjyoRImkbBdzEuGU+80uTwT3V7GjN6+LSlxMZWphNNhP7U0rtHOPJ23DHyvU5QnHWhHnkSkNaPOosJnKtZSe6Zj/XG26vbQVLKhXy7XmZsOCb3bbXMZUjIPLqgqp4SOjgtaDFwIIU3ITu3qoQTHYatK7JINnpgx4hDjO300Z/khXRAyKx1vxhTVzJ5Ld7o7Ue08ESOVjSeJHUHQJGdp8HCvEZjCOUdF3IoXIzRClUvuLNHOO4yFdRFXYOW8PR+PW5eJssvF5rB2lhT+XqjM3BDOqfakJMll2SaGkdOuKq7KQU5UMSQupljH0bknjls7PD1vTUXmHrG4iKyV5XVnX2MWkwYSvkhUU3miUjEIyfiLIKQB2WVjVfjCY4uediPmL2RlbGHKnmstUmbomQopHd/LKPEOuwca+PHO3BnK9nq2ArSIj/DdPZ842PCgq1pB2vZwnsVwK2+vF3hvFP41Xji7UFtXicYov5HkcSsd9prcPs0HiREnNi22UjfGJ7Q1bqXnJ+O9kAKVTlpZzOkCJjJdUi22RTnOM5nYRehq7nz3gct3bAoazjJL+x4EGpE3O3HaIVtJPIv2SGy5YxMKvK81FHfU5kOtOQHd2V0dPLRokSCpvqRXLIaGvrBxvBw89ejiiOTBrNYRwSQnMasSd2UPL2FOmd6ttQ4aktqMFCCnmQ9GSthJ1iCGd0em7b16nEwbhsr2FDmc3g7cHu4ZIzlBR1rq1Vl8IunxVi/Ds4MIemAROWpiEr+OwnR3cGLepqdHZMgcosZJfk1Fd4aaOzuernR/vRQH2TCLPBv0/Z3vO7RAzm460+rjciOo6VDYlGnWZjWYZK9RO7rjlQe9AhbG+PfhVo8pPRADPXS74a5ZSD0OxNOYDCouNHR4jgDnn7v9KYWMGM3P3u6chcx0KzOO2u7l1Lb2V4oTDuOh34eGFsBuTvfbftqfj51hJjE8HNPdnQ2FZAE5/Ix2nsDcawHV0/3sJKEi7yG7Ybnx0dOdZaDYbn+WEpIB3ffVuxbELSOH2FcGeIoZo3nsly1dPYUY2UF5NUcaBHwdo7fb2ct9WYyzmiHCLu4YXlMSEgz19qeH16V3/jAdJ+3k7WLmepvYhzwXNzrKuex5Vsn2SPA7tn+qk6btu5MoVZbHulqIdmx2fVwS5m7hGnOVb+ijdh1W2NaUplcn8hxkOjl7z4vPLNuyJJ8dCHe7yRK2xnzcU7WIvTPZk+PUbkGRU4AgTyts8R3kTnBrDYf7CZGFltWJRxjv/SfCbk8xaya6oeqiFkmM5Q3J87RH+qLqJywRgd4OP8ZlkJj2nrjpztO8IhAHJ0+KjutzkoPimOOtZ2mpu+UkPo8BCICdOzP00csjTj4wx/hBD32XbKm0HS4gZ3kE9dpS2tXiEWove/gqxTdd2vOQvCg6u2NNLr6Up9Lkj0lB1+N1gW2Dw44siIiZSOTMvJxrgp6ZCTqah/qZ2e3tnsPIcI3yuUicyeVoNSke1xtb+yWO8WhYeCddB6Cg3zP0UEConitYDdOlxTLGvd5LkHk2kASmb+TESXrct7xUy5N82TccnItxfnwIy22qfFSbEleL/SurGQ8nPaVkvZ/ju1jvEZmJ5EsRit5sspm/Zens3ljWo7apvKP24hwcZQkPyyjaZ+g5Hqq91VDscvGF4L5Nn4dcPImliOyrhek5fXlw0ZWN76B+fLAYzcDKgxqUQK5C+MqKPn+S+jjcPsK8TO93YcuW5pU0uGtTJ+gTDa7IrEqQL6Z8vitu2lMhpFZZVNdpiqT1p/F8kZdiV1wsSe0ctcuVXXY66rBmpJR2lNNAULeHnHWPd0i/qmmgIihNq7x9VGPTaRFESXc35nw/RR2TymWfngNpOCZmcSqyspTMaX8vYYeuqqd0PPc7NWACU46ovcBsbYhzFNk6ZEfe5RByf1fPas/JTOyleZUcCL3VS6jZFTZLR+PlhAY3/VY8gtNt38XCvhKelVqU+3saHA7OBbKlTLfMKjaFnS2coC7FjmkryDR8PFp3rJuF64Voa8EFDEImnapeuFkcLNLQZsaf076+XXjlcN0huJVx3kmaaCOteJnh7eB2Uc5mHunIfBgY26iLgj3fEja+Nr5vuneBdjglrTo1TCtI16hSOO4pDEFSD5N6U+2EaY/tCrY/h5q2DNO4CxAtEh/PydTt+GZAzImpTuNEe1qgEHFIZ629RRKN4WtzLOjxVAhJANWpR4bhkviasBAev/dYrByq8YRl1yoJ1RSbyXZmyoAeeUMKBtN3XEkdWtitkQlSZTNf0gLbCekFRwM9RxTWweY7d2kf5UjMN3qW9TQ+ysWgs+duZzJJxajSJVG0yxNvQoY839KlBKAltP541UnOjoUc1EJaRlNP/qY8gzN9FqxLQfaLhQI2FvbO84gXaZtoDmIxrt4ynbKLDzp6vbnlpWaTcu9Tnkbtj2puSmTytNm6LchIQcvwthVCjbd3UXoAfVGliXXFnliXlu9U6ac37FLZe2v2djXk9pXIC5l0vKCnU1lhrGikk3SnDjcUP+XMKCXQxE7eQan5GA4tviIlLr1R7nEmapQ8eTlhjxUf3Qo+itRtozZYeWDEcMc4xAk6JEJEYU9eYuHydIa145Z55Id5yuzkNOklhjpP/MDVIV2FdZGKd/NsuqOfpy43OqHMXjLJZvnEDU+UWhwcUdfbU9+OrG3CepL094o/tHwcav617DjT9h0cOUbFkx92NO7Nz+gg4M7C2ry0h8o7GSqC6AUPY3B2jIy1cV2OAJWEevLE+ah3Bnqu692YkN4ce3KRHB66xxmVsqsDVxwpQsrUGeoxlveb4gyN+bOwd3flcIs4jzyd2fw4VgJrcImQMqM6Rc1J38ZCYws3Fn1cHZ3IlsPCJIZeeQlFPozE4A3F6Ymow5j7RUjZ+wE0KgyK8kGxPfqX83MoB+bMxuxA7FqEfWJR5QW7IRpxixYop55vLnkhGuhEWrFjEFNwdjrH7kRckuXRGapBka+ydbrgFzvlFyEa0ekJ2XzHFBkMP8gQDqQOTsv6ugV9VrI9q62VuNtEgbwHPqWPgWV6Ty9mhsyNm56qzxt3QUlLEJ/ZHlSKtlAMY41tZWnrYoV5I+vavp4UrzyywsKHokZctUt9elQwY1g52/XdobzCB98roVzaqnt/n5xt/mgot/pJEXekvi9BpBokFPu+iI2yVhdWsjBDmATSFdf7hd1DWRDQLfKMDJRkHg8vBgVp8bxbNRsiS1ejo6tO6B3tm6LXO+cSjqppoWdF05Md6GvCdlpihueobsbR/dU3c7frUus4XgqhGWoVafqt2h22xHnY5vwxNS6ypx4uGX6aarWLXfr8nBz3eGTM7uxczFPIZkwg7M6ROI5GnOAPqnlWfjrQrkPBVz1LhrSteLxEuJOtByXYYrV0sazpEdu5n5dQzethz/gZji9W8PS4BwBAWOkHOEXQlivclk+2LSsq6K21a4sxc923ZblCFp2PKyq1rqAZfeqJh/HN8HiWAqFyYRZKdRykRxYbb8HZtjWQT1TSinXC8SZl+6IbREmngeeeNgZWTCIJmhCibTCSR5/GGMIXJ7asUAi2CRLyBlG3TsZcEyTSYEySBC3p48tFwvVYdw9pDrNWOcqiK4VHvvPYbSlWjF+erDCtIbrn9Qk7hUyc0BOXHOMgGYirrlJEE6H13d8KVgq6PthtnTuFM1BtqUtxvgdIWaVmMjUoJyXZHO/8LQZRODRgF4WwZakvyaMjOheegXKeXR6UCKWKe6Gmq00bOCVOtFByd+vUwyw/yQPlD0YlHJPyhnUonyzGHZVNuHpeZsLiNVOh5z5hii2Enbiz3pE4ZGHaoT8Slp9P4nyt2QPttnVexWm2v5BEcSiNHjWTo32g22tyYXQlkDSNceKzjXI70sLOB525BKB7QK4+e0HyR/uQM86fyMpnK+qySI96gmY5dh2oON4XNMzyi2UwbXAPfSygYUE3hTK+h9Uha3LR4jxlOVZiRChYyZtKMkqNA8JjsPY2ncyMUujhgIcwCgpeHzORwjdgjek4SIswL1f3LNY7B0G0pVE+3yRb3abeyIJYn5+FVp+XCed2Kk/0qnqnTOW4KP4cUju/4txnwyc8KsEGyFY2yEI5elg0Eoq3Ervks8yMKOtOVeFxFrtNebj1EOQS0TIdMzZSLgeXnNEBQR/Z6UKB/lvVdVEpe+meJ5NKGUbOmxwhm9YZDXthKrzGTLoZtpQDSPl95ox4zKdWqJLhciB9LMHK51nuWXdIrtip8wWaO0aJAFVYOTtpceprKqNqbVFs35UONYZp0NXxVM4ng+7GCix1FqVGD2TS9m8Re5ub3u179spmLktTcG1MM3V/xMbKzGx66y9L5UD6zmIgOzsX50TRQZdPqgfvqWTLjbO40wm0GDvdHykr9XcG5j5A+1v2NHESYwcdY1q83HpmJ+1G1vEYbK8vWEtZfL/4vmBB1YgixG4iQ3IkySU+Fk02wRNgnntwiEinyueJEato6FU3nVDiFjPaqXlEO953htlKBCSNL9bOHvEtun0mpYs/a2lciizBuLgyi+b5MDPXVkMjQ+89yZV9o5gikbeKhMQcc5tzfx/vDYi6sWEfq+qhidy5sActr6CEzgvLzcwdtLij4/U8mm6pA+nhHC/YzvXID+6DCe3BHC/xbjpXTPYYm3QPR/cLaV+NarjrXCunSE6HLqf5uZ71CmGNdLRQCj5xd4KpzokgXzBRJcSeU4tZFkVnO925nZxFz5DzeBx6HkyI3ktapF1wen9OrGGW0930dClBuebkRc12qiMm1P3QD2kioDESLdexu1PHbZ+hNLItRkdxkKAv4KN3XeQMo3TPx4TS3YM2Ats6VPCcIKvfdyTPOu008cSZ9ymqDbjoRsEn3+mNSTJYlDSErR/4Q+FstyHVwrZkFX5Wu+pe7hQSJWEu43C0NJsLFQcDjkoMI4RENe/Nh0tAdBIpZuafSvcGPdywWAwc4x5VJVWgGRlucHHrUTzB2b2FpT3+JElf3T8Gl7C2twGWRkNqucPFqE3PxENoyqgkQeCUYdGgUxhbI46WgA8i1mic7QfCsOx6it/2VRp2+4d3pO2dbwoq7qCwtYgDf0Uvd62rFgsnBZwV3BAaFV/VggaHYR6mjguBVOGeh+F02D3w7CFcO0Tdb7Ps4Yec6ODixYKPUq6quIRYvC9LHgI6eI9CSlvUqNuDPPY+96QqxKCezeQLl27hdgx32laC4YnjPoP0xzN8OAh1zhZx6pNbHFqa4F4CPz7j0+msGAXy7HGlDab0eM/dfXJUQ+g4qahjDRfqYgP4wy+GBzNCtR165MkbqgDar5wONBXn8eqIjW5LLFaSjKet+ihwDyWwIxK58XJ++H7Hj4/d3pQcpVs6gTJvZ65A75AXjfaJ7tXgYqgRY0wREYaq0Pl4mxEJgqeVX+kUxls4bdE3bH50zoxmfOga4m26RrqDt6B0L6e2QHwLukiSejaieBG3VLuYHFS1lB6jz6siHg/09XAvHnc5RFhYrOgLfT5ouny3m+vT6ftDqDR9xe0wWTAJPyB93Epvd86gtxG292nKk64pTKVkG7QERlALg8htcdUOYdWYLQnVgB6EJ7rY2XVXygmSxE03D3pWEHtCIsPL5bQwiuVxKo3L24CM0dvdxt2pNxNL8ZPzUyiWgsZ4zto1oYx0XD0HpLz4OtrARWvN9/xE4o+Fc89Q3s+SkTgQehiUxjAEvFC67oYiqiv61hAgsqOTAsdvl/K413zAjaF9vz3sSAuFvMJEHQpGyKj9nJiLztOdR861S5/J/HLzY9hk64mfhsDiFROTQrKXtienjYsHdsW87ursw30NinPzYCbKASdRrZkUmm7TECeX6/n6tK6DizPC3ZkXp3qKp2HwLcAc6HQUdostm45q7TXQIVQahRWYj5/x5amFl7pXw/a5bJ3CL4wBCW4Fm88QBgN2x/HYeJqIrYQM7BgkPOeHTgpDCls6dL+ENTQo8LZ0kgG70Y67uJXni3KLZcY+uXUQXV/OdXS0E4fLuWVxWthR4VudY6D6ktGa9OAyG/zi6UJtaNv00oQQBLNm8HhW0U7bRQ6TH5iM5TItVSuU2mMnZ3wwdXApVKgJOFTY7SD2sFiM+AC7qczegAxb9t61IokFqnlgw2GUK182yHxkjs/rUs1lPETbkTgOMsWleD8y7Has4KAcLGU2Q67qurvf3M479zFlTUY8fFx27HGG90pwteFwKCzejQ7mgjkFVZK0LpnCTiUciOJ1/wRp+IUU5LSCJ1aLp/0N3mMiVW397hoSYJlD1DsAJlsEMjV/ThVxiO+2ItzJcRc2PFojyH2eh87Vu/vs2pBeXC95WjXHuzYYhS4R4a052qdble8Hl+Iij/e17paD4v1cTLXRd0TcPa9XFM4eyJifJvmZzOaWcDAhVIaj4hPHwG4eJRLDQsRUzrY/H3ZbE6ExXE/Kfm/6OZdF7kHG4yLDNFRV6uBKQa3rDEbvD0qF97uFHihq6ZBpETgXtmdC6PHDNaLgJCMfSSWqaJRPhzEariZ5Z7QDDbU6CW0XacIrG+krPSpcprIW9Glf0EboKqOxE9cbOlwPONJz5oHx61veB3NGUqQ4lyBzxuvWsMf6dJ/roq3I+G4OInu0kpZisU4v4HsWpo/WOVsaNuqu1hst2iiQED5h1iVa3WmIwxmUtn5F2nDxbOwK2Y31HoEohmCi3TSDVut6J1Ffkg5b1yILmp4pxU4ww3etfFLJ7DqI2hUPWdzFOgNkh20rTRfE2/Hk+2UeNxm3yzl1fyfsMMuE0CiWauATyARYYQyD0RlDikL1rm97C4dqtWGafTKe8X7rU9x+qRQIfsqanZpGgOszYejlti4bizIaDZ4P/LZDCY/x0AXjUpfaPx8N/yDkffIAZRl+2IfzfJnw0eng/A4yPZed5IgSLW0f9+rtCXo+TtXsi1dDOvxUujlT5sJj8CdxZ1WH6clc88U04q8qVRml6PXVoDYPBruhYgFtW0vijahXPAmyL6x7UfQDUarbGDJ9gjmpS4OnXc8lW7cE3WSOTVRf+zAq7Z3jpQi7HBv4wqomaYf7l8C09Ge3DAq1HHlCysNw8iTFPftX0Ti2B/1ZIgUPwDQMpAHeeXCe0WTLXAuNSoXgysXErEO3UXqGe+DLJ+aXlz0KJ6egyop7jW4jeCdQJAjlRjRpmv7PDx8/rEd73g/o/PdPBq+/qv9/dmLg7Zf730/8vU6CBI7/5bXWl39Bp79+/NB4CdDo7VxEm/XR+yGCvzsV8em/POG1Tp/fjtt+P3j0dpSpc6L1/6F8SAq/b7tm/taW2evEH5jh9u16dL399n4q5Mdhlm+vo8+rTC8O/D4L/G9ukwThrwceuvJb5axeTYr1SF/gJ04XvN9G7wdGPn7wZ7BRidd+wynyW9BUq8XvZ8eAofhn5DP+4W//B9NLYbhWNAAA -->
