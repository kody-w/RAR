---
name: "rar-cat-agent-skills-competitive-battlecard-builder"
description: "Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/competitive_battlecard_builder", "rar_sha256": "0b7356f6516b4afaabbed99ae04111381a60d133eeba92effdad8545f2f05ddd", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Michael Heath", "tags": ["sales_enablement", "productivity", "comparison"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/competitive_battlecard_builder`. The original RAPP
agent is preserved byte-for-byte in `competitive_battlecard_builder_agent.py` and in the RCI capsule.

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

Competitive Battlecard Builder — Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder
  Upstream author: Michael Heath
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_battlecard_builder_agent.py` and embedded as the fenced Python below (sha256 0b7356f6516b4afa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_battlecard_builder_agent.py` first:

```bash
python3 competitive_battlecard_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitive_battlecard_builder_agent.py   # or on stdin
python3 competitive_battlecard_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Competitive Battlecard Builder — Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder
  Upstream author: Michael Heath
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/competitive_battlecard_builder',
    "version": '2.0.0',
    "display_name": 'Competitive Battlecard Builder',
    "description": 'Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…',
    "author": 'Michael Heath',
    "tags": ['sales_enablement', 'productivity', 'comparison'],
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
        "upstream_slug": 'competitive-battlecard-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd2d932cf8ec2e523',
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.667, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:comparison'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class CompetitiveBattlecardBuilder(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CompetitiveBattlecardBuilder'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(CompetitiveBattlecardBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
