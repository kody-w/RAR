---
name: "rar-cowork-cookbook-commit-risk-review"
description: "Know which Commit deals are at risk before quarter-end - with follow-ups drafted and CRM updated."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/commit_risk_review", "rar_sha256": "bb8db9f9005cf9b28de54a16099aea18952b9e177b398c146ed22740b93aa325", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "commit_risk_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/commit-risk-review:227d648ae5822906eed639edf3e9989e68531f70c059dacf750c91acde72bb5b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/commit_risk_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `commit_risk_review_agent.py` is
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
