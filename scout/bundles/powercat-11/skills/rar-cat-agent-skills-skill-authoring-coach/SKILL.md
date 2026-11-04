---
name: "rar-cat-agent-skills-skill-authoring-coach"
description: "Help makers design concise, reusable Agent Skills with clear triggers, instructions, resources, and packaging."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/skill_authoring_coach", "rar_sha256": "d87d562cb6ff69f03c5fbe70ec218c4a216e2f3a22cb4aa2055fdc360addc454", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["skills", "authoring", "documentation", "productivity", "agent"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `skill_authoring_coach_agent.py` and embedded as the fenced Python below (sha256 d87d562cb6ff69f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `skill_authoring_coach_agent.py` first:

```bash
python3 skill_authoring_coach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 skill_authoring_coach_agent.py   # or on stdin
python3 skill_authoring_coach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/skill_authoring_coach_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/skill_authoring_coach_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/skill_authoring_coach/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
