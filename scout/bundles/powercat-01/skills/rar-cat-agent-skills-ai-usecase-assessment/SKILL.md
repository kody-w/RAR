---
name: "rar-cat-agent-skills-ai-usecase-assessment"
description: "Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting \u2014 grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_usecase_assessment", "rar_sha256": "b1c7ceb11b90cd8bd781cbfab3f8c914f11830d1ae2eb360f2aa3b68152fef67", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Alicja Gilderdale", "tags": ["assessment", "ai", "agent", "use_case", "scoring", "report", "html", "intake"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/ai_usecase_assessment`. The original RAPP
agent is preserved byte-for-byte in `ai_usecase_assessment_agent.py` and in the RCI capsule.

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

AI Use Case Assessment — Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting — grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-usecase-assessment
  Upstream author: Alicja Gilderdale
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_usecase_assessment_agent.py` and embedded as the fenced Python below (sha256 b1c7ceb11b90cd8b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_usecase_assessment_agent.py` first:

```bash
python3 ai_usecase_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_usecase_assessment_agent.py   # or on stdin
python3 ai_usecase_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI Use Case Assessment — Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting — grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-usecase-assessment
  Upstream author: Alicja Gilderdale
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_usecase_assessment',
    "version": '2.0.0',
    "display_name": 'AI Use Case Assessment',
    "description": 'Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting — grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork.',
    "author": 'Alicja Gilderdale',
    "tags": ['assessment', 'ai', 'agent', 'use_case', 'scoring', 'report', 'html', 'intake'],
    "category": 'analysis',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'ai-usecase-assessment',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-usecase-assessment',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '8d143663df287664',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout', 'Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.4, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AiUsecaseAssessment(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiUsecaseAssessment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(AiUsecaseAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
