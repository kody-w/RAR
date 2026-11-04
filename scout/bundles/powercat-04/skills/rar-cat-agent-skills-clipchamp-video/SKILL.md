---
name: "rar-cat-agent-skills-clipchamp-video"
description: "Produce a polished, narrated demo video of a live web app or Copilot Studio agent \u2014 real screen-flow footage under an AI (Ava neural) voiceover \u2014 either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clipchamp_video", "rar_sha256": "d2cfd098c26b1ed16c4eb39226dc8486860550d40cd1b8f1c0c6672dc6793515", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Phi-Lay Nguyen", "tags": ["video", "demo", "narration", "playwright", "ffmpeg", "copilot_studio", "clipchamp", "tts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/clipchamp_video`. The original RAPP
agent is preserved byte-for-byte in `clipchamp_video_agent.py` and in the RCI capsule.

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

Clipchamp Narrated Demo Video — Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#clipchamp-video
  Upstream author: Phi-Lay Nguyen
  Upstream version: 1.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `clipchamp_video_agent.py` and embedded as the fenced Python below (sha256 d2cfd098c26b1ed1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `clipchamp_video_agent.py` first:

```bash
python3 clipchamp_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 clipchamp_video_agent.py   # or on stdin
python3 clipchamp_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/clipchamp_video_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/clipchamp_video_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/clipchamp_video/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Clipchamp Narrated Demo Video — Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#clipchamp-video
  Upstream author: Phi-Lay Nguyen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/clipchamp_video',
    "version": '3.0.2',
    "display_name": 'Clipchamp Narrated Demo Video',
    "description": 'Produce a polished, narrated demo video of a live web app or Copilot Studio agent — real screen-flow footage under an AI (Ava neural) voiceover — either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project.',
    "author": 'Phi-Lay Nguyen',
    "tags": ['video', 'demo', 'narration', 'playwright', 'ffmpeg', 'copilot_studio', 'clipchamp', 'tts'],
    "category": 'creative',
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
        "upstream_slug": 'clipchamp-video',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#clipchamp-video',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c2e348b1022ad7a1',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:produce'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ClipchampVideo(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ClipchampVideo'
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
    print(ClipchampVideo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
