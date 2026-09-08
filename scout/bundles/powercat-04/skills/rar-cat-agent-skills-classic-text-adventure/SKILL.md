---
name: "rar-cat-agent-skills-classic-text-adventure"
description: "Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/classic_text_adventure", "rar_sha256": "09395f5d6e086ccbeb20463fd8726db778b02f174064e42616b0ab3b4d7e5fac", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Andreas Adner", "tags": ["adventure", "game", "python"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `classic_text_adventure_agent.py` and embedded as the fenced Python below (sha256 09395f5d6e086ccb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `classic_text_adventure_agent.py` first:

```bash
python3 classic_text_adventure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 classic_text_adventure_agent.py   # or on stdin
python3 classic_text_adventure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
