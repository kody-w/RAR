---
name: "rar-cat-agent-skills-wikipedia-human-style-writing"
description: "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wikipedia_human_style_writing", "rar_sha256": "ec40d454b5af83d585e82045cc3a98514cf04def8ec70f25a3e94f819abe8bf2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Chris Garty", "tags": ["writing", "content", "editing", "style", "humanize", "ai_detection", "wikipedia"]}
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
