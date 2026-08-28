---
name: "rar-cat-agent-skills-cowork-use-case-one-pager"
description: "Turn a Cowork conversation, into a one-page HTML use case write-up \u2014 narrative, impact figures, workflow steps, and outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/cowork_use_case_one_pager", "rar_sha256": "04d7936c14c1ba540141659716a7bacc34a2cd3fcb057a4625d749fd89492bb7", "source_kind": "rar-agent", "source_commit": "409a3c18c6511b9cbf68a9f6716c5be9715b10c4", "version": "2.0.1", "author": "Tim Sparks", "tags": ["productivity", "use_case", "html", "documents", "writing", "audit"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/cowork_use_case_one_pager`. The original RAPP
agent is preserved byte-for-byte in `cowork_use_case_one_pager_agent.py` and in the RCI capsule.

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

Cowork Use Case One-Pager — Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager
  Upstream author: Tim Sparks
  Upstream version: 1.0.1
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `cowork_use_case_one_pager_agent.py` and embedded as the fenced Python below (sha256 04d7936c14c1ba54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `cowork_use_case_one_pager_agent.py` first:

```bash
python3 cowork_use_case_one_pager_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 cowork_use_case_one_pager_agent.py   # or on stdin
python3 cowork_use_case_one_pager_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cowork Use Case One-Pager — Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager
  Upstream author: Tim Sparks
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/cowork_use_case_one_pager',
    "version": '2.0.1',
    "display_name": 'Cowork Use Case One-Pager',
    "description": 'Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.',
    "author": 'Tim Sparks',
    "tags": ['productivity', 'use_case', 'html', 'documents', 'writing', 'audit'],
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
        "upstream_slug": 'cowork-use-case-one-pager',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e6c8d90451f0dc94',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.556, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'tag:writing', 'word:write'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CoworkUseCaseOnePager(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CoworkUseCaseOnePager'
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
    print(CoworkUseCaseOnePager().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
