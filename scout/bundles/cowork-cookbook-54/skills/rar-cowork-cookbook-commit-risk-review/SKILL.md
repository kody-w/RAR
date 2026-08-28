---
name: "rar-cowork-cookbook-commit-risk-review"
description: "Know which Commit deals are at risk before quarter-end - with follow-ups drafted and CRM updated."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/commit_risk_review", "rar_sha256": "bb8db9f9005cf9b28de54a16099aea18952b9e177b398c146ed22740b93aa325", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commit_risk_review_agent.py` and embedded as the fenced Python below (sha256 bb8db9f9005cf9b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commit_risk_review_agent.py` first:

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
    "version": '2.0.0',
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
