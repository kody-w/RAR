---
name: "rar-cat-agent-skills-generating-podcast-script"
description: "Turn a topic or a pile of source material \u2014 a newsletter, news digest, or set of articles \u2014 into a two-host, NotebookLM-style podcast episode, with multi-voice SSML and optional Azure Text-to-Speech audio."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/generating_podcast_script", "rar_sha256": "088f3508f57592e23049713c53ec4dbbe00dba83ce2fe83bef96a6e98a3aed17", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.2", "author": "Remi Dyon", "tags": ["content", "podcast", "audio", "text_to_speech", "ssml", "news"]}
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
