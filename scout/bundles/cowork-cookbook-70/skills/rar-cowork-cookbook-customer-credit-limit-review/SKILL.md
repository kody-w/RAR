---
name: "rar-cowork-cookbook-customer-credit-limit-review"
description: "Builds a review report of customers whose credit limit or exposure looks out of policy."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_credit_limit_review", "rar_sha256": "73a04e3622c1154bb2e99baf166ae4917e928c883b66f156106418778e800e2d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

Customer Credit Limit Review — Builds a review report of customers whose credit limit or exposure looks out of policy.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_credit_limit_review_agent.py` and embedded as the fenced Python below (sha256 73a04e3622c1154b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_credit_limit_review_agent.py` first:

```bash
python3 customer_credit_limit_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_credit_limit_review_agent.py   # or on stdin
python3 customer_credit_limit_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Credit Limit Review — Builds a review report of customers whose credit limit or exposure looks out of policy.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'Customer Credit Limit Review',
    "description": 'Builds a review report of customers whose credit limit or exposure looks out of policy.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f6478ca7062e818f',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class CustomerCreditLimitReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerCreditLimitReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(CustomerCreditLimitReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
