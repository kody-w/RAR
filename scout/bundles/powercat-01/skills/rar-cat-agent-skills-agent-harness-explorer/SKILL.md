---
name: "rar-cat-agent-skills-agent-harness-explorer"
description: "Discover, document, and monitor what the agent harness can do \u2014 Python libraries, tools, MCP servers, and runtime capabilities \u2014 with repeatable, comparable snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_harness_explorer", "rar_sha256": "ae4ce30f551513975fd4b56323c880f35f9894e07285212f88b81f65ce2f8eae", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Chris Garty and Andrew Hess", "tags": ["diagnostics", "runtime", "python", "capabilities", "snapshots", "scripts"]}
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
