---
name: "rar-cat-agent-skills-gantt-chart-generator"
description: "Generate clean, consistently-styled matplotlib Gantt charts from a schedule CSV or DataFrame \u2014 with group colours, completion overlays, and a today line."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/gantt_chart_generator", "rar_sha256": "e65f1661b81bf0103d70144a51f6b3ac3d022e795400f9e8c93ea1780eed398c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["gantt", "timeline", "project_management", "matplotlib", "charts", "scripts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `gantt_chart_generator_agent.py` and embedded as the fenced Python below (sha256 e65f1661b81bf010…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `gantt_chart_generator_agent.py` first:

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
