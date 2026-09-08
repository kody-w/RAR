---
name: "rar-cat-agent-skills-tool-tracer"
description: "On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` \u2192 `tool_trace.json`)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/tool_tracer", "rar_sha256": "94d1c0edc220629574391ccfba7db23a74bcced8cd5a12e608f317dbfae87151", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafael Lopez Alcaraz", "tags": ["transparency", "observability", "debugging", "workflow", "logging", "json", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/tool_tracer`. The original RAPP
agent is preserved byte-for-byte in `tool_tracer_agent.py` and in the RCI capsule.

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

Tool Tracer — On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` → `tool_trace.json`).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a diagnose capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#tool-tracer
  Upstream author: Rafael Lopez Alcaraz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `tool_tracer_agent.py` and embedded as the fenced Python below (sha256 94d1c0edc2206295…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `tool_tracer_agent.py` first:

```bash
python3 tool_tracer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 tool_tracer_agent.py   # or on stdin
python3 tool_tracer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Tool Tracer — On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` → `tool_trace.json`).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a diagnose capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#tool-tracer
  Upstream author: Rafael Lopez Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/tool_tracer',
    "version": '3.0.2',
    "display_name": 'Tool Tracer',
    "description": 'On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` → `tool_trace.json`).',
    "author": 'Rafael Lopez Alcaraz',
    "tags": ['transparency', 'observability', 'debugging', 'workflow', 'logging', 'json', 'productivity'],
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
        "upstream_slug": 'tool-tracer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#tool-tracer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '5fcd9f882c958e11',
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
_SPEC = {'archetype': 'diagnose', 'checks': ['The symptom is recorded separately from any theory about it.', 'A reliable reproduction exists.', 'Causation was demonstrated by toggling it, not inferred from correlation.', 'A regression check now covers the failure.'], 'confidence': 0.6, 'deliverable': 'A diagnosis: observed symptom, reproduction, the boundary that isolated it, demonstrated cause, fix, and the check that pins it.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'environment': 'Optional. Where it happens, and where it does not.', 'subject': 'The symptom — what was observed, not what you think caused it.'}, 'refined_by': 'rules', 'signals': ['tag:observability', 'word:debug'], 'steps': ['Separate the symptom from the theory. Write down only what was observed, with timestamps.', 'Establish a reliable reproduction. An intermittent bug you cannot trigger is not yet being debugged, it is being guessed at.', 'Find the boundary: the nearest case that works and the nearest that fails. The cause lives between them.', 'Bisect that gap, changing one variable at a time.', 'Confirm the cause by making the failure appear and disappear on demand.', 'Fix the cause, then add the check that would have caught it — otherwise it returns under a different symptom.'], 'subject_label': 'symptom to diagnose', 'verb': 'Diagnose'}


class ToolTracer(BasicAgent):
    """Diagnose agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ToolTracer'
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
    print(ToolTracer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
