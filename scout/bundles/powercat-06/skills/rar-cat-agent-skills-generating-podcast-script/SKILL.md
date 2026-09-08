---
name: "rar-cat-agent-skills-generating-podcast-script"
description: "Turn a topic or a pile of source material \u2014 a newsletter, news digest, or set of articles \u2014 into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/generating_podcast_script", "rar_sha256": "7829c0c907532eeddf7c64df1787e7755bd40cf1c3ef745e991f4de682414a4d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.1.2", "author": "Remi Dyon", "tags": ["content", "podcast", "audio", "text_to_speech", "ssml", "news"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/generating_podcast_script`. The original RAPP
agent is preserved byte-for-byte in `generating_podcast_script_agent.py` and in the RCI capsule.

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

Podcast Script Generator — Turn a topic or a pile of source material — a newsletter, news digest, or set of articles — into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#generating-podcast-script
  Upstream author: Remi Dyon
  Upstream version: 1.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `generating_podcast_script_agent.py` and embedded as the fenced Python below (sha256 7829c0c907532eed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `generating_podcast_script_agent.py` first:

```bash
python3 generating_podcast_script_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 generating_podcast_script_agent.py   # or on stdin
python3 generating_podcast_script_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Podcast Script Generator — Turn a topic or a pile of source material — a newsletter, news digest, or set of articles — into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#generating-podcast-script
  Upstream author: Remi Dyon
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/generating_podcast_script',
    "version": '3.1.2',
    "display_name": 'Podcast Script Generator',
    "description": 'Turn a topic or a pile of source material — a newsletter, news digest, or set of articles — into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio.',
    "author": 'Remi Dyon',
    "tags": ['content', 'podcast', 'audio', 'text_to_speech', 'ssml', 'news'],
    "category": 'general',
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
        "upstream_slug": 'generating-podcast-script',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#generating-podcast-script',
        "upstream_version": '1.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b619697cd53a907a',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.667, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class GeneratingPodcastScript(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GeneratingPodcastScript'
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
    print(GeneratingPodcastScript().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
