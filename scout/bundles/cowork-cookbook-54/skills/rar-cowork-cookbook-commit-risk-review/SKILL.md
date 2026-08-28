---
name: "rar-cowork-cookbook-commit-risk-review"
description: "Know which Commit deals are at risk before quarter-end - with follow-ups drafted and CRM updated."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/commit_risk_review", "rar_sha256": "4755b6a75ffe9bb85b77ae5c1f73000cdbb5d50ca0adc22ad5a66a330f10e7f9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/commit_risk_review`. The original RAPP
agent is preserved byte-for-byte in `commit_risk_review_agent.py` and in the RCI capsule.

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

Commit risk review — Know which Commit deals are at risk before quarter-end - with follow-ups drafted and CRM updated.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/commit-risk-review
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commit_risk_review_agent.py` and embedded as the fenced Python below (sha256 4755b6a75ffe9bb8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commit_risk_review_agent.py` first:

```bash
python3 commit_risk_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commit_risk_review_agent.py   # or on stdin
python3 commit_risk_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Commit risk review — Know which Commit deals are at risk before quarter-end - with follow-ups drafted and CRM updated.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/commit-risk-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/commit_risk_review',
    "version": '2.0.1',
    "display_name": 'Commit risk review',
    "description": 'Know which Commit deals are at risk before quarter-end - with follow-ups drafted and CRM updated.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'commit-risk-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/commit-risk-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0966eeb5d7645166',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/commit-risk-review', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'PowerPoint', 'Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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


class CommitRiskReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CommitRiskReview'
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
    print(CommitRiskReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
