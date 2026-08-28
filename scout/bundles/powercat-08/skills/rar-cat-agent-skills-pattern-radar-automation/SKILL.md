---
name: "rar-cat-agent-skills-pattern-radar-automation"
description: "Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar_automation", "rar_sha256": "4a46e8a71dfa5a6e08732d289372d52fe203669fef202c3956fa38a1d6f3317a", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Srinivas Varukala", "tags": ["automation", "productivity", "teams", "email", "content", "insights"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/pattern_radar_automation`. The original RAPP
agent is preserved byte-for-byte in `pattern_radar_automation_agent.py` and in the RCI capsule.

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

Pattern Radar (Scheduled) — Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing — things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pattern-radar-automation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pattern_radar_automation_agent.py` and embedded as the fenced Python below (sha256 4a46e8a71dfa5a6e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pattern_radar_automation_agent.py` first:

```bash
python3 pattern_radar_automation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pattern_radar_automation_agent.py   # or on stdin
python3 pattern_radar_automation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pattern Radar (Scheduled) — Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing — things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pattern-radar-automation
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/pattern_radar_automation',
    "version": '2.0.0',
    "display_name": 'Pattern Radar (Scheduled)',
    "description": 'Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing — things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware.',
    "author": 'Srinivas Varukala',
    "tags": ['automation', 'productivity', 'teams', 'email', 'content', 'insights'],
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
        "upstream_slug": 'pattern-radar-automation',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#pattern-radar-automation',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '137112290f4a7fbf',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.421, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PatternRadarAutomation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PatternRadarAutomation'
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
    print(PatternRadarAutomation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
