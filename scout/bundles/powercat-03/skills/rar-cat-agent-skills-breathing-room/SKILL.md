---
name: "rar-cat-agent-skills-breathing-room"
description: "Shows where your own week has room to breathe and where it does not, from your calendar and what you send: meeting density, back-to-back runs, deep-work blocks, evenings and weekends, and the load already building three to ten days out. When a day or a coming week is overloaded it points to the most movable meetings, and it recognises time off rather than reading it as a quiet week. Reports on yo\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/breathing_room", "rar_sha256": "fe3c40feeeb2605e05593311b3be9795246c664abc303adc3c2602715001418b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.1.3", "author": "Allan De Castro", "tags": ["calendar", "workload", "focus", "work_life_balance", "meetings", "deep_work", "self_service"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/breathing_room`. The original RAPP
agent is preserved byte-for-byte in `breathing_room_agent.py` and in the RCI capsule.

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

Breathing Room — Shows where your own week has room to breathe and where it does not, from your calendar and what you send: meeting density, back-to-back runs, deep-work blocks, evenings and weekends, and the load already building three to ten days out. When a day or a coming week is overloaded it points to the most movable meetings, and it recognises time off rather than reading it as a quiet week. Reports on yo…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#breathing-room
  Upstream author: Allan De Castro
  Upstream version: 1.1.1
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `breathing_room_agent.py` and embedded as the fenced Python below (sha256 fe3c40feeeb2605e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `breathing_room_agent.py` first:

```bash
python3 breathing_room_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 breathing_room_agent.py   # or on stdin
python3 breathing_room_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Breathing Room — Shows where your own week has room to breathe and where it does not, from your calendar and what you send: meeting density, back-to-back runs, deep-work blocks, evenings and weekends, and the load already building three to ten days out. When a day or a coming week is overloaded it points to the most movable meetings, and it recognises time off rather than reading it as a quiet week. Reports on yo…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#breathing-room
  Upstream author: Allan De Castro
  Upstream version: 1.1.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/breathing_room',
    "version": '3.1.3',
    "display_name": 'Breathing Room',
    "description": 'Shows where your own week has room to breathe and where it does not, from your calendar and what you send: meeting density, back-to-back runs, deep-work blocks, evenings and weekends, and the load already building three to ten days out. When a day or a coming week is overloaded it points to the most movable meetings, and it recognises time off rather than reading it as a quiet week. Reports on yo…',
    "author": 'Allan De Castro',
    "tags": ['calendar', 'workload', 'focus', 'work_life_balance', 'meetings', 'deep_work', 'self_service'],
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
        "upstream_slug": 'breathing-room',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#breathing-room',
        "upstream_version": '1.1.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '419764044da81b3f',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class BreathingRoom(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BreathingRoom'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(BreathingRoom().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
