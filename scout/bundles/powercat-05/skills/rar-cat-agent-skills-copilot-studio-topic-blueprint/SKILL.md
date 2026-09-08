---
name: "rar-cat-agent-skills-copilot-studio-topic-blueprint"
description: "Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_topic_blueprint", "rar_sha256": "a9be9e59a4cacd1eef693c098ba55c3cac648f190e65d3a0361b5094fcfa48f3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Elliot Margot", "tags": ["agent", "blueprint", "topics", "design", "power_platform", "orchestration", "adaptive_card"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_topic_blueprint`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_topic_blueprint_agent.py` and in the RCI capsule.

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

Copilot Studio Topic Blueprint — Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint
  Upstream author: Elliot Margot
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_topic_blueprint_agent.py` and embedded as the fenced Python below (sha256 a9be9e59a4cacd1e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_topic_blueprint_agent.py` first:

```bash
python3 copilot_studio_topic_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_topic_blueprint_agent.py   # or on stdin
python3 copilot_studio_topic_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Topic Blueprint — Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_topic_blueprint',
    "version": '3.0.2',
    "display_name": 'Copilot Studio Topic Blueprint',
    "description": 'Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan.',
    "author": 'Elliot Margot',
    "tags": ['agent', 'blueprint', 'topics', 'design', 'power_platform', 'orchestration', 'adaptive_card'],
    "category": 'creative',
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
        "upstream_slug": 'copilot-studio-topic-blueprint',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-topic-blueprint',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '05163d5246a491ef',
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.667, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'tag:design', 'word:blueprint', 'word:plan'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class CopilotStudioTopicBlueprint(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioTopicBlueprint'
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
    print(CopilotStudioTopicBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
