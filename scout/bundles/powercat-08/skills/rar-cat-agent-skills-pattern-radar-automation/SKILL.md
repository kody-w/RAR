---
name: "rar-cat-agent-skills-pattern-radar-automation"
description: "Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar_automation", "rar_sha256": "4a46e8a71dfa5a6e08732d289372d52fe203669fef202c3956fa38a1d6f3317a", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pattern_radar_automation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/pattern-radar-automation:7d8252af8ad3218c061a9abd321532a372ff911604147e64b29cb84c80bb121f", "kind": "skill"}, "version": "2.0.0", "author": "Srinivas Varukala", "tags": ["automation", "productivity", "teams", "email", "content", "insights"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/pattern_radar_automation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pattern_radar_automation_agent.py` is
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
