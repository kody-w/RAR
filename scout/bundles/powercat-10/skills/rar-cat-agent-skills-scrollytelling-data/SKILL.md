---
name: "rar-cat-agent-skills-scrollytelling-data"
description: "Turns data into a scroll-driven HTML story."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/scrollytelling_data", "rar_sha256": "0dc2134948992af0c75f37446ddf370d42a355e9e563a6988f0de3c719d35e18", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "AndrewHessMSFT", "tags": ["data", "visualization", "storytelling", "reporting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/scrollytelling_data`. The original RAPP
agent is preserved byte-for-byte in `scrollytelling_data_agent.py` and in the RCI capsule.

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

Scrollytelling Data — Turns data into a scroll-driven HTML story.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#scrollytelling-data
  Upstream author: AndrewHessMSFT
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scrollytelling_data_agent.py` and embedded as the fenced Python below (sha256 0dc2134948992af0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scrollytelling_data_agent.py` first:

```bash
python3 scrollytelling_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scrollytelling_data_agent.py   # or on stdin
python3 scrollytelling_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrollytelling Data — Turns data into a scroll-driven HTML story.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#scrollytelling-data
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/scrollytelling_data',
    "version": '2.0.0',
    "display_name": 'Scrollytelling Data',
    "description": 'Turns data into a scroll-driven HTML story.',
    "author": 'AndrewHessMSFT',
    "tags": ['data', 'visualization', 'storytelling', 'reporting'],
    "category": 'pipeline',
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
        "upstream_slug": 'scrollytelling-data',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#scrollytelling-data',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '0b872fe30f38e4cf',
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.8, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data', 'tag:reporting'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ScrollytellingData(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScrollytellingData'
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
    print(ScrollytellingData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
