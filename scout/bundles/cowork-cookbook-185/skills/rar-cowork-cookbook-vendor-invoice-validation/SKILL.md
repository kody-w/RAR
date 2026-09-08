---
name: "rar-cowork-cookbook-vendor-invoice-validation"
description: "Checks open, unposted vendor invoices in Dynamics 365 F&SCM against posting rules (active vendor, posting profile, currency match, balanced tax lines, PO match) and returns an exceptions workbook plus an unsent email dra"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_validation", "rar_sha256": "90c2718b8be4405870ea9e38433327810ec84cf441cf3460fd2941c7a572df29", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_invoice_validation`. The original RAPP
agent is preserved byte-for-byte in `vendor_invoice_validation_agent.py` and in the RCI capsule.

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

Vendor Invoice Pre-Posting Validation — Checks open, unposted vendor invoices in Dynamics 365 F&SCM against posting rules (active vendor, posting profile, currency match, balanced tax lines, PO match) and returns an exceptions workbook plus an unsent email dra

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-validation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_validation_agent.py` and embedded as the fenced Python below (sha256 90c2718b8be44058…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_validation_agent.py` first:

```bash
python3 vendor_invoice_validation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_validation_agent.py   # or on stdin
python3 vendor_invoice_validation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Pre-Posting Validation — Checks open, unposted vendor invoices in Dynamics 365 F&SCM against posting rules (active vendor, posting profile, currency match, balanced tax lines, PO match) and returns an exceptions workbook plus an unsent email dra

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
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-validation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_validation',
    "version": '3.0.3',
    "display_name": 'Vendor Invoice Pre-Posting Validation',
    "description": 'Checks open, unposted vendor invoices in Dynamics 365 F&SCM against posting rules (active vendor, posting profile, currency match, balanced tax lines, PO match) and returns an exceptions workbook plus an unsent email dra',
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
        "upstream_slug": 'vendor-invoice-validation',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-validation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '35fd08e696d59f23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/vendor-invoice-validation', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Accounts payable role', 'Output matches: Workbook of invoices that would fail to post, and an email draft to the AP team.'], 'confidence': 1.0, 'deliverable': 'Workbook of invoices that would fail to post, and an email draft to the AP team.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the back-and-forth of failed postings by surfacing posting blockers (inactive vendor, missing tax, PO mismatch) before AP releases the batch.', 'expected_output': 'Workbook of invoices that would fail to post, and an email draft to the AP team.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Accounts payable role'], 'prompt': 'List open vendor invoices not yet posted. For each: confirm vendor is active, posting profile is configured, currency matches the vendor, tax lines balance, and (when applicable) a PO match exists. Build an Excel workbook of exceptions and draft an email (do not send) to the AP team summarizing counts by exception type.', 'steps': ['Paste the prompt in Cowork.', 'Review the email draft and recipients before sending.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork ran all four plan steps and produced 'Vendor-invoice-exceptions-2026-05-23.xlsx' with three sheets (Summary, Exceptions, Methodology). USMF finding: zero open vendor invoices awaiting posting - both vendor invoice register batches (00352, 00377) are already marked posted. Cowork drafted a zero-finding AP team email (saved to Drafts, not sent) and helpfully noted that USSI has ~35 pending invoices if you want to see the validation logic exercise non-zero results.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Catches posting-blocker issues on vendor invoices before they get to the GL.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Checks open, unposted vendor invoices in Dynamics 365 F&SCM against posting rules (active vendor, posting profile, currency match, balanced tax lines, PO match) and returns an exceptions workbook plus an unsent email dra', 'example_request': 'Check our open vendor invoices for posting errors and draft an email to AP with the exception list.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Use before an AP posting run to find vendor invoices that would fail to post and hand AP a fix-list with counts by exception type.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt in Cowork.', 'Review the email draft and recipients before sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class VendorInvoiceValidation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceValidation'
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
    print(VendorInvoiceValidation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
