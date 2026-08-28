---
name: "rar-cowork-cookbook-pipeline-risk-and-next-best-actions-review"
description: "Know exactly which deals need attention this week - and exactly what to do - without manually digging through CRM and email threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pipeline_risk_and_next_best_actions_review", "rar_sha256": "51ab2487dc01ba09aae099b79aa438302a57904a7b87d4cfb31a0cb958724a85", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
