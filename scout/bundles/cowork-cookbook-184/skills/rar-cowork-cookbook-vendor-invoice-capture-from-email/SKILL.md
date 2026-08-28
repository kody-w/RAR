---
name: "rar-cowork-cookbook-vendor-invoice-capture-from-email"
description: "Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_from_email", "rar_sha256": "44a42080a7cacd0766b8f451e34a2475c4e2edadf971f15ec867502b0002e63e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

Vendor Invoice Capture from Email — Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_capture_from_email_agent.py` and embedded as the fenced Python below (sha256 44a42080a7cacd07…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_capture_from_email_agent.py` first:

```bash
python3 vendor_invoice_capture_from_email_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_capture_from_email_agent.py   # or on stdin
python3 vendor_invoice_capture_from_email_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Capture from Email — Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'Vendor Invoice Capture from Email',
    "description": 'Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'edf03ca890a66aed',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class VendorInvoiceCaptureFromEmail(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceCaptureFromEmail'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
