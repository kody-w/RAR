---
name: "rar-cat-agent-skills-meeting-analyzer"
description: "Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and \u2014 most importantly \u2014 hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/meeting_analyzer", "rar_sha256": "bb10c34d0d9a18bf34f0487582f49eeaaaba6c1400fa00a2abe1943c42c44f03", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Michael Ferro Pereira", "tags": ["meetings", "analysis", "insights", "personas", "transcription", "productivity", "communication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/meeting_analyzer`. The original RAPP
agent is preserved byte-for-byte in `meeting_analyzer_agent.py` and in the RCI capsule.

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
