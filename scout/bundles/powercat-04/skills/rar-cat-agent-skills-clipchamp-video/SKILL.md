---
name: "rar-cat-agent-skills-clipchamp-video"
description: "Produce a polished, narrated demo video of a live web app or Copilot Studio agent \u2014 real screen-flow footage under an AI (Ava neural) voiceover \u2014 either fully headless (ffmpeg + edge-tts) or assembled in the Clipchamp web UI as an editable project."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/clipchamp_video", "rar_sha256": "99c1a93abfecee1f36363f05c06d8b7f08c9a63e141aeb6e4f2014b6c50b4a4c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Phi-Lay Nguyen", "tags": ["video", "demo", "narration", "playwright", "ffmpeg", "copilot_studio", "clipchamp", "tts"]}
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
