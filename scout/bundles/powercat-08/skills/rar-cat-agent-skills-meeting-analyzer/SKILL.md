---
name: "rar-cat-agent-skills-meeting-analyzer"
description: "Analyzes meeting content pasted as text or provided as audio/video transcripts. Delivers a structured intelligence report: explicit decisions and action items, participant persona profiles, and \u2014 most importantly \u2014 hidden insights: unspoken tensions, implicit risks, unresolved topics, and signals that were not made explicit during the meeting but are critical to the context."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/meeting_analyzer", "rar_sha256": "9b13ab416edb7d4f7013b1e210c393170b136d2b21efd1b02702ef7abccfc95d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Michael Ferro Pereira", "tags": ["meetings", "analysis", "insights", "personas", "transcription", "productivity", "communication"]}
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
