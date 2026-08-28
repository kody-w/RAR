---
name: "rar-cat-agent-skills-explainer-video"
description: "Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/explainer_video", "rar_sha256": "e67a73837e765ab5655949ff4d5fca1ed395181db51a69d1ea036fb3852bd6d6", "source_kind": "rar-agent", "source_commit": "657d2bb31e7d75b8fe4216443a5336cb035c07c9", "version": "2.0.0", "author": "Damien Bird", "tags": ["video", "education", "training", "communication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/explainer_video`. The original RAPP
agent is preserved byte-for-byte in `explainer_video_agent.py` and in the RCI capsule.

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

Explainer Video — Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#explainer-video
  Upstream author: Damien Bird
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `explainer_video_agent.py` and embedded as the fenced Python below (sha256 e67a73837e765ab5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `explainer_video_agent.py` first:

```bash
python3 explainer_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 explainer_video_agent.py   # or on stdin
python3 explainer_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Explainer Video — Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#explainer-video
  Upstream author: Damien Bird
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/explainer_video',
    "version": '2.0.0',
    "display_name": 'Explainer Video',
    "description": 'Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.',
    "author": 'Damien Bird',
    "tags": ['video', 'education', 'training', 'communication'],
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
        "upstream_slug": 'explainer-video',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#explainer-video',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '3922dbf6d24c64ac',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:communication'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ExplainerVideo(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ExplainerVideo'
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(ExplainerVideo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
