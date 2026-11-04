---
name: "rar-cat-agent-skills-meeting-analyzer"
description: "Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and \u2014 most importantly \u2014 hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/meeting_analyzer", "rar_sha256": "9b13ab416edb7d4f7013b1e210c393170b136d2b21efd1b02702ef7abccfc95d", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Michael Ferro Pereira", "tags": ["meetings", "analysis", "insights", "personas", "transcription", "productivity", "communication"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `meeting_analyzer_agent.py` and embedded as the fenced Python below (sha256 9b13ab416edb7d4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `meeting_analyzer_agent.py` first:

```bash
python3 meeting_analyzer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 meeting_analyzer_agent.py   # or on stdin
python3 meeting_analyzer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/meeting_analyzer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/meeting_analyzer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/meeting_analyzer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
