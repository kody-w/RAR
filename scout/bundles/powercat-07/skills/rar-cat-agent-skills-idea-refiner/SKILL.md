---
name: "rar-cat-agent-skills-idea-refiner"
description: "Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/idea_refiner", "rar_sha256": "1f45a76ddaa7dca12d9857414545d29e8dc4e2ee13f87af6eb03b928acdb7bb7", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "idea_refiner_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/idea-refiner:5e635294318c9e65c823a6780c0f3cb526245dcc329a4b69602519dc3ed4390a", "kind": "skill"}, "version": "2.0.0", "author": "Mathias Salomonsen", "tags": ["productivity", "planning", "decision_making", "refinement", "brainstorming"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/idea_refiner`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `idea_refiner_agent.py` is
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
