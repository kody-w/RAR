---
name: "rar-cat-agent-skills-wikipedia-human-style-writing"
description: "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wikipedia_human_style_writing", "rar_sha256": "ec40d454b5af83d585e82045cc3a98514cf04def8ec70f25a3e94f819abe8bf2", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Chris Garty", "tags": ["writing", "content", "editing", "style", "humanize", "ai_detection", "wikipedia"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/wikipedia_human_style_writing`. The original RAPP
agent is preserved byte-for-byte in `wikipedia_human_style_writing_agent.py` and in the RCI capsule.

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

Wikipedia Human Style Writing — Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing
  Upstream author: Chris Garty
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wikipedia_human_style_writing_agent.py` and embedded as the fenced Python below (sha256 ec40d454b5af83d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wikipedia_human_style_writing_agent.py` first:

```bash
python3 wikipedia_human_style_writing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wikipedia_human_style_writing_agent.py   # or on stdin
python3 wikipedia_human_style_writing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/wikipedia_human_style_writing_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/wikipedia_human_style_writing_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/wikipedia_human_style_writing/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Wikipedia Human Style Writing — Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing
  Upstream author: Chris Garty
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/wikipedia_human_style_writing',
    "version": '2.1.2',
    "display_name": 'Wikipedia Human Style Writing',
    "description": "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.",
    "author": 'Chris Garty',
    "tags": ['writing', 'content', 'editing', 'style', 'humanize', 'ai_detection', 'wikipedia'],
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
        "upstream_slug": 'wikipedia-human-style-writing',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4a55ea6837b037ca',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing', 'word:draft'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WikipediaHumanStyleWriting(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WikipediaHumanStyleWriting'
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
    print(WikipediaHumanStyleWriting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
