---
name: "rar-cat-agent-skills-agent-evaluation-designer"
description: "Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_evaluation_designer", "rar_sha256": "3eb41727a5557227f7de268386141ced0eb30e2a55b6fd292c8ce8d6f93f7b97", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "James Papadimitriou", "tags": ["evaluation", "testing", "quality_assurance", "go_live", "decision_making"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/agent_evaluation_designer`. The original RAPP
agent is preserved byte-for-byte in `agent_evaluation_designer_agent.py` and in the RCI capsule.

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

Agent Evaluation Designer — Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-evaluation-designer
  Upstream author: James Papadimitriou
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_evaluation_designer_agent.py` and embedded as the fenced Python below (sha256 3eb41727a5557227…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_evaluation_designer_agent.py` first:

```bash
python3 agent_evaluation_designer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_evaluation_designer_agent.py   # or on stdin
python3 agent_evaluation_designer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/agent_evaluation_designer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/agent_evaluation_designer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/agent_evaluation_designer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Agent Evaluation Designer — Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-evaluation-designer
  Upstream author: James Papadimitriou
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_evaluation_designer',
    "version": '3.0.2',
    "display_name": 'Agent Evaluation Designer',
    "description": 'Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision.',
    "author": 'James Papadimitriou',
    "tags": ['evaluation', 'testing', 'quality_assurance', 'go_live', 'decision_making'],
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
        "upstream_slug": 'agent-evaluation-designer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-evaluation-designer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '5932d5f6ea50fb35',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.308, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:quality_assurance', 'tag:testing'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AgentEvaluationDesigner(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AgentEvaluationDesigner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AgentEvaluationDesigner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
