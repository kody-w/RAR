---
name: "rar-cowork-cookbook-pipeline-risk-and-next-best-actions-review"
description: "Know exactly which deals need attention this week - and exactly what to do - without manually digging through CRM and email threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_risk_and_next_best_actions_review", "rar_sha256": "11bcce1cb5f719fe8d1bee683f24a2b9ba1701d4f565fbe63ccd63318a886d6e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pipeline_risk_and_next_best_actions_review`. The original RAPP
agent is preserved byte-for-byte in `pipeline_risk_and_next_best_actions_review_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pipeline_risk_and_next_best_actions_review_agent.py` and embedded as the fenced Python below (sha256 11bcce1cb5f719fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pipeline_risk_and_next_best_actions_review_agent.py` first:

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
    "version": '2.0.1',
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
