---
name: "rar-cat-agent-skills-style-analyzer"
description: "Analyzes your Teams chats and emails to build a reusable profile of your writing voice \u2014 greetings, tone, length, punctuation, sign-offs, common phrases, and quirks \u2014 and saves it to memory for other assistants to use."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/style_analyzer", "rar_sha256": "529eb8528b62f6d9e5c1d80182371e91a9c7d725ddb394fb0588a2d6f7608287", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Srinivas Varukala", "tags": ["writing", "style", "teams", "email", "memory", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/style_analyzer`. The original RAPP
agent is preserved byte-for-byte in `style_analyzer_agent.py` and in the RCI capsule.

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
