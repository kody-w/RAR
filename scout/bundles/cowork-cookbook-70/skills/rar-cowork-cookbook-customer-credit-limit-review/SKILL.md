---
name: "rar-cowork-cookbook-customer-credit-limit-review"
description: "Produces a read-only Excel workbook of customers flagged for credit review \u2014 over 80% of limit, no limit with AR over $10,000, or a limit with no 12-month activity \u2014 one sheet per category sorted by exposure descending."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_credit_limit_review", "rar_sha256": "c713ca964e33f302d3b2114731691069d4aa42d308f0e8e3f0713d17aa951a70", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_credit_limit_review`. The original RAPP
agent is preserved byte-for-byte in `customer_credit_limit_review_agent.py` and in the RCI capsule.

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

Customer Credit Limit Review — Produces a read-only Excel workbook of customers flagged for credit review — over 80% of limit, no limit with AR over $10,000, or a limit with no 12-month activity — one sheet per category sorted by exposure descending.

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-credit-limit-review
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_credit_limit_review_agent.py` and embedded as the fenced Python below (sha256 c713ca964e33f302…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_credit_limit_review_agent.py` first:

```bash
python3 customer_credit_limit_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_credit_limit_review_agent.py   # or on stdin
python3 customer_credit_limit_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Credit Limit Review — Produces a read-only Excel workbook of customers flagged for credit review — over 80% of limit, no limit with AR over $10,000, or a limit with no 12-month activity — one sheet per category sorted by exposure descending.

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-credit-limit-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_credit_limit_review',
    "version": '3.0.3',
    "display_name": 'Customer Credit Limit Review',
    "description": 'Produces a read-only Excel workbook of customers flagged for credit review — over 80% of limit, no limit with AR over $10,000, or a limit with no 12-month activity — one sheet per category sorted by exposure descending.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'customer-credit-limit-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-credit-limit-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fbe350c4f88edb95',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/customer-credit-limit-review', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Credit/collections role', 'Output matches: Workbook with categorized customer credit issues.'], 'confidence': 1.0, 'deliverable': 'Workbook with categorized customer credit issues.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Protects DSO and reduces bad-debt write-offs by flagging customers who have drifted out of credit policy before the next big order ships.', 'expected_output': 'Workbook with categorized customer credit issues.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Credit/collections role'], 'prompt': 'Build a credit-management review: list customers whose current AR exposure is greater than 80% of their credit limit, customers with no credit limit set but with AR balance > $10,000, and customers with credit limit > $0 but no activity in 12 months. Output an Excel workbook with one sheet per category, sorted by exposure descending. Do not change limits.', 'steps': ['Paste the prompt.', 'Review the report; update limits via D365 with the credit committee.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork found that the tenant's most recent transaction is 2023-11-29 and built a 12-month window ending there. Real findings: 9 customers over 80% exposure (Sparrow Retail US-008 at 920%, Contoso Retail Chicago US-015 at 179%, Yellow Square US-024 at 173%; 5 of 9 above 150%); 0 customers with no-limit-but-balance (3 customers have $0 limit all with $0 open AR); 11 customers carrying credit lines with no activity in the 12-month window. Real workbook Credit-review-2026-05-23.xlsx with one sheet per category sorted by exposure descending plus a Notes sheet documenting methodology and the CustomersV3 / CustTransactions entities used. No credit limits modified.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Highlights credit-policy issues so the credit team can act.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Produces a read-only Excel workbook of customers flagged for credit review — over 80% of limit, no limit with AR over $10,000, or a limit with no 12-month activity — one sheet per category sorted by exposure descending.', 'example_request': 'Build a credit limit review workbook for customers over 80% exposure, no limit with AR over $10k, and inactive 12 months.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when preparing a credit committee or collections review of customer credit limits and AR exposure in Dynamics 365 F&SCM. It reports only; it never changes limits.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Review the report; update limits via D365 with the credit committee.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CustomerCreditLimitReview(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerCreditLimitReview'
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
    print(CustomerCreditLimitReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
