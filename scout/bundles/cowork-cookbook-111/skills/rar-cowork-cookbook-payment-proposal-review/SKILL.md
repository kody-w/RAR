---
name: "rar-cowork-cookbook-payment-proposal-review"
description: "Reviews the current Dynamics 365 F&SCM payment proposal and returns an Excel workbook flagging vendors on hold, expiring-discount invoices missing from the proposal, duplicates, sub-$50 payments, and missing bank details"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/payment_proposal_review", "rar_sha256": "7594cc30558d66c5016c0da05e50425f6c0bcd89aabdf42d5e5d6bc4861575f4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/payment_proposal_review`. The original RAPP
agent is preserved byte-for-byte in `payment_proposal_review_agent.py` and in the RCI capsule.

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

Payment Proposal Review — Reviews the current Dynamics 365 F&SCM payment proposal and returns an Excel workbook flagging vendors on hold, expiring-discount invoices missing from the proposal, duplicates, sub-$50 payments, and missing bank details

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
  Upstream entry : https://coworkcookbook.com/recipes/payment-proposal-review
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `payment_proposal_review_agent.py` and embedded as the fenced Python below (sha256 7594cc30558d66c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `payment_proposal_review_agent.py` first:

```bash
python3 payment_proposal_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 payment_proposal_review_agent.py   # or on stdin
python3 payment_proposal_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Payment Proposal Review — Reviews the current Dynamics 365 F&SCM payment proposal and returns an Excel workbook flagging vendors on hold, expiring-discount invoices missing from the proposal, duplicates, sub-$50 payments, and missing bank details

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
  Upstream entry : https://coworkcookbook.com/recipes/payment-proposal-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/payment_proposal_review',
    "version": '3.0.3',
    "display_name": 'Payment Proposal Review',
    "description": 'Reviews the current Dynamics 365 F&SCM payment proposal and returns an Excel workbook flagging vendors on hold, expiring-discount invoices missing from the proposal, duplicates, sub-$50 payments, and missing bank details',
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
        "upstream_slug": 'payment-proposal-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/payment-proposal-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5fad29b0e055bc08',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/payment-proposal-review', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Accounts payable role', 'Output matches: Workbook with flagged proposal lines by category.'], 'confidence': 1.0, 'deliverable': 'Workbook with flagged proposal lines by category.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Stops payment-run mistakes - duplicates, blocked vendors, missed discounts - at the review stage instead of after the wire clears.', 'expected_output': 'Workbook with flagged proposal lines by category.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Accounts payable role'], 'prompt': "Read the current payment proposal lines. Flag: vendors on hold, invoices with discount expiring within 2 days that are NOT in the proposal, duplicate invoices, payments below a $50 threshold, and vendors missing bank details. Output an Excel workbook 'Payment-proposal-review-<YYYY-MM-DD>.xlsx'. Do not release the proposal.", 'steps': ['Paste the prompt.', 'Review the workbook with the AP manager before releasing the proposal in D365.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork used journal 00601 (18 lines, $40,327.96 USD paid by CHECK to Federal Tax Authority, Humongous Insurance, Idaho Department of Family Services) as a representative proposal and ran all five checks. Findings: 0 vendors on hold, 3 payments below $50 (Federal Tax Authority lines, $37.85 each), 3 vendors missing VendorBankAccount records (acceptable - method is CHECK), 3 duplicate proposal lines (lines 1/2/5 share vendor/date/amount, due 2017-01-15), 0 discount-expiring not in proposal (VendorInvoiceHeader entity is empty in USMF). Produced 'Payment-proposal-review-2026-05-23.xlsx' with a tab per flag plus the full proposal-lines detail. No proposal was released.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Sanity-checks a payment proposal before release.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reviews the current Dynamics 365 F&SCM payment proposal and returns an Excel workbook flagging vendors on hold, expiring-discount invoices missing from the proposal, duplicates, sub-$50 payments, and missing bank details', 'example_request': 'Review the current payment proposal and flag anything that needs attention before we release it.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call before releasing a payment proposal in D365 F&SCM, when an AP reviewer needs flagged proposal lines checked for accuracy.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Review the workbook with the AP manager before releasing the proposal in D365.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PaymentProposalReview(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PaymentProposalReview'
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
    print(PaymentProposalReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
