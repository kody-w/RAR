---
name: "rar-cat-agent-skills-agent-performance-triage"
description: "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_performance_triage", "rar_sha256": "d5ab5d95947d61784c790645d416c6ead847ceededcefbe615a1b505b80d59b3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Marco Zama", "tags": ["copilot_studio", "analytics", "optimization", "operations", "post_launch", "backlog", "assessment", "monitoring"]}
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
