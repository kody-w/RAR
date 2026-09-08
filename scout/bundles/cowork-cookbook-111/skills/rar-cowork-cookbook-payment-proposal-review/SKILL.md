---
name: "rar-cowork-cookbook-payment-proposal-review"
description: "Reviews the current Dynamics 365 F&SCM payment proposal and returns an Excel workbook flagging vendors on hold, expiring-discount invoices missing from the proposal, duplicates, sub-$50 payments, and missing bank details"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/payment_proposal_review", "rar_sha256": "7594cc30558d66c5016c0da05e50425f6c0bcd89aabdf42d5e5d6bc4861575f4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916Z5PbSLblX+HW29jufpQE7/RiIhY0IEAYggABEGxNqOG9IQxhevu/b6JYJXXP9My8idhPS4WKMJnX5b3n3Izkry9O38VV8/L5RQ+ccnVw8jyJg2bllP5qWw1Vk4GvKnPB/5VXlV2TuH1XNe3Lhxc/aL0mqbukKsF0LXgkwdCuujhYeX3TBGW32k2lUyReu8JIYsX9L30rr2pnKpZXdVPVVevkr4qaoOubsgXXq/3oBflq0fuqMsydKErKaPUISh+oXVXlKq5y/8MqGOukAW8++knrVT0QmZSPKvGCdlUkbbvMCZuqeLXnXdmHld/XeeI5XdB+WLW9+/F/EvC7SeDJYsv7ZNcps5UfdE6SL84Go1PUedC+fP75rx9eEnD98vnXFy93WvDoRX2KUN/0PGMBZuVOGYHX9QRiXIL7OmjCqinAIz8IV293P7ZBHn5Y/ed/ZoPTRO1Pn7+Uq7fPl5fln9aXr250ldN2gb/ynNpxkzzppk8rNh+cqf0ewVXbLVH59Jz5XVJVr/6yvPvxqeRTFHQ/fnmpgAnOsoBfXn5aVQ3Q1/TL9adFSv3jT5/yagiaH3/6LgcELQ28bhEGrP709e3+TSwY+H1oEq6+6up++6arCbykDoDw3/m3fJ6mv4l7C8nX5+Afq/rD6s8lL/78Bdj7TEIXyP1zsSAGYObLp7RKyh/fdDQVyCan9IIff/pHYr048LI8abv/ltyfn4LjwPFBtN5C8tOH1+X762r95ts3mf9YbQ0S5t/xBAx/V/ctUP9I9uvK/o3oPClBvbyv5Z+K+7MJ67+sfv6Hvv2zCR9W4ZeXXZAnD5B3bh58Xv36miI//+B/f/jDX38Dov+lGL3qG+9VwtfCKZMwaLuvX3/+oX19/MNff/6hr0EWB07xtW/yP5P5Z3F91fOHCL6N+vGPc4F+o8zKaihX32po9WtV/4/mt08r08kT//vz9vPq95W4fNarxYl3pc8Q/K4aW2Dr7+L408tvAHJK4E3vvb4G+PEf/7GSE6+p2irsVjoAwG4FFrhLimAx/hIn7Sp5gnETgLi2CQjs2ziQ/8sKLxZX4eqX/+29wvxH7w3moTc8/PqOmqAYFzj75dPqAsRVTQIAGQC3xqrql9KJFjQHquomaIPmAeDJnbrgI6jij8sFQOXVL/9A4tfXyZ/q6ZdX5E2eKKdthQXh2j4PPi2+WHFQvlnuAYIIxsDrgdy88oARYZIvUA50V/kDIOTid5sleb7yE4AhgKmmJ8P05edF2C+//OI6bfylfEIytnpSWAuBAd/MWX38CLwJ8ySKuy9l4MXV6odff/th9X9W/2zWq/BFhwo44S3ywMKjflJWoJL6V45ZLcsIYOI18r/+9hZTIKYEnAvWKQmT4DkZZGIW+O8B1nn2I0qQKzcAgQVBLeqq6RaaSrpPKyFcfbMXKF1eLUwQV20HGKwGzBmU3gSkOsCdb5Esq27VgnRrw+nDqm+DV62/uI3zamIBStrpflnJWxXwTpWDP4uZT3p3yqoELJp/W/7ncyCk+aFdbd5FfFopS+4Bgm2cOm6cNx2h81wXwDfv04FwZ1UGw5dyYdZgCdVrITzDAwaByHhvS/pxWXPQixSg6v32XffrGGdhx8srSzZfyvYtyZ1mWQoPgD5QGvWJv0D/f72lVBtXfe6/xg9Yukh6WwX/bVU+PZf02bW8E/zqyfCrLz0KI/jq/+feZ3GfPRy0/YG97HervXLR7OeyLO3g4s6zgwTdyArk5rMEv3co7yj0DsZfyjwBOdZM//Uc+bqYb2OeANc3IPYaq73KB5kElmWR+5roS+I2zVIizpfyHfWB7atXiAPxAagAqmZJ1neFy9t3S2NQ+sv99w7gNTEaf/EeJPOq7l0QolUYBL7reBmwqlmK9W2ZQdYHS+EOceLFf/BqBaSD5ALyl0VKQPkBZvj0DYmfb99N/8PEZ6OzTHltAntQq82rAGBHsBi4rMuQdACynO7ZfQM/P78vbVF3i+8uqBbg6fNh0AT3PmmT14V+xjWoARh/XL6fni5PQRKBAgHBAmVQ9yC6r4WzLH8B2hhgw5IBQVMkJaB1EJS3ILwKdIoFBQDKvmXvU+Lr4zeHgtdqW/jofeLiyDJnofhnejrl9HuwuPxZmgB5xTLiVe/fZto3bYvsBTBbUCBA4/vbZy/w6Unnz35h9S73899tb37893ZArwRt/DEBPq/irqvbzxD0JNV3Tv0E4Ap62tq+8+vH98r8+GTDP4h7evp59e+Z9AcRbyXxeYV8gj/ByyvpLaXePiAC248b+yO+vP1SasF3DAXqqwLk1LJeEyD0b4T3PgSwXtQE0TL4SYDtwpsDoOpXxAfB/1L+PseXGgOEUkav4FP9rvZfmR/k+3OtvhETeFV2QLe/dIVR8GnZTC3mt8HL57LP8w8vAF6Df7L1WkinWBK4XTZqS6wDwJjB690rHozdcvnHTezp9cLJP612T/T7fZK9UcVClb+rhadzwCkPaAAgu+DrQm3AuUX5UkdOCxIT5OTiRDfVi9XPXdrS131r+v7eGgsw8AJlfvV5IaMPbwUPvkGj/mH1recGWt92QYuGoOzBBvPnpd9fwvA6ZbkAc8DXt0nfNvBu8PLXv7MLGPaKIgCLF1nfjfw+tHrdJywuANHdc1v76wsIuQNi4LwF/a3RBMNB0X1cyKqDQD4C5eD+mTng3X+3BX2b1sYO6IXAPIpgcM/DYIKgfZL0CBghPdh3YCIgYBwlQnDnej7NOI7rhzjqg+c+6Xo4TSIERYQ4kPdMu69LO5EsphAMFcIMg4Y4gsI+2KWjuO/TJA2kUyjsMK5DuATjuN+nZknpv/n39GcJ3rdueInDm5u/vrgkDkbyeCuwz88WYhAXsih3kq7QFabHfEL7mgOA51wCTK+V1iZ9inWw6Xwb+6rnRDJKvUQbLzfO28U5L7MzLIT3fXiTqBPqFyJPHf382MK+PdhC4Z2uahGq82nEB2YeezoHQKFHzahk69mUO/vByaFQGh30OGAPplet+OwebWGa0dJb66SGTukZb7PrcS3lEIjuQ3Nux9ue2KfCUXNIUc5oWK3aKz/IZrJu4QdyL8ibaY9XkUlrEVmLW12WUUTfnEY9UAahu/CS3Iy3uD6csljKhEnfoZkhblE08234RliltXZ56WJr9q3kDJ2Vat3f5vSjbuD1iTc6/NxM+GT0t6uQn7mLKDLWZgCqMQohaA9q1qOb43TgMv3IMPSNQgvd5lzDsUbdVSpUKM2iOHG63LF1ebxpl0tLR0LtjXCm9wTvXTS5Dgnqnt16oU4I+xadNznLbSuDgqlQvma3o16Xbc7HCeJx25NPxHtMHEy7gI2mZstxp0rFSTi2+M7Bhx5OGiJIOhyTU8Z21ueRPNfwsN34e97RKH2OfPya4DHvcrqYzyLOVnRkSAKZYbom5PDRwTHD3dTUPmC9Bk/Ru+7d5W1I0udwp1AXqh2oEVPSQ+6c5My4mNLkJDvhaHrUBSRAgmSRiyCH8eAlySQquWVtdzIZqq7pnus6mBJpw9HILid7b4JjrkHo+HLz1dzNaiiwH/BecNIoOm510BiKE28wZGlsnJwWYTWJKb2nC9TQ+MijT+StUMYtPoun0s1O97uPikMlU+ezbaTTcS2GoxdlSjth4m0bBATC1gelcvZo7W6suHPO7AN1AWQnRsIb4TG37dneXTHz7ud8kgrXKpKgJPKQW4brdFHTWw8pU4s0+C3m0puwE/gosY7U9pgp25E8KYOrqLOHqPHJrdoUpk5RhQvFBuzmeDJ0BVm8qw2vKOW5O3m0czyl1jwRJa4I7p0TZ2SmzynERNBYt5ClnSaVSQEmXIiUUUM8uEalWTXr4znb0ztQJXahHYDpgXkit1u1zYSw1/fSsF/3SHq2+SHLocPAH+lNI+3rLc+clSIfalSOszlMdCSdvC5TD6553oN80bsN6zSEsNVxT5tEND5F9HBCorY80A+uF2/9pjwf08F3D6yLZSMOlm4SXWWONwi1h+TAEh+D/0gQwwsN0lNr+8TB7Y4lD0pNmGUFM+cyY+gzs6E2ResPHa/AO5KjFRO+4XmnQd48DtbsWDr1YBSlQ+ihJ5A6Zk72pLfC2aQ0m0y1soxjebweb7Z1yJWglVFlB8/TPghvm/wAyZyNiEeBQ7cen52Pw80TBXSWQhPaFVvsBm/rmNWN1jziCkHY7r6VyfkawCVz95KuD3W4HF2O2ycPT+7x3MrOjR/Abng9FZyeUuemd0zb0s7cY9AEGyQUsr5AGt7VNr7FET3gAR+1CewW13k0xx7liv0+nJr1Ngu29tq4ddwI20PuUVNGHbtZ3nf9lgPvrDpVGIZUOed2WXPasPHFzLw7hCTK+FGSxdZ9bDuS4uXIncfYUuikywZVxQInK9aYbx3HA3NoXM/zI5+Yp/Z2kRmBbum64jD2wDBZrarnNsyL3vbPJzU4hd7DP0MHBhG76Izu/Ct83mBEdzzxQ9+HzBDngbmmLBXOtfPsOSexP7Aygh1LnbyyCerxdlE+6KoVIpu0MXlnpJKxFZFKGneIKp5aG2yTvPjAqI0ZAPXOzhkN7XjMNJ43lAd8U6STvo0k2JjK3D4aiTGWltbtuY1AEtvIaOXY1zjK2bD7JA1Q8oIeCF2LmnYQI+vAYwWhbS8Jh+XOA+eTHZuc7Tvf3YyH7N6J29G841zpDF2poZ6CaDTAQY3Q9qUI35igdBHcgw5bY2teDR7ee0rH8LmVGF6iApbpT6NGXrZrI76MEw6hoSLuuq6w+UtwjqK5vk3hbgQszpOPNLttMi9Erx1YzkmMdkWh0VKXsCyHahIfEf21rW0Rl1RHssQoFXq/VW4c2qV3sZjmwcKHOuVHfA0VGzK8bGio0ni3vW+GlmR9RI4LWtkK8dzRZSSGNX5RNw+7ZpN54tjKN9rzEOzYDk6KGGoGNK6Ooj9ERt5u8DqVIlxM64NuFapi2rAscOxJTLYJhF4BzU1Cd2edeCKNwTpgjXk90ZF42Bbjg0JM7cKPp1SRhV0Fr9HzGbdtu+okomZ2D6Zw9jSVzyZ74OVYMI67iE33sSaz9WnHaikWSnRpJ1TCanuThkYo1ArhJKZXfBPTEXcF4OxcVKri0+Yc1/naS9JtcqktBrmeNEMH8dN1aD9NpTHurM1urHJIyjk1OwqFKDGewfXWeTNnWVRuUs6e9ww1BBSqxXZs4rdNzN+4TURs11rWJLTVZ2UgmsnBum02nbQbHU/oj5lhjzQjiiyaKyMosKuA7TfeVLAHx+1b7HpXTKHfxBDOa86QbxJX3GEBQiLS0Tuomirs/YOloDNyGTWRDZkk5s6otp1tFMvdCe9nsDDaDkaum8BRU8TdCKj36Owdy8JaqSq2Zem+2Yi2I3R54XBrgVAv9/w4yNx6kIwHTO3k/PaAeyHntwqdBUGl3RLd8LT1cJ+3ObLtxoO4YWOeALEzmvGyPaKitN4DHPRJtdZoB+9k4aiqcA099It3Zpnx4Mqtm7Y8FBp1IoTnYlf11+Y+X7yLs1YtmZXkecBQyOXu7qbicdETkcuj8e5NsrvctVaoWOfKjX57vRFBcAgopYSlY/rg6uK+TRyH3Ni7MhujrQL6hFgy8zirEro4HzdkgrDlTIln2WhdM3sI2bBrZbc+kQ7ORCf3sWMi6R5vD23lFbdhJ2r9EXcsD4szPOR6aWxOayO6nLfqAMu3yD5J5lnURyOJR+sC65CM7N1YVwFolPhgGqV6NCVumxT3Ik6m/ni8DEQYnm0kkLN71ei2tbd7TeK40TzzckKkB4I55Wt2NibiUSNwalqptbtuu/p4lHfCHBXVpulI67ipS5nw7aTFi8Moj9hVKY/oJiyPbXFnptPZOV6EIuJb033s6xOgBvY4xHtRimqS3dQHYZgrhDGL7NEBXL8xEaoXSp6aSO7nbEUdE+h+J0nhJOuja2g3rkA7szPQ6XZvbttrwXOOo+4tplkXIhwckdnH3b45WBntKtIwk4iScVlKkKdTep6P+sm6y4IBdezxvEWF3KNR3UdKfyg0pCSRDcD5Pb6nKpvCLCObLAT1XKYcH8d66GzqgaANcrnv1HnLNYBLRzfNQ04hGQcJ9F7vQz45HFRbiyj3tmXtVncphrg4u+5cc75xRCwtjdlLzfgsT4IMMtf1HFaGOiKXULdoiRyuPtbKTcdrlxwtQijSVEa9NmRYEhgEqzTYq4y7U8Yd27i5srtGu8syWStJyGxKWsiLR6cDU1xnO58uZhuHV9iskzY9C7W0l243K3owtinYvX/u6IMZ9U3JtqW3GbTQ6K+YqHS7NAYQQppl0t49xfVi4ZJs+U34mM1Zx1OiVsKZXgcSojO0ItJ5GWYiuZmH80j7Ib+j9Qr2w4Pd2wkHQVSZToR6uEL9GhrEcXa2TSLyV5Sy+xki1ROzb032fkxok1hzYtAPc6ZhhOsqXFHWmvPY51iBsCcgK4gxUWP5w0YfApvfYcNxDTtsb+6IDSVw+cEx7F43mkMrs2HMGGCLs681OfVb83HZx5ErdkfhnEU+xF9DhYFTe5DvjCatQ7OrGZq8Mshwv0YFm8BNwFDQA/eUImVmWMy4RJlgcYxMYiLZfYmIRiE7AcxUguELkFrCPp9WoxIneTJLuQn2CHHv6PwksJaiPuopeIzVuo/2R4FucmK0pCxHXeUotrQkeOosrpUJY9mzXWUFklxa7sBQ2mYnKq2x7gqKle1NxEOW/zDApsmVCmnDR7WcNjlI38jUCcXhChPmYm7o58tJpB/YXaOU+zr3e/zatp1J3ALE8yRNcnN+L/o5eaAb/QBbt/ocScROi/UsJcPNVmggtzjbGsgKnt2067s5nM+ztalvvqdtDztpLyMXV9Ev8PqAWG0iz2fu1hkTH1LXDh7qs1x33L3lNH3MGU7aPfDTJs6SCfQ5mQZzqesduSrW6A2R1YV+QW+KOV6tYn9pRxkaZbxBECJxwWwXE6vAjjvzsHEfl3W62aYR1TJ+sdMQNC7t8n42WPWMMhEjKY8hSHbrFjfqbBR22/OGGTzCznDKOnOJO/EcqSggwTvXOKgqxJj7Q/Ggj6iHJ3nWNpdavncZeY9bO8zJsanFo3GvC3KqxP0JHgZJoFDkZnfVZVaHebzAe/RutElQVzmzo26mqXZ02h3dO2PeW6z2lX7MnV2Em6LrK0KF+1CsG7cBvlLhyegrXj2GSg6p6Cw7o150CWUiFF+Eo3/c1gcUa8gUM/VSt3JJCB5Gjm22eUDY1xrt/CY6EwPkiAjrGHB3x+dY31Jafi0YlZ/Z9X4nV/BQmoeHL0mPSZTwwk7ujMzr3YMdt1ewy07XmHO4z4HSpgbfsfuHEOuSten6211GIQyAbbI+pK0yzbcD11zk1tuhOEaMDATF+Xo0rtxBSM0QmpS1gxGN4bmoJZL9zaUsJaTzRsr1UtBldddaB3vHJ3s6vBx6RSU5eNuM1hW3JV2NpnxnTyMPyzzOZ4U8azRtr8mL7Kba41LV1u0U9BW612Iac89BF7E1i5QGdgvzh+x4+HQfjzExUFQM6dxxtLG6py6RjxHSphKHRhagoEcQkyDdcc/SD/y6o6WLe8pUqx+Y4wGwEcGV6n6vUvVhTZ2d24zLSOleea09hKomWmnTaxWkRzWirxuekpUreoOFtNje9luRkPmdSyGjhd2KcI/IG1ZTmtAQJlxDJqFiWkZEkFCkReQ8z/eSheOH0RXKQXn4qfnIuvzBC4MMydQxwziKNvOpU5PNo02O5t535VzWaK9QSesSQVs59yJ4dzqQhoU9miQ2ZVVPvenG5TLv88edV2hKdJH187HDTaUd/FbE+GrIdgVabomBga0yfzhGO9RHkqnDaa2mo81A2Hz2ttB0vZ8YuZ6VOSClvXGN6LHUObtxpKgSVELSqMI1lRjq2xNhHLnTuhjwac0YiIrAF9g00Ivh815N9ELR8sLJSYhCK5s58OHqDqvzpRIvm3n7uHXHaKak8nqVfeVgTjARYc3Bq+Ndku5IeMMU0ZWi7c52DXOtsm2dmiNxwzqKAd9YbDnWHLLn23wtHo6jMF2jgzpuNkr+CBL0BrkKaE9l7kzVFov3xWAHD2sa6cFnOe6uQ1e7kW6pxe6ICmIuh8RKkzbGVSnlDfcOitjak3dFyVtYVCiW9yeqYpTkhjRzrjh9gej0AduVYBPp6VLYDjPVXVBipHxQm3J4Ij2i0CmE0zircGRMz6dUk8vyWKC+RvkBwmL8mppzwiM4+4F5YrZrmrB+eGDfcpvJUPSzPdibWXuxYTnVIDGUcUUmAXVumtj+rogIGnGKtvck1fLmjLkzI3NTRlsh8t0jgsJzRM3CmSM1T+vsS83X8UNDRkxn7TzMjZSq1FlP11AobEV0c5G1SXdhvILTASPx4xD22U2sLuNmFrk8baC7rcdTPIH2uGMOm5IX70wCh3qgno7sWpJbJMJP6tSimG5NJIyKHQaomoXvKC2nMV3SNVWID9e9ooZMscfKPc/KeJm22T12pn7YQ76ERhv0ROFeIgP4nDmeoANUwfwEcpREhKYko61D7vYwIDFKZ3jx0lqTug1vD11X+aIrCNfxHOIhXfW6Qgmr9x6JaYoDuu0CJC0mCaeVRj1UUnNMZZ/ZTjLPQLVcQKqxpYhcC25kyjS6psxZDj0uSqwdlFvmXXim6S16pj1YPUooYzeHTIVp1rRqQmebwGNUASWNnLnQgG/udW084tM1Lyex8AXG0UaSaEOnQ0al6GusOxP1vHbxjVOlCn0nHB5T+rJ2d+MVORZNns/ng36wtqhGZefTWtC1s4MooQqtTQZXEZYsIDqIwBYJq3jp5uw0rMuR8N4ZwwPrifwa3Bt0uEe0f0WuUtc9el8n6mINNg9rvOp1zx6VoLHnZjPMXnRWHEmqrhZyuK5rZp0Wc/WwIXmbWVAQERdDhTS6WG+Qo5215UYqgtY/IE2E0/DJJSk2730t2fExO0xblNru9S1zJo8VT7C+67G4slWGUO5Rt/Efuyt0SVVxfZpYCdeR9aZRdwe/69Ytx+yVo0ZhnKEalRohBoWUcUn2FTU5a7qlsA5TUdMKmanFmXXRerMClRMDuWd6uK9nD9Tf7FEINggHfL3Z7TqCO1Bd1vf75H663x2k3xczRBfxiSK8lqdPKvooTg/zjkQ1rTIJgGq/V0hKgdy9TA/NyDOnoXsU9gXsF2miOx0KR23xJnAwdH0S0AcJGgL/FjUzv9+WqE3sI42lvHvp13UkJtttTVYC3atwkeEqn88GEh76TLtNeJr2lzBvNwe4qCXT8NXdUPFDlDgjTyDEFENismuw9VgMFzx0mR6iuKCRzmdsnGcqNaWAzINLUmF7vrYF7NoT4eaq86DCI+xBKFvTO8MCydYx7s5ujs2tmlIUzqksJvBpL8EuVp45FJ702JbAvnU9k5oG0TyK8qEN4Bu6NSOsqjHkyPdNxLUMy7J/efnwspz0vZ3X/avfAi0HK//PzneeRzHvh/2vp2KB439+1fX5X1ry1w8vjZcAO54nVm3eR28HPX9zXvXxHxzpLpOm549p3k8cn2eXnRMtvyR9SUq/b7tm+tpW+evBPpjh9u3yI7R2scsD378/xHN6P+m+Hz111Veg+WX5cdhyUh/4idMFb7fR24Hdhxf/7ZcoXzGS+Bo09eLX2+EwcAf7BH/CXn77v6O07+AJLAAA -->
