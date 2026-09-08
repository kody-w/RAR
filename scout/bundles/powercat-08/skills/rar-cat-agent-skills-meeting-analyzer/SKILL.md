---
name: "rar-cat-agent-skills-meeting-analyzer"
description: "Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and \u2014 most importantly \u2014 hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/meeting_analyzer", "rar_sha256": "cff073328a4f633a926aca3452f228aa971695a532761e72af7a40d99c3f14cd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Michael Ferro Pereira", "tags": ["meetings", "analysis", "insights", "personas", "transcription", "productivity", "communication"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `meeting_analyzer_agent.py` and embedded as the fenced Python below (sha256 cff073328a4f633a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `meeting_analyzer_agent.py` first:

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
    "version": '2.1.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
