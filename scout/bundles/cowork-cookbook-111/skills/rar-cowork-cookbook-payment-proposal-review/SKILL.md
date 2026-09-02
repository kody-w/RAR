---
name: "rar-cowork-cookbook-payment-proposal-review"
description: "Reviews the current payment proposal for accuracy and flags lines that need attention before release."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/payment_proposal_review", "rar_sha256": "3516253ef9d600a853cab068bc87554a5ad1d20033effabe0b6bd35ce3cca7bd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "payment_proposal_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/payment-proposal-review:12cb58190cd4f0c33e695f9a12ac631637ca547fee98d6132a10dd36d95ba368", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/payment_proposal_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `payment_proposal_review_agent.py` is
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

Payment Proposal Review — Reviews the current payment proposal for accuracy and flags lines that need attention before release.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `payment_proposal_review_agent.py` and embedded as the fenced Python below (sha256 3516253ef9d600a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `payment_proposal_review_agent.py` first:

```bash
python3 payment_proposal_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 payment_proposal_review_agent.py   # or on stdin
python3 payment_proposal_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Payment Proposal Review — Reviews the current payment proposal for accuracy and flags lines that need attention before release.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Payment Proposal Review',
    "description": 'Reviews the current payment proposal for accuracy and flags lines that need attention before release.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd7b114adb7d66ff',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PaymentProposalReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PaymentProposalReview'
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
    print(PaymentProposalReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
