---
name: "rar-cowork-cookbook-vendor-invoice-capture-skill"
description: "Runs the packaged vendor-invoice-capture skill against the connected mailbox and Dynamics 365 USMF: scans unread mail for invoice PDFs, extracts fields, matches vendors, skips duplicates, creates pending vendor invoices,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_skill", "rar_sha256": "985bf2021a2e32174d9a3ec91d451597d676259608e36ddd8a41d85ff607d703", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
