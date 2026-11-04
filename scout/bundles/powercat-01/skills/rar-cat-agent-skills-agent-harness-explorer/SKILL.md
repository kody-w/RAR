---
name: "rar-cat-agent-skills-agent-harness-explorer"
description: "Discover, document, and monitor what the agent harness can do \u2014 Python libraries, tools, MCP servers, and runtime capabilities \u2014 with repeatable, comparable snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_harness_explorer", "rar_sha256": "4e86bceb09a0a54ccd4332a264a2601cd15a61f27f86be2cbf1a859693f83cd5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Chris Garty and Andrew Hess", "tags": ["diagnostics", "runtime", "python", "capabilities", "snapshots", "scripts"]}
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
