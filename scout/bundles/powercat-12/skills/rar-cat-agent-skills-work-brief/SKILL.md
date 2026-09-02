---
name: "rar-cat-agent-skills-work-brief"
description: "A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_brief", "rar_sha256": "9a295dbb76bd5acabb6141ccd43ef65992dc2e63b2a0553d06d6f30fb42f24d2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "work_brief_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/work-brief:3421f6d14687e3caadd9a6aff77a0c9dd7b980c1cdb31f8de2db4c71ed6d9faf", "kind": "skill"}, "version": "1.4.0", "author": "Allan De Castro", "tags": ["productivity", "automation", "teams", "email", "calendar", "briefing", "multilingual"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/work_brief`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `work_brief_agent.py` is
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

Work Brief — A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-brief
  Upstream author: Allan De Castro
  Upstream version: 0.4.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `work_brief_agent.py` and embedded as the fenced Python below (sha256 9a295dbb76bd5aca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `work_brief_agent.py` first:

```bash
python3 work_brief_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 work_brief_agent.py   # or on stdin
python3 work_brief_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Work Brief — A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-brief
  Upstream author: Allan De Castro
  Upstream version: 0.4.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/work_brief',
    "version": '1.4.0',
    "display_name": 'Work Brief',
    "description": 'A morning brief that reads your mail, calendar, and Teams, then tells you what you owe people before the week starts.',
    "author": 'Allan De Castro',
    "tags": ['productivity', 'automation', 'teams', 'email', 'calendar', 'briefing', 'multilingual'],
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
        "upstream_slug": 'work-brief',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#work-brief',
        "upstream_version": '0.4.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '669d0b5ee44266f3',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WorkBrief(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WorkBrief'
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
    print(WorkBrief().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
