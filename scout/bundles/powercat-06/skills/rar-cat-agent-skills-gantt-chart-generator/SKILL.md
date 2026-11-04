---
name: "rar-cat-agent-skills-gantt-chart-generator"
description: "Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame \u2014 with group colours, completion overlays, and a today line."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/gantt_chart_generator", "rar_sha256": "061ce3cfa4ea2f9aa26ffd7d11a22e3555748d5b254ca6ce2d6eb091b2c48a3a", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["gantt", "timeline", "project_management", "matplotlib", "charts", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/gantt_chart_generator`. The original RAPP
agent is preserved byte-for-byte in `gantt_chart_generator_agent.py` and in the RCI capsule.

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

Gantt Chart Builder — Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame — with group colours, completion overlays, and a today line.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#gantt-chart-generator
  Upstream author: Nazish Qasim
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `gantt_chart_generator_agent.py` and embedded as the fenced Python below (sha256 061ce3cfa4ea2f9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `gantt_chart_generator_agent.py` first:

```bash
python3 gantt_chart_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 gantt_chart_generator_agent.py   # or on stdin
python3 gantt_chart_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/gantt_chart_generator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/gantt_chart_generator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/gantt_chart_generator/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Gantt Chart Builder — Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame — with group colours, completion overlays, and a today line.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#gantt-chart-generator
  Upstream author: Nazish Qasim
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/gantt_chart_generator',
    "version": '3.0.2',
    "display_name": 'Gantt Chart Builder',
    "description": 'Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame — with group colours, completion overlays, and a today line.',
    "author": 'Nazish Qasim',
    "tags": ['gantt', 'timeline', 'project_management', 'matplotlib', 'charts', 'scripts'],
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
        "upstream_slug": 'gantt-chart-generator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#gantt-chart-generator',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fe66d46e3035d79c',
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:scripts', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class GanttChartGenerator(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GanttChartGenerator'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(GanttChartGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
