---
name: "rar-cat-agent-skills-agent-harness-explorer"
description: "Discover, document, and monitor what the agent harness can do \u2014 Python libraries, tools, MCP servers, and runtime capabilities \u2014 with repeatable, comparable snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_harness_explorer", "rar_sha256": "ae4ce30f551513975fd4b56323c880f35f9894e07285212f88b81f65ce2f8eae", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Chris Garty and Andrew Hess", "tags": ["diagnostics", "runtime", "python", "capabilities", "snapshots", "scripts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_harness_explorer_agent.py` and embedded as the fenced Python below (sha256 ae4ce30f55151397…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_harness_explorer_agent.py` first:

```bash
python3 agent_harness_explorer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_harness_explorer_agent.py   # or on stdin
python3 agent_harness_explorer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
