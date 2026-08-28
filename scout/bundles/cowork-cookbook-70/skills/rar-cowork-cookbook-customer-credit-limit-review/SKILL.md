---
name: "rar-cowork-cookbook-customer-credit-limit-review"
description: "Builds a review report of customers whose credit limit or exposure looks out of policy."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_credit_limit_review", "rar_sha256": "6607a422fad3816166663dc62894ff2b27ce8f5a0c9ec87e13838f90edb79174", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_credit_limit_review_agent.py` and embedded as the fenced Python below (sha256 6607a422fad38161…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_credit_limit_review_agent.py` first:

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
    "version": '2.0.0',
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
