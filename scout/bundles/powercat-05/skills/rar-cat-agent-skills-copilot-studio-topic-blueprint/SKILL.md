---
name: "rar-cat-agent-skills-copilot-studio-topic-blueprint"
description: "Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_topic_blueprint", "rar_sha256": "a9be9e59a4cacd1eef693c098ba55c3cac648f190e65d3a0361b5094fcfa48f3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Elliot Margot", "tags": ["agent", "blueprint", "topics", "design", "power_platform", "orchestration", "adaptive_card"]}
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
