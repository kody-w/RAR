---
name: "rar-cat-agent-skills-gantt-chart-generator"
description: "Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame \u2014 with group colours, completion overlays, and a today line."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/gantt_chart_generator", "rar_sha256": "061ce3cfa4ea2f9aa26ffd7d11a22e3555748d5b254ca6ce2d6eb091b2c48a3a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["gantt", "timeline", "project_management", "matplotlib", "charts", "scripts"]}
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
