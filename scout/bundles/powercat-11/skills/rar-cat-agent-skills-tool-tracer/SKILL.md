---
name: "rar-cat-agent-skills-tool-tracer"
description: "On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` \u2192 `tool_trace.json`)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/tool_tracer", "rar_sha256": "795258346e89a87dcd4972fa952b9f58ed8e728ee53155c36f30dc0ff307ef89", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Rafael Lopez Alcaraz", "tags": ["transparency", "observability", "debugging", "workflow", "logging", "json", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `tool_tracer_agent.py` and embedded as the fenced Python below (sha256 795258346e89a87d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `tool_tracer_agent.py` first:

```bash
python3 tool_tracer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 tool_tracer_agent.py   # or on stdin
python3 tool_tracer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/tool_tracer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/tool_tracer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/tool_tracer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
