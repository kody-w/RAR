---
name: "rar-cat-agent-skills-booth-loop-video"
description: "Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen \u2014 rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/booth_loop_video", "rar_sha256": "e7d0efd552cb1b7678b8324be22afc0e9e6ebee21df4fef2a23393d575f5b113", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Al Macey", "tags": ["video", "animation", "python", "marketing", "events", "design", "ffmpeg"]}
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
