---
name: "rar-cat-agent-skills-agent-performance-triage"
description: "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_performance_triage", "rar_sha256": "c733f72d68b4a9d519b6a7ff701c963143d0a361037a576be6f8f298fe17ca82", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Marco Zama", "tags": ["copilot_studio", "analytics", "optimization", "operations", "post_launch", "backlog", "assessment", "monitoring"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_performance_triage_agent.py` and embedded as the fenced Python below (sha256 c733f72d68b4a9d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_performance_triage_agent.py` first:

```bash
python3 agent_performance_triage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_performance_triage_agent.py   # or on stdin
python3 agent_performance_triage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/agent_performance_triage_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/agent_performance_triage_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/agent_performance_triage/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
