---
name: "rar-cat-agent-skills-scrollytelling-data"
description: "Turns data into a scroll-driven HTML story."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/scrollytelling_data", "rar_sha256": "0dc2134948992af0c75f37446ddf370d42a355e9e563a6988f0de3c719d35e18", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scrollytelling_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/scrollytelling-data:e542937b87c24bc9287f82721c32eae42af529014f0062352816f0af86ca0f62", "kind": "skill"}, "version": "2.0.0", "author": "AndrewHessMSFT", "tags": ["data", "visualization", "storytelling", "reporting"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/scrollytelling_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scrollytelling_data_agent.py` is
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
