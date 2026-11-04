---
name: "rar-cat-agent-skills-tool-tracer"
description: "On-demand tool/action trace for Copilot Studio runs (`/special-debug tool-trace` \u2192 `tool_trace.json`)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/tool_tracer", "rar_sha256": "795258346e89a87dcd4972fa952b9f58ed8e728ee53155c36f30dc0ff307ef89", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Rafael Lopez Alcaraz", "tags": ["transparency", "observability", "debugging", "workflow", "logging", "json", "productivity"]}
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
