---
name: "rar-cat-agent-skills-ai-first-process-redesign"
description: "Redesign your existing processes with AI-first thinking"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_first_process_redesign", "rar_sha256": "6fcb40c0aefde81d18f04518bfc8826d717720562bf6014f8f96d11677b90bb9", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ai_first_process_redesign_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/ai-first-process-redesign:f22cf7b97a822a43dd2b6fff909f0fd28da1144a6d4dd6358c92b8a151d18ebf", "kind": "skill"}, "version": "3.1.1", "author": "Tim Sparks", "tags": ["productivity", "process_improvement", "agentic_workflow"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/ai_first_process_redesign`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ai_first_process_redesign_agent.py` is
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

AI-First Process Redesign — Redesign your existing processes with AI-first thinking

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign
  Upstream author: Tim Sparks
  Upstream version: 2.1.1
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_first_process_redesign_agent.py` and embedded as the fenced Python below (sha256 6fcb40c0aefde81d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_first_process_redesign_agent.py` first:

```bash
python3 ai_first_process_redesign_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_first_process_redesign_agent.py   # or on stdin
python3 ai_first_process_redesign_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI-First Process Redesign — Redesign your existing processes with AI-first thinking

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign
  Upstream author: Tim Sparks
  Upstream version: 2.1.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_first_process_redesign',
    "version": '3.1.1',
    "display_name": 'AI-First Process Redesign',
    "description": 'Redesign your existing processes with AI-first thinking',
    "author": 'Tim Sparks',
    "tags": ['productivity', 'process_improvement', 'agentic_workflow'],
    "category": 'general',
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
        "upstream_slug": 'ai-first-process-redesign',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign',
        "upstream_version": '2.1.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ae3bcfad1b711034',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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


class AiFirstProcessRedesign(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiFirstProcessRedesign'
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
    print(AiFirstProcessRedesign().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
