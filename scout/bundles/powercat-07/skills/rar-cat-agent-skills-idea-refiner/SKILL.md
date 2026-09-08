---
name: "rar-cat-agent-skills-idea-refiner"
description: "Refines an existing plan, decision, or draft through relentless, branch-by-branch questioning. Grouped in batches of 2-5 with recommended answers, pulling facts from Work IQ where possible, until every part has been fully thought through."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/idea_refiner", "rar_sha256": "e738ccce46e81b957aee2b02fb6e92e0c6f7a007f8d264a0539158190464d5d4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["productivity", "planning", "decision_making", "refinement", "brainstorming"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `idea_refiner_agent.py` and embedded as the fenced Python below (sha256 e738ccce46e81b95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `idea_refiner_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
