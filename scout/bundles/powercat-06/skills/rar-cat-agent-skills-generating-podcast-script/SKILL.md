---
name: "rar-cat-agent-skills-generating-podcast-script"
description: "Turn a topic or a pile of source material \u2014 a newsletter, news digest, or set of articles \u2014 into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/generating_podcast_script", "rar_sha256": "088f3508f57592e23049713c53ec4dbbe00dba83ce2fe83bef96a6e98a3aed17", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.1.2", "author": "Remi Dyon", "tags": ["content", "podcast", "audio", "text_to_speech", "ssml", "news"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `generating_podcast_script_agent.py` and embedded as the fenced Python below (sha256 088f3508f57592e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `generating_podcast_script_agent.py` first:

```bash
python3 generating_podcast_script_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 generating_podcast_script_agent.py   # or on stdin
python3 generating_podcast_script_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/generating_podcast_script_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/generating_podcast_script_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/generating_podcast_script/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
