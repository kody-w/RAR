---
name: "rar-cat-agent-skills-pattern-radar"
description: "Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar", "rar_sha256": "5ab75e34a67a13fa24db57751e922a5b329554145596e626e4e324b6feb31aac", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Srinivas Varukala", "tags": ["productivity", "automation", "content", "email", "teams", "insights"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/pattern_radar`. The original RAPP
agent is preserved byte-for-byte in `pattern_radar_agent.py` and in the RCI capsule.

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

Pattern Radar — Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing — things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pattern-radar
  Upstream author: Srinivas Varukala
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pattern_radar_agent.py` and embedded as the fenced Python below (sha256 5ab75e34a67a13fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pattern_radar_agent.py` first:

```bash
python3 pattern_radar_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pattern_radar_agent.py   # or on stdin
python3 pattern_radar_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pattern Radar — Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing — things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pattern-radar
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/pattern_radar',
    "version": '2.0.0',
    "display_name": 'Pattern Radar',
    "description": 'Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing — things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates).',
    "author": 'Srinivas Varukala',
    "tags": ['productivity', 'automation', 'content', 'email', 'teams', 'insights'],
    "category": 'productivity',
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
        "upstream_slug": 'pattern-radar',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#pattern-radar',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'cde1b5f304153695',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PatternRadar(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PatternRadar'
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
    print(PatternRadar().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
