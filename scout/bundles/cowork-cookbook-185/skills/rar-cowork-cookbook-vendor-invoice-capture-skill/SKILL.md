---
name: "rar-cowork-cookbook-vendor-invoice-capture-skill"
description: "Runs the packaged vendor-invoice-capture skill against the connected mailbox and Dynamics 365 USMF: scans unread mail for invoice PDFs, extracts fields, matches vendors, skips duplicates, creates pending vendor invoices,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_skill", "rar_sha256": "985bf2021a2e32174d9a3ec91d451597d676259608e36ddd8a41d85ff607d703", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_invoice_capture_skill`. The original RAPP
agent is preserved byte-for-byte in `vendor_invoice_capture_skill_agent.py` and in the RCI capsule.

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

Vendor Invoice Capture Skill (packaged + scored) — Runs the packaged vendor-invoice-capture skill against the connected mailbox and Dynamics 365 USMF: scans unread mail for invoice PDFs, extracts fields, matches vendors, skips duplicates, creates pending vendor invoices,

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-capture-skill
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_capture_skill_agent.py` and embedded as the fenced Python below (sha256 985bf2021a2e3217…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_capture_skill_agent.py` first:

```bash
python3 vendor_invoice_capture_skill_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_capture_skill_agent.py   # or on stdin
python3 vendor_invoice_capture_skill_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Capture Skill (packaged + scored) — Runs the packaged vendor-invoice-capture skill against the connected mailbox and Dynamics 365 USMF: scans unread mail for invoice PDFs, extracts fields, matches vendors, skips duplicates, creates pending vendor invoices,

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-capture-skill
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_capture_skill',
    "version": '3.0.3',
    "display_name": 'Vendor Invoice Capture Skill (packaged + scored)',
    "description": 'Runs the packaged vendor-invoice-capture skill against the connected mailbox and Dynamics 365 USMF: scans unread mail for invoice PDFs, extracts fields, matches vendors, skips duplicates, creates pending vendor invoices,',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'vendor-invoice-capture-skill',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-capture-skill',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf2c38b92120d435',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-05', 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/vendor-invoice-capture-skill', 'uses_skills': {'custom': ['vendor-invoice-capture'], 'ootb': ['Email', 'PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_get_entity_metadata', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}, {'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Cowork Skill Management enabled in the session', 'Prerequisite: Cowork D365 ERP plugin enabled and pointed at USMF', 'Prerequisite: PDF parsing skill enabled in the session', 'Prerequisite: Outlook plugin enabled with mailbox read access', 'Output matches: After invocation, Cowork hands off to the packaged skill, executes the full workflow against the live mailbox + USMF, and returns:\n\n- A run summary card listing emails found, records created, and skips with reasons.\n- Output artifacts in the workspace panel (extracted PDFs, generated reports).\n- A Skill Quality Report (HTML) you can open from the Output panel to confirm the 97/100 score.'], 'confidence': 1.0, 'deliverable': 'After invocation, Cowork hands off to the packaged skill, executes the full workflow against the live mailbox + USMF, and returns:\n\n- A run summary card listing emails found, records created, and skips with reasons.\n- Output artifacts in the workspace panel (extracted PDFs, generated reports).\n- A Skill Quality Report (HTML) you can open from the Output panel to confirm the 97/100 score.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Lets you ship the vendor-invoice intake workflow as a reusable Cowork skill instead of pasting a long prompt every time. The Skill Management quality report (97/100, Excellent) covers trigger clarity, instruction specificity, scope boundaries, and robustness — so AP and IT can adopt the skill knowing it passes Cowork's skill-quality gates.", 'expected_output': 'After invocation, Cowork hands off to the packaged skill, executes the full workflow against the live mailbox + USMF, and returns:\n\n- A run summary card listing emails found, records created, and skips with reasons.\n- Output artifacts in the workspace panel (extracted PDFs, generated reports).\n- A Skill Quality Report (HTML) you can open from the Output panel to confirm the 97/100 score.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Cowork Skill Management enabled in the session', 'Cowork D365 ERP plugin enabled and pointed at USMF', 'PDF parsing skill enabled in the session', 'Outlook plugin enabled with mailbox read access'], 'prompt': 'Trigger the packaged `vendor-invoice-capture` skill against the connected mailbox and Dynamics 365 (USMF). The skill encapsulates the full intake workflow: inbox scan, PDF extraction, USMF vendor match, duplicate guard, pending vendor invoice creation, and a summary report.\n\nExample trigger phrases — any of these will hand off to the skill:\n\n- capture vendor invoices from my inbox\n- process invoice emails\n- enter this invoice in D365\n- create a pending vendor invoice\n- add tax to that invoice\n\nWhen invoked the skill will:\n\n1. List unread mail with PDF attachments that look like invoices.\n2. Extract every field present on each PDF.\n3. Match the vendor against USMF vendors in D365 (by account, then by name).\n4. Skip duplicates by checking pending invoices and processed message IDs.\n5. Create a pending VendorInvoiceHeader plus VendorInvoiceLine rows for matched vendors.\n6. Return a run summary: emails found, records created, skips with reasons.\n\nIf no qualifying invoice emails are present, the skill exits with a single-line "no new vendor invoices" note.', 'steps': ['Install the `vendor-invoice-capture` skill in your Cowork environment (or import it from the cookbook repo into Skill Management).', 'Run the Cowork Skill Quality Report tool against the skill to confirm the score (expect 97/100 with the shipped definition).', 'Invoke the skill conversationally — any of the trigger phrases above will hand off to it.', '(Optional) Wire the skill into a scheduled Cowork task so it runs hourly without human prompting.', 'Inspect the run summary in the chat output and confirm the new pending invoices in USMF (Accounts payable → Vendor invoices → Pending vendor invoices).'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-05', 'what_it_does': "`vendor-invoice-capture` is a packaged Cowork skill that wraps the [Vendor Invoice Capture from Email](../vendor-invoice-capture-from-email/) workflow into a reusable trigger:\n\n- A short list of natural trigger phrases (capture vendor invoices, process invoice emails, enter this invoice in D365, create a pending vendor invoice, add tax to that invoice).\n- A scoped instruction body covering inbox scan, PDF extraction, USMF vendor match, duplicate guard, pending invoice create, and run summary.\n- A robustness story that handles the empty-inbox case quietly and skips invoices whose vendor cannot be matched in USMF.\n\nThe skill's quality scorecard:\n\n| Dimension | Score |\n| --- | --- |\n| Trigger Clarity | 24 / 25 |\n| Instruction Specificity | 25 / 25 |\n| Scope Boundaries | 24 / 25 |\n| Robustness | 24 / 25 |\n| **Total** | **97 / 100 — Excellent** |\n\nThe Trigger Coverage Analysis confirms five common phrasings (capture vendor invoices from my inbox, process invoice emails, enter this invoice in D365, create a pending vendor invoice, add tax to that invoice) all resolve to this skill."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs the packaged vendor-invoice-capture skill against the connected mailbox and Dynamics 365 USMF: scans unread mail for invoice PDFs, extracts fields, matches vendors, skips duplicates, creates pending vendor invoices,', 'example_request': 'Capture vendor invoices from my inbox and create the pending invoices in D365 USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants invoice emails processed into D365 USMF as pending vendor invoices, or asks to capture/enter an invoice from their inbox.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Install the `vendor-invoice-capture` skill in your Cowork environment (or import it from the cookbook repo into Skill Management).', 'Run the Cowork Skill Quality Report tool against the skill to confirm the score (expect 97/100 with the shipped definition).', 'Invoke the skill conversationally — any of the trigger phrases above will hand off to it.', '(Optional) Wire the skill into a scheduled Cowork task so it runs hourly without human prompting.', 'Inspect the run summary in the chat output and confirm the new pending invoices in USMF (Accounts payable → Vendor invoices → Pending vendor invoices).'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class VendorInvoiceCaptureSkill(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceCaptureSkill'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(VendorInvoiceCaptureSkill().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
