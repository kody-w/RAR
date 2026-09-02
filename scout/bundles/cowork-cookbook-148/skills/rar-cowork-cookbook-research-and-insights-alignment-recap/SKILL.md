---
name: "rar-cowork-cookbook-research-and-insights-alignment-recap"
description: "Surface everything that came out of this week's research sessions - what landed, what didn't, and what still needs an owner."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/research_and_insights_alignment_recap", "rar_sha256": "4cd5174fe215d81f99321344163b4a2919a99d8b3c6d2a85b710ebf1766643d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "research_and_insights_alignment_recap_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/research-and-insights-alignment-recap:759058fb3fef2bad05f7dad8c1a2296f25136e603faff956263b51e72ab422e4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/research_and_insights_alignment_recap`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `research_and_insights_alignment_recap_agent.py` is
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

Research and insights alignment recap — Surface everything that came out of this week's research sessions - what landed, what didn't, and what still needs an owner.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/research-and-insights-alignment-recap
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `research_and_insights_alignment_recap_agent.py` and embedded as the fenced Python below (sha256 4cd5174fe215d81f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `research_and_insights_alignment_recap_agent.py` first:

```bash
python3 research_and_insights_alignment_recap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 research_and_insights_alignment_recap_agent.py   # or on stdin
python3 research_and_insights_alignment_recap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Research and insights alignment recap — Surface everything that came out of this week's research sessions - what landed, what didn't, and what still needs an owner.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/research-and-insights-alignment-recap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/research_and_insights_alignment_recap',
    "version": '2.0.0',
    "display_name": 'Research and insights alignment recap',
    "description": "Surface everything that came out of this week's research sessions - what landed, what didn't, and what still needs an owner.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'beginner', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'research-and-insights-alignment-recap',
        "upstream_url": 'https://coworkcookbook.com/recipes/research-and-insights-alignment-recap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae70eb16e21980cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/perform-market-research'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/research-and-insights-alignment-recap', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 1.0, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['word:research'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ResearchAndInsightsAlignmentRecap(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ResearchAndInsightsAlignmentRecap'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(ResearchAndInsightsAlignmentRecap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
