---
name: "rar-cat-agent-skills-gantt-chart-generator"
description: "Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame \u2014 with group colours, completion overlays, and a today line."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/gantt_chart_generator", "rar_sha256": "2df2f858299c6f1239e65bb152f4bbb593ba2072dbcac6316d6362416bdee486", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "gantt_chart_generator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/gantt-chart-generator:51184e12fa57bae6346daefde3787b5c913c95d753d47c2cd0989d8e2bdd2119", "kind": "skill"}, "version": "2.0.0", "author": "Nazish Qasim", "tags": ["gantt", "timeline", "project_management", "matplotlib", "charts", "scripts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/gantt_chart_generator`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `gantt_chart_generator_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
