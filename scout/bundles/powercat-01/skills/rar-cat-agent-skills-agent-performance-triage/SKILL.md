---
name: "rar-cat-agent-skills-agent-performance-triage"
description: "Turn a live agent's analytics and transcripts into a diagnosis and a prioritized improvement backlog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_performance_triage", "rar_sha256": "c733f72d68b4a9d519b6a7ff701c963143d0a361037a576be6f8f298fe17ca82", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marco Zama", "tags": ["copilot_studio", "analytics", "optimization", "operations", "post_launch", "backlog", "assessment", "monitoring"]}
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
