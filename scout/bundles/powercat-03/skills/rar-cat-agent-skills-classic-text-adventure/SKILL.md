---
name: "rar-cat-agent-skills-classic-text-adventure"
description: "Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/classic_text_adventure", "rar_sha256": "90b57384eee43f39e7dd44a0ba50ba226615e3b65355dcdc8f5b1f49fac559a1", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "classic_text_adventure_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/classic-text-adventure:7d10670a901cf58f8d1172d38431ca4144b3bd4af0df55f097b889170d11775e", "kind": "skill"}, "version": "1.1.0", "author": "Andreas Adner", "tags": ["adventure", "game", "python"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/classic_text_adventure`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `classic_text_adventure_agent.py` is
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

Classic Text Adventure — Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#classic-text-adventure
  Upstream author: Andreas Adner
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `classic_text_adventure_agent.py` and embedded as the fenced Python below (sha256 90b57384eee43f39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `classic_text_adventure_agent.py` first:

```bash
python3 classic_text_adventure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 classic_text_adventure_agent.py   # or on stdin
python3 classic_text_adventure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Classic Text Adventure — Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#classic-text-adventure
  Upstream author: Andreas Adner
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/classic_text_adventure',
    "version": '1.1.0',
    "display_name": 'Classic Text Adventure',
    "description": 'Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics.',
    "author": 'Andreas Adner',
    "tags": ['adventure', 'game', 'python'],
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
        "upstream_slug": 'classic-text-adventure',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#classic-text-adventure',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '9a6d89774728370c',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class ClassicTextAdventure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ClassicTextAdventure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(ClassicTextAdventure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
