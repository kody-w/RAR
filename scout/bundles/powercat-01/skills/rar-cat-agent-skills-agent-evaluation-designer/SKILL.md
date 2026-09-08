---
name: "rar-cat-agent-skills-agent-evaluation-designer"
description: "Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_evaluation_designer", "rar_sha256": "092e5313a720a8566584b69405d92d384a4563943ea16bf6cb84abf87dd60ff3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "James Papadimitriou", "tags": ["evaluation", "testing", "quality_assurance", "go_live", "decision_making"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_evaluation_designer_agent.py` and embedded as the fenced Python below (sha256 092e5313a720a856…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_evaluation_designer_agent.py` first:

```bash
python3 agent_evaluation_designer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_evaluation_designer_agent.py   # or on stdin
python3 agent_evaluation_designer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
