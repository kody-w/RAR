---
name: "rar-cat-agent-skills-tool-tracer"
description: "On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` \u2192 `tool_trace.json`)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/tool_tracer", "rar_sha256": "94d1c0edc220629574391ccfba7db23a74bcced8cd5a12e608f317dbfae87151", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Rafael Lopez Alcaraz", "tags": ["transparency", "observability", "debugging", "workflow", "logging", "json", "productivity"]}
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
