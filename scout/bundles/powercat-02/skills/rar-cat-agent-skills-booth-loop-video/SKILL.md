---
name: "rar-cat-agent-skills-booth-loop-video"
description: "Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen \u2014 rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/booth_loop_video", "rar_sha256": "e7d0efd552cb1b7678b8324be22afc0e9e6ebee21df4fef2a23393d575f5b113", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Al Macey", "tags": ["video", "animation", "python", "marketing", "events", "design", "ffmpeg"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/booth_loop_video`. The original RAPP
agent is preserved byte-for-byte in `booth_loop_video_agent.py` and in the RCI capsule.

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

Booth Loop Video — Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen — rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#booth-loop-video
  Upstream author: Al Macey
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `booth_loop_video_agent.py` and embedded as the fenced Python below (sha256 e7d0efd552cb1b76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `booth_loop_video_agent.py` first:

```bash
python3 booth_loop_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 booth_loop_video_agent.py   # or on stdin
python3 booth_loop_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Booth Loop Video — Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen — rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#booth-loop-video
  Upstream author: Al Macey
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/booth_loop_video',
    "version": '3.0.2',
    "display_name": 'Booth Loop Video',
    "description": 'Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen — rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render.',
    "author": 'Al Macey',
    "tags": ['video', 'animation', 'python', 'marketing', 'events', 'design', 'ffmpeg'],
    "category": 'devtools',
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
        "upstream_slug": 'booth-loop-video',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#booth-loop-video',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4be125c262ad5707',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.667, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:design'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BoothLoopVideo(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BoothLoopVideo'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(BoothLoopVideo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
