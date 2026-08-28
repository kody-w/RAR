---
name: "rar-cat-agent-skills-gantt-chart-generator"
description: "Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame \u2014 with group colours, completion overlays, and a today line."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/gantt_chart_generator", "rar_sha256": "2df2f858299c6f1239e65bb152f4bbb593ba2072dbcac6316d6362416bdee486", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Nazish Qasim", "tags": ["gantt", "timeline", "project_management", "matplotlib", "charts", "scripts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `gantt_chart_generator_agent.py` and embedded as the fenced Python below (sha256 2df2f858299c6f12…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `gantt_chart_generator_agent.py` first:

```bash
python3 gantt_chart_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 gantt_chart_generator_agent.py   # or on stdin
python3 gantt_chart_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
