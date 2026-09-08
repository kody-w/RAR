---
name: "rar-cat-agent-skills-generating-podcast-script"
description: "Turn a topic or a pile of source material \u2014 a newsletter, news digest, or set of articles \u2014 into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/generating_podcast_script", "rar_sha256": "7829c0c907532eeddf7c64df1787e7755bd40cf1c3ef745e991f4de682414a4d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.2", "author": "Remi Dyon", "tags": ["content", "podcast", "audio", "text_to_speech", "ssml", "news"]}
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
