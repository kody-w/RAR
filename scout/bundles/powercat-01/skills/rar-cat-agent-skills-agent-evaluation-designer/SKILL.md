---
name: "rar-cat-agent-skills-agent-evaluation-designer"
description: "Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_evaluation_designer", "rar_sha256": "3eb41727a5557227f7de268386141ced0eb30e2a55b6fd292c8ce8d6f93f7b97", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "James Papadimitriou", "tags": ["evaluation", "testing", "quality_assurance", "go_live", "decision_making"]}
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
