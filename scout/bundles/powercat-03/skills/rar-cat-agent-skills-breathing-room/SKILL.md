---
name: "rar-cat-agent-skills-breathing-room"
description: "Shows where your own week has room to breathe and where it does not, from your calendar and what you send: meeting density, back-to-back runs, deep-work blocks, evenings and weekends, and the load already building three to ten days out. When a day or a coming week is overloaded it points to the most movable meetings, and it recognises time off rather than reading it as a quiet week. Reports on yo\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/breathing_room", "rar_sha256": "fe3c40feeeb2605e05593311b3be9795246c664abc303adc3c2602715001418b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.3", "author": "Allan De Castro", "tags": ["calendar", "workload", "focus", "work_life_balance", "meetings", "deep_work", "self_service"]}
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
