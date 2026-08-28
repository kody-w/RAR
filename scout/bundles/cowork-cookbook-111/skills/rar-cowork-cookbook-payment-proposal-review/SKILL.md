---
name: "rar-cowork-cookbook-payment-proposal-review"
description: "Reviews the current payment proposal for accuracy and flags lines that need attention before release."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/payment_proposal_review", "rar_sha256": "3516253ef9d600a853cab068bc87554a5ad1d20033effabe0b6bd35ce3cca7bd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
