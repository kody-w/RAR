---
name: "rar-cowork-cookbook-pipeline-risk-and-next-best-actions-review"
description: "Know exactly which deals need attention this week - and exactly what to do - without manually digging through CRM and email threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_risk_and_next_best_actions_review", "rar_sha256": "51ab2487dc01ba09aae099b79aa438302a57904a7b87d4cfb31a0cb958724a85", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pipeline_risk_and_next_best_actions_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/pipeline-risk-and-next-best-actions-review:738e45d510516321e42783774b5cdc62b170042a3a8e27e073e98ce1eca36f86", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/pipeline_risk_and_next_best_actions_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pipeline_risk_and_next_best_actions_review_agent.py` is
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

Pipeline risk and next-best-actions review — Know exactly which deals need attention this week - and exactly what to do - without manually digging through CRM and email threads.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/pipeline-risk-and-next-best-actions-review
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pipeline_risk_and_next_best_actions_review_agent.py` and embedded as the fenced Python below (sha256 51ab2487dc01ba09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pipeline_risk_and_next_best_actions_review_agent.py` first:

```bash
python3 pipeline_risk_and_next_best_actions_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pipeline_risk_and_next_best_actions_review_agent.py   # or on stdin
python3 pipeline_risk_and_next_best_actions_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pipeline risk and next-best-actions review — Know exactly which deals need attention this week - and exactly what to do - without manually digging through CRM and email threads.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/pipeline-risk-and-next-best-actions-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pipeline_risk_and_next_best_actions_review',
    "version": '2.0.0',
    "display_name": 'Pipeline risk and next-best-actions review',
    "description": 'Know exactly which deals need attention this week - and exactly what to do - without manually digging through CRM and email threads.',
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
        "upstream_slug": 'pipeline-risk-and-next-best-actions-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/pipeline-risk-and-next-best-actions-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b53d6af6e0c495e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/analyze-sales-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/pipeline-risk-and-next-best-actions-review', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.375, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PipelineRiskAndNextBestActionsReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PipelineRiskAndNextBestActionsReview'
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
    print(PipelineRiskAndNextBestActionsReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
