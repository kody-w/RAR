---
name: "rar-cat-agent-skills-meeting-analyzer"
description: "Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and \u2014 most importantly \u2014 hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/meeting_analyzer", "rar_sha256": "cff073328a4f633a926aca3452f228aa971695a532761e72af7a40d99c3f14cd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Michael Ferro Pereira", "tags": ["meetings", "analysis", "insights", "personas", "transcription", "productivity", "communication"]}
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
