---
name: "rar-cat-agent-skills-agent-evaluation-designer"
description: "Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_evaluation_designer", "rar_sha256": "092e5313a720a8566584b69405d92d384a4563943ea16bf6cb84abf87dd60ff3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "James Papadimitriou", "tags": ["evaluation", "testing", "quality_assurance", "go_live", "decision_making"]}
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
