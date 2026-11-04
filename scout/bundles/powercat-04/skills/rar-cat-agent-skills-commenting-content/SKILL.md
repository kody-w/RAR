---
name: "rar-cat-agent-skills-commenting-content"
description: "Comments Word or PowerPoint files with Comments."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/commenting_content", "rar_sha256": "9c7b154df5c10cdacffbad111641404a33a2d64cc6cb64867c867d8df66f8489", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/commenting_content`. The original RAPP
agent is preserved byte-for-byte in `commenting_content_agent.py` and in the RCI capsule.

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

Commenting Content — Comments Word or PowerPoint files with Comments.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#commenting-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commenting_content_agent.py` and embedded as the fenced Python below (sha256 9c7b154df5c10cda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commenting_content_agent.py` first:

```bash
python3 commenting_content_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commenting_content_agent.py   # or on stdin
python3 commenting_content_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/commenting_content_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/commenting_content_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/commenting_content/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Commenting Content — Comments Word or PowerPoint files with Comments.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#commenting-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/commenting_content',
    "version": '3.0.2',
    "display_name": 'Commenting Content',
    "description": 'Comments Word or PowerPoint files with Comments.',
    "author": 'AndrewHessMSFT',
    "tags": ['documents', 'productivity'],
    "category": 'productivity',
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
        "upstream_slug": 'commenting-content',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#commenting-content',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fcac24466182f80a',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CommentingContent(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CommentingContent'
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
    print(CommentingContent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
