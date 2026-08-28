---
name: "rar-cat-agent-skills-classic-text-adventure"
description: "Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/classic_text_adventure", "rar_sha256": "90b57384eee43f39e7dd44a0ba50ba226615e3b65355dcdc8f5b1f49fac559a1", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Andreas Adner", "tags": ["adventure", "game", "python"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/classic_text_adventure`. The original RAPP
agent is preserved byte-for-byte in `classic_text_adventure_agent.py` and in the RCI capsule.

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
