---
name: "rar-cat-agent-skills-idea-refiner"
description: "Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/idea_refiner", "rar_sha256": "1f45a76ddaa7dca12d9857414545d29e8dc4e2ee13f87af6eb03b928acdb7bb7", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Mathias Salomonsen", "tags": ["productivity", "planning", "decision_making", "refinement", "brainstorming"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/idea_refiner`. The original RAPP
agent is preserved byte-for-byte in `idea_refiner_agent.py` and in the RCI capsule.

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

Idea Refiner — Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#idea-refiner
  Upstream author: Mathias Salomonsen
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `idea_refiner_agent.py` and embedded as the fenced Python below (sha256 1f45a76ddaa7dca1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `idea_refiner_agent.py` first:

```bash
python3 idea_refiner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 idea_refiner_agent.py   # or on stdin
python3 idea_refiner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Idea Refiner — Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#idea-refiner
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/idea_refiner',
    "version": '2.0.0',
    "display_name": 'Idea Refiner',
    "description": 'Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through.',
    "author": 'Mathias Salomonsen',
    "tags": ['productivity', 'planning', 'decision_making', 'refinement', 'brainstorming'],
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
        "upstream_slug": 'idea-refiner',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#idea-refiner',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'f0afbd6c6948a24e',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:planning', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class IdeaRefiner(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'IdeaRefiner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(IdeaRefiner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
