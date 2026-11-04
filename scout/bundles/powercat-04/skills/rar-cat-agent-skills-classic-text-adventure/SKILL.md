---
name: "rar-cat-agent-skills-classic-text-adventure"
description: "Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/classic_text_adventure", "rar_sha256": "4c4a86cbf7aeee5e0f57eff39d2e15f30542f45222da4cb6bad6b6993f190995", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Andreas Adner", "tags": ["adventure", "game", "python"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/classic_text_adventure`. The original RAPP
agent is preserved byte-for-byte in `classic_text_adventure_agent.py` and in the RCI capsule.

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

Classic Text Adventure — Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#classic-text-adventure
  Upstream author: Andreas Adner
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `classic_text_adventure_agent.py` and embedded as the fenced Python below (sha256 4c4a86cbf7aeee5e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `classic_text_adventure_agent.py` first:

```bash
python3 classic_text_adventure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 classic_text_adventure_agent.py   # or on stdin
python3 classic_text_adventure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/classic_text_adventure_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/classic_text_adventure_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/classic_text_adventure/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Classic Text Adventure — Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#classic-text-adventure
  Upstream author: Andreas Adner
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/classic_text_adventure',
    "version": '2.1.2',
    "display_name": 'Classic Text Adventure',
    "description": 'Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics.',
    "author": 'Andreas Adner',
    "tags": ['adventure', 'game', 'python'],
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
        "upstream_slug": 'classic-text-adventure',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#classic-text-adventure',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '9a6d89774728370c',
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class ClassicTextAdventure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ClassicTextAdventure'
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
    print(ClassicTextAdventure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
