---
name: "rar-cowork-cookbook-research-and-insights-alignment-recap"
description: "Surface everything that came out of this week's research sessions - what landed, what didn't, and what still needs an owner."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/research_and_insights_alignment_recap", "rar_sha256": "4cd5174fe215d81f99321344163b4a2919a99d8b3c6d2a85b710ebf1766643d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
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
