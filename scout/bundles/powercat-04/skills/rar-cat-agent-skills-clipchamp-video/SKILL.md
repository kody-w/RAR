---
name: "rar-cat-agent-skills-clipchamp-video"
description: "Produce a polished, narrated demo video of a live web app or Copilot Studio agent \u2014 real screen-flow footage under an AI (Ava neural) voiceover \u2014 either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clipchamp_video", "rar_sha256": "99c1a93abfecee1f36363f05c06d8b7f08c9a63e141aeb6e4f2014b6c50b4a4c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Phi-Lay Nguyen", "tags": ["video", "demo", "narration", "playwright", "ffmpeg", "copilot_studio", "clipchamp", "tts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `clipchamp_video_agent.py` and embedded as the fenced Python below (sha256 99c1a93abfecee1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `clipchamp_video_agent.py` first:

```bash
python3 clipchamp_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 clipchamp_video_agent.py   # or on stdin
python3 clipchamp_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
