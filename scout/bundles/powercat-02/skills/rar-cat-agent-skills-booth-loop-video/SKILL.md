---
name: "rar-cat-agent-skills-booth-loop-video"
description: "Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen \u2014 rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/booth_loop_video", "rar_sha256": "575d67a2bcd525e8ebc8092fd3e0cee5e5ed253e5f72d9a6e2cda8505ca17753", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Al Macey", "tags": ["video", "animation", "python", "marketing", "events", "design", "ffmpeg"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `booth_loop_video_agent.py` and embedded as the fenced Python below (sha256 575d67a2bcd525e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `booth_loop_video_agent.py` first:

```bash
python3 booth_loop_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 booth_loop_video_agent.py   # or on stdin
python3 booth_loop_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/booth_loop_video_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/booth_loop_video_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/booth_loop_video/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
