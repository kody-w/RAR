---
name: "rar-cat-agent-skills-breathing-room"
description: "Shows where your own week has room to breathe and where it does not, from your calendar and what you send: meeting density, back-to-back runs, deep-work blocks, evenings and weekends, and the load already building three to ten days out. When a day or a coming week is overloaded it points to the most movable meetings, and it recognises time off rather than reading it as a quiet week. Reports on yo\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/breathing_room", "rar_sha256": "c1c264754985128b9c1ffd20b0e9b22a6766c10b6b2e72a0714764af07e00b0a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.3", "author": "Allan De Castro", "tags": ["calendar", "workload", "focus", "work_life_balance", "meetings", "deep_work", "self_service"]}
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
