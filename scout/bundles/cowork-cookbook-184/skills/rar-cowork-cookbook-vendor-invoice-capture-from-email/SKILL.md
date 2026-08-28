---
name: "rar-cowork-cookbook-vendor-invoice-capture-from-email"
description: "Watches the inbox for emails with PDF attachments that look like vendor invoices, extracts every field from the PDF, matches the vendor against USMF master data, and creates a pending vendor invoice record in Dynamics 365 F&O with the header and lines populated."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_from_email", "rar_sha256": "74aff5e7e60d62993665b35bb9bee48629a27e4eff7d50466256a2128df6d1c7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_capture_from_email_agent.py` and embedded as the fenced Python below (sha256 74aff5e7e60d6299…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_capture_from_email_agent.py` first:

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
    "version": '2.0.0',
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
