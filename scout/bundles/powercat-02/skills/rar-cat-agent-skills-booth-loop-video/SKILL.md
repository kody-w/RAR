---
name: "rar-cat-agent-skills-booth-loop-video"
description: "Generate a silent, looping 1920x1080 MP4 for a conference booth, kiosk, or lobby screen \u2014 rendered frame-by-frame in Python (Pillow + ffmpeg), with previews before the full render."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/booth_loop_video", "rar_sha256": "575d67a2bcd525e8ebc8092fd3e0cee5e5ed253e5f72d9a6e2cda8505ca17753", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Al Macey", "tags": ["video", "animation", "python", "marketing", "events", "design", "ffmpeg"]}
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
