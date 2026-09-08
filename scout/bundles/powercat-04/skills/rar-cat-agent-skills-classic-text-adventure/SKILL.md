---
name: "rar-cat-agent-skills-classic-text-adventure"
description: "Play a deterministic, resumable Colossal Cave adventure with exact game output and built-in diagnostics."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/classic_text_adventure", "rar_sha256": "09395f5d6e086ccbeb20463fd8726db778b02f174064e42616b0ab3b4d7e5fac", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Andreas Adner", "tags": ["adventure", "game", "python"]}
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
