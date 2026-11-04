---
name: "rar-cat-agent-skills-commenting-content"
description: "Comments Word or PowerPoint files with Comments."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/commenting_content", "rar_sha256": "9c7b154df5c10cdacffbad111641404a33a2d64cc6cb64867c867d8df66f8489", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
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
