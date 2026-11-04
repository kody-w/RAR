---
name: "rar-cat-agent-skills-classic-text-adventure"
description: "Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/classic_text_adventure", "rar_sha256": "4c4a86cbf7aeee5e0f57eff39d2e15f30542f45222da4cb6bad6b6993f190995", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Andreas Adner", "tags": ["adventure", "game", "python"]}
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
