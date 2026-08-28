---
name: "rar-cowork-cookbook-research-and-insights-alignment-recap"
description: "Surface everything that came out of this week's research sessions - what landed, what didn't, and what still needs an owner."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/research_and_insights_alignment_recap", "rar_sha256": "a272dc235647083c32bb5b5b0e5ff7a6653f2345fb2edfda47639d483c9a645d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/research_and_insights_alignment_recap`. The original RAPP
agent is preserved byte-for-byte in `research_and_insights_alignment_recap_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `research_and_insights_alignment_recap_agent.py` and embedded as the fenced Python below (sha256 a272dc235647083c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `research_and_insights_alignment_recap_agent.py` first:

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
    "version": '2.0.1',
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
