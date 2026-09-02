---
name: "rar-cat-agent-skills-meeting-analyzer"
description: "Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and \u2014 most importantly \u2014 hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/meeting_analyzer", "rar_sha256": "bb10c34d0d9a18bf34f0487582f49eeaaaba6c1400fa00a2abe1943c42c44f03", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "meeting_analyzer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/meeting-analyzer:037420bce5ca0d9ea892b3c96997bfa90f9e06490dab2dba62eecd96584442ed", "kind": "skill"}, "version": "1.1.0", "author": "Michael Ferro Pereira", "tags": ["meetings", "analysis", "insights", "personas", "transcription", "productivity", "communication"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/meeting_analyzer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `meeting_analyzer_agent.py` is
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

Meeting Analyzer — Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and — most importantly — hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#meeting-analyzer
  Upstream author: Michael Ferro Pereira
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `meeting_analyzer_agent.py` and embedded as the fenced Python below (sha256 bb10c34d0d9a18bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `meeting_analyzer_agent.py` first:

```bash
python3 meeting_analyzer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 meeting_analyzer_agent.py   # or on stdin
python3 meeting_analyzer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Meeting Analyzer — Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and — most importantly — hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#meeting-analyzer
  Upstream author: Michael Ferro Pereira
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/meeting_analyzer',
    "version": '1.1.0',
    "display_name": 'Meeting Analyzer',
    "description": 'Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and — most importantly — hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context.',
    "author": 'Michael Ferro Pereira',
    "tags": ['meetings', 'analysis', 'insights', 'personas', 'transcription', 'productivity', 'communication'],
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
        "upstream_slug": 'meeting-analyzer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#meeting-analyzer',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '71c742aa9f713491',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.667, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'tag:insights'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class MeetingAnalyzer(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MeetingAnalyzer'
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
    print(MeetingAnalyzer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
