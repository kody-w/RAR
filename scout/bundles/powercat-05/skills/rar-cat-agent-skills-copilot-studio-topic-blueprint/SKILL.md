---
name: "rar-cat-agent-skills-copilot-studio-topic-blueprint"
description: "Turn a one-line use case into a build-ready Microsoft Copilot Studio agent blueprint: recommended agent type and orchestration, topics, tools, knowledge, variables, a welcome Adaptive Card, security and Copilot Credits notes, and a first test plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_topic_blueprint", "rar_sha256": "e2024d790e12876be0154250bf26a90cee1e959d35146d58c5a4107b9f58ce36", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Elliot Margot", "tags": ["agent", "blueprint", "topics", "design", "power_platform", "orchestration", "adaptive_card"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_topic_blueprint_agent.py` and embedded as the fenced Python below (sha256 e2024d790e12876b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_topic_blueprint_agent.py` first:

```bash
python3 copilot_studio_topic_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_topic_blueprint_agent.py   # or on stdin
python3 copilot_studio_topic_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_studio_topic_blueprint_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_topic_blueprint_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_topic_blueprint/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
