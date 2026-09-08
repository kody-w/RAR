---
name: "rar-cat-agent-skills-skill-authoring-coach"
description: "Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/skill_authoring_coach", "rar_sha256": "b367fbfdfd349e0947f87666afc5f82890b1500c3e600fda8d63b669fe7695f8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["skills", "authoring", "documentation", "productivity", "agent"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/skill_authoring_coach`. The original RAPP
agent is preserved byte-for-byte in `skill_authoring_coach_agent.py` and in the RCI capsule.

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

Skill Authoring Coach — Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `skill_authoring_coach_agent.py` and embedded as the fenced Python below (sha256 b367fbfdfd349e09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `skill_authoring_coach_agent.py` first:

```bash
python3 skill_authoring_coach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 skill_authoring_coach_agent.py   # or on stdin
python3 skill_authoring_coach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Skill Authoring Coach — Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/skill_authoring_coach',
    "version": '2.1.2',
    "display_name": 'Skill Authoring Coach',
    "description": 'Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging.',
    "author": 'Simon Owen',
    "tags": ['skills', 'authoring', 'documentation', 'productivity', 'agent'],
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
        "upstream_slug": 'skill-authoring-coach',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#skill-authoring-coach',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dd0ed10e586119e5',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 1.0, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:design'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class SkillAuthoringCoach(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SkillAuthoringCoach'
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
    print(SkillAuthoringCoach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
