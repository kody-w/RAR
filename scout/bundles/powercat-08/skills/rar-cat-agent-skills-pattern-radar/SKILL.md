---
name: "rar-cat-agent-skills-pattern-radar"
description: "Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar", "rar_sha256": "5ab75e34a67a13fa24db57751e922a5b329554145596e626e4e324b6feb31aac", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pattern_radar_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/pattern-radar:445e91fd54a6e07515eb790232bbd3e67c034a8576c769f1003d11fc40c8e998", "kind": "skill"}, "version": "2.0.0", "author": "Srinivas Varukala", "tags": ["productivity", "automation", "content", "email", "teams", "insights"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/pattern_radar`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pattern_radar_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
