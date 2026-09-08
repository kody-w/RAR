---
name: "rar-cat-agent-skills-skill-authoring-coach"
description: "Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/skill_authoring_coach", "rar_sha256": "b367fbfdfd349e0947f87666afc5f82890b1500c3e600fda8d63b669fe7695f8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["skills", "authoring", "documentation", "productivity", "agent"]}
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
