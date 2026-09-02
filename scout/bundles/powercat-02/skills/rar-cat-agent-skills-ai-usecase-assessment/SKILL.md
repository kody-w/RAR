---
name: "rar-cat-agent-skills-ai-usecase-assessment"
description: "Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting \u2014 grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_usecase_assessment", "rar_sha256": "b1c7ceb11b90cd8bd781cbfab3f8c914f11830d1ae2eb360f2aa3b68152fef67", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ai_usecase_assessment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/ai-usecase-assessment:3ce5f6a18d08a85d221449278c1927dbc5a8d6fa143a39dd95cf84566f89ec0d", "kind": "skill"}, "version": "2.0.0", "author": "Alicja Gilderdale", "tags": ["assessment", "ai", "agent", "use_case", "scoring", "report", "html", "intake"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/ai_usecase_assessment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ai_usecase_assessment_agent.py` is
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
