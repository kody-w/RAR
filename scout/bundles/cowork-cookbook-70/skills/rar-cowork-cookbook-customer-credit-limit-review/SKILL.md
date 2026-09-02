---
name: "rar-cowork-cookbook-customer-credit-limit-review"
description: "Builds a review report of customers whose credit limit or exposure looks out of policy."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_credit_limit_review", "rar_sha256": "6607a422fad3816166663dc62894ff2b27ce8f5a0c9ec87e13838f90edb79174", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "customer_credit_limit_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/customer-credit-limit-review:915927450dcbc2259d6b222b321615996c3e1163b36dbad93c7d5514378bfdea", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/customer_credit_limit_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `customer_credit_limit_review_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
