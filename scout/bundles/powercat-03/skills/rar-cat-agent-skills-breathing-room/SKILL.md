---
name: "rar-cat-agent-skills-breathing-room"
description: "Shows where your own week has room to breathe and where it does not, from your calendar and what you send: meeting density, back-to-back runs, deep-work blocks, evenings and weekends, and the load already building three to ten days out. When a day or a coming week is overloaded it points to the most movable meetings, and it recognises time off rather than reading it as a quiet week. Reports on yo\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/breathing_room", "rar_sha256": "c1c264754985128b9c1ffd20b0e9b22a6766c10b6b2e72a0714764af07e00b0a", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.1.3", "author": "Allan De Castro", "tags": ["calendar", "workload", "focus", "work_life_balance", "meetings", "deep_work", "self_service"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `breathing_room_agent.py` and embedded as the fenced Python below (sha256 c1c264754985128b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `breathing_room_agent.py` first:

```bash
python3 breathing_room_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 breathing_room_agent.py   # or on stdin
python3 breathing_room_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/breathing_room_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/breathing_room_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/breathing_room/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
