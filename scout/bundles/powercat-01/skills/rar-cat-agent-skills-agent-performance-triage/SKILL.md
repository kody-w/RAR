---
name: "rar-cat-agent-skills-agent-performance-triage"
description: "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_performance_triage", "rar_sha256": "d5ab5d95947d61784c790645d416c6ead847ceededcefbe615a1b505b80d59b3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marco Zama", "tags": ["copilot_studio", "analytics", "optimization", "operations", "post_launch", "backlog", "assessment", "monitoring"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/agent_performance_triage`. The original RAPP
agent is preserved byte-for-byte in `agent_performance_triage_agent.py` and in the RCI capsule.

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

Agent Performance Triage — Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-performance-triage
  Upstream author: Marco Zama
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_performance_triage_agent.py` and embedded as the fenced Python below (sha256 d5ab5d95947d6178…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_performance_triage_agent.py` first:

```bash
python3 agent_performance_triage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_performance_triage_agent.py   # or on stdin
python3 agent_performance_triage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Agent Performance Triage — Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-performance-triage
  Upstream author: Marco Zama
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_performance_triage',
    "version": '3.0.2',
    "display_name": 'Agent Performance Triage',
    "description": "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog.",
    "author": 'Marco Zama',
    "tags": ['copilot_studio', 'analytics', 'optimization', 'operations', 'post_launch', 'backlog', 'assessment', 'monitoring'],
    "category": 'analysis',
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
        "upstream_slug": 'agent-performance-triage',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-performance-triage',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '7498e78b8a1f891e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.4, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:assessment'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class AgentPerformanceTriage(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AgentPerformanceTriage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(AgentPerformanceTriage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
