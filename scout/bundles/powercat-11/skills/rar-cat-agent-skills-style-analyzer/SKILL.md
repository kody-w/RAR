---
name: "rar-cat-agent-skills-style-analyzer"
description: "Analyzes your Teams chats and emails to build a reusable profile of your writing voice \u2014 greetings, tone, length, punctuation, sign-offs, common phrases, and quirks \u2014 and saves it to memory for other assistants to use."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/style_analyzer", "rar_sha256": "529eb8528b62f6d9e5c1d80182371e91a9c7d725ddb394fb0588a2d6f7608287", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "style_analyzer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/style-analyzer:19bdd8a06b0a8f031c1784ac2546f772f3a5e6333316def0a18eb8c5fd038ded", "kind": "skill"}, "version": "2.0.0", "author": "Srinivas Varukala", "tags": ["writing", "style", "teams", "email", "memory", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/style_analyzer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `style_analyzer_agent.py` is
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

Communication Style Analyzer — Analyzes your Teams chats and emails to build a reusable profile of your writing voice — greetings, tone, length, punctuation, sign-offs, common phrases, and quirks — and saves it to memory for other assistants to use.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#style-analyzer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `style_analyzer_agent.py` and embedded as the fenced Python below (sha256 529eb8528b62f6d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `style_analyzer_agent.py` first:

```bash
python3 style_analyzer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 style_analyzer_agent.py   # or on stdin
python3 style_analyzer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Communication Style Analyzer — Analyzes your Teams chats and emails to build a reusable profile of your writing voice — greetings, tone, length, punctuation, sign-offs, common phrases, and quirks — and saves it to memory for other assistants to use.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#style-analyzer
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/style_analyzer',
    "version": '2.0.0',
    "display_name": 'Communication Style Analyzer',
    "description": 'Analyzes your Teams chats and emails to build a reusable profile of your writing voice — greetings, tone, length, punctuation, sign-offs, common phrases, and quirks — and saves it to memory for other assistants to use.',
    "author": 'Srinivas Varukala',
    "tags": ['writing', 'style', 'teams', 'email', 'memory', 'productivity'],
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
        "upstream_slug": 'style-analyzer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#style-analyzer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e5e6f66aa29bdddf',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class StyleAnalyzer(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StyleAnalyzer'
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
    print(StyleAnalyzer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
