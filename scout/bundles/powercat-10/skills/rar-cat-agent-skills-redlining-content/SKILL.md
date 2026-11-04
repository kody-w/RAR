---
name: "rar-cat-agent-skills-redlining-content"
description: "Redlines a document based on changes from a template with Track Changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/redlining_content", "rar_sha256": "23f87285631370ceeebed84404c33b157dde7837d12fcffb70a243232f687688", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/redlining_content`. The original RAPP
agent is preserved byte-for-byte in `redlining_content_agent.py` and in the RCI capsule.

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

Redlining Content — Redlines a document based on changes from a template with Track Changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#redlining-content
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `redlining_content_agent.py` and embedded as the fenced Python below (sha256 23f87285631370ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `redlining_content_agent.py` first:

```bash
python3 redlining_content_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 redlining_content_agent.py   # or on stdin
python3 redlining_content_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/redlining_content_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/redlining_content_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/redlining_content/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Redlining Content — Redlines a document based on changes from a template with Track Changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#redlining-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/redlining_content',
    "version": '3.0.2',
    "display_name": 'Redlining Content',
    "description": 'Redlines a document based on changes from a template with Track Changes.',
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
        "upstream_slug": 'redlining-content',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#redlining-content',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '1c2ec4d219101bd1',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class RedliningContent(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RedliningContent'
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
    print(RedliningContent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
