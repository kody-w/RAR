---
name: "rar-cowork-cookbook-vendor-invoice-validation"
description: "Checks open, unposted vendor invoices in Dynamics 365 F&SCM against posting rules (active vendor, posting profile, currency match, balanced tax lines, PO match) and returns an exceptions workbook plus an unsent email dra"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_validation", "rar_sha256": "90c2718b8be4405870ea9e38433327810ec84cf441cf3460fd2941c7a572df29", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
