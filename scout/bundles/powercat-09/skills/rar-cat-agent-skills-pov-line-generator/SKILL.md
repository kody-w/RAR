---
name: "rar-cat-agent-skills-pov-line-generator"
description: "Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pov_line_generator", "rar_sha256": "a44620f4c73e4333235c8caf48c5f63607e423bd181878e3a813b3c995c1e3d0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "positioning", "marketing", "content", "social_media"]}
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
