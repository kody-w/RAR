---
name: "rar-cat-agent-skills-clipchamp-video"
description: "Produce a polished, narrated demo video of a live web app or Copilot Studio agent \u2014 real screen-flow footage under an AI (Ava neural) voiceover \u2014 either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clipchamp_video", "rar_sha256": "d2cfd098c26b1ed16c4eb39226dc8486860550d40cd1b8f1c0c6672dc6793515", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Phi-Lay Nguyen", "tags": ["video", "demo", "narration", "playwright", "ffmpeg", "copilot_studio", "clipchamp", "tts"]}
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
