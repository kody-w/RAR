---
name: "rar-cat-agent-skills-agent-harness-explorer"
description: "Discover, document, and monitor what the agent harness can do \u2014 Python libraries, tools, MCP servers, and runtime capabilities \u2014 with repeatable, comparable snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_harness_explorer", "rar_sha256": "4e86bceb09a0a54ccd4332a264a2601cd15a61f27f86be2cbf1a859693f83cd5", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Chris Garty and Andrew Hess", "tags": ["diagnostics", "runtime", "python", "capabilities", "snapshots", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/agent_harness_explorer`. The original RAPP
agent is preserved byte-for-byte in `agent_harness_explorer_agent.py` and in the RCI capsule.

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

Agent Harness Explorer — Discover, document, and monitor what the agent harness can do — Python libraries, tools, MCP servers, and runtime capabilities — with repeatable, comparable snapshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a diagnose capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-harness-explorer
  Upstream author: Chris Garty and Andrew Hess
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "environment": {
      "description": "Optional. Where it happens, and where it does not.",
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
      "description": "The symptom \u2014 what was observed, not what you think caused it.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_harness_explorer_agent.py` and embedded as the fenced Python below (sha256 4e86bceb09a0a54c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_harness_explorer_agent.py` first:

```bash
python3 agent_harness_explorer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_harness_explorer_agent.py   # or on stdin
python3 agent_harness_explorer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/agent_harness_explorer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/agent_harness_explorer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/agent_harness_explorer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Agent Harness Explorer — Discover, document, and monitor what the agent harness can do — Python libraries, tools, MCP servers, and runtime capabilities — with repeatable, comparable snapshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a diagnose capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-harness-explorer
  Upstream author: Chris Garty and Andrew Hess
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_harness_explorer',
    "version": '2.1.2',
    "display_name": 'Agent Harness Explorer',
    "description": 'Discover, document, and monitor what the agent harness can do — Python libraries, tools, MCP servers, and runtime capabilities — with repeatable, comparable snapshots.',
    "author": 'Chris Garty and Andrew Hess',
    "tags": ['diagnostics', 'runtime', 'python', 'capabilities', 'snapshots', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'agent-harness-explorer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-harness-explorer',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '61ae6c239cb9c236',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork', 'Scout'],
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
_SPEC = {'archetype': 'diagnose', 'checks': ['The symptom is recorded separately from any theory about it.', 'A reliable reproduction exists.', 'Causation was demonstrated by toggling it, not inferred from correlation.', 'A regression check now covers the failure.'], 'confidence': 0.571, 'deliverable': 'A diagnosis: observed symptom, reproduction, the boundary that isolated it, demonstrated cause, fix, and the check that pins it.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'environment': 'Optional. Where it happens, and where it does not.', 'subject': 'The symptom — what was observed, not what you think caused it.'}, 'refined_by': 'rules', 'signals': ['tag:diagnostics', 'tag:runtime'], 'steps': ['Separate the symptom from the theory. Write down only what was observed, with timestamps.', 'Establish a reliable reproduction. An intermittent bug you cannot trigger is not yet being debugged, it is being guessed at.', 'Find the boundary: the nearest case that works and the nearest that fails. The cause lives between them.', 'Bisect that gap, changing one variable at a time.', 'Confirm the cause by making the failure appear and disappear on demand.', 'Fix the cause, then add the check that would have caught it — otherwise it returns under a different symptom.'], 'subject_label': 'symptom to diagnose', 'verb': 'Diagnose'}


class AgentHarnessExplorer(BasicAgent):
    """Diagnose agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AgentHarnessExplorer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'environment': {'description': 'Optional. Where it happens, and where it does not.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The symptom — what was observed, not what you think caused it.', 'type': 'string'}},
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
    print(AgentHarnessExplorer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
