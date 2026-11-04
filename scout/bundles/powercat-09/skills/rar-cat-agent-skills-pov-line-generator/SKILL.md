---
name: "rar-cat-agent-skills-pov-line-generator"
description: "Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pov_line_generator", "rar_sha256": "a44620f4c73e4333235c8caf48c5f63607e423bd181878e3a813b3c995c1e3d0", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "positioning", "marketing", "content", "social_media"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/pov_line_generator`. The original RAPP
agent is preserved byte-for-byte in `pov_line_generator_agent.py` and in the RCI capsule.

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

POV Line Generator — Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pov-line-generator
  Upstream author: Simon Owen
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pov_line_generator_agent.py` and embedded as the fenced Python below (sha256 a44620f4c73e4333…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pov_line_generator_agent.py` first:

```bash
python3 pov_line_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pov_line_generator_agent.py   # or on stdin
python3 pov_line_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/pov_line_generator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/pov_line_generator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/pov_line_generator/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
POV Line Generator — Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pov-line-generator
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/pov_line_generator',
    "version": '2.1.2',
    "display_name": 'POV Line Generator',
    "description": 'Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.',
    "author": 'Simon Owen',
    "tags": ['writing', 'positioning', 'marketing', 'content', 'social_media'],
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
        "upstream_slug": 'pov-line-generator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#pov-line-generator',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bf492abfe32d66ad',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing', 'word:generate'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PovLineGenerator(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PovLineGenerator'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(PovLineGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
