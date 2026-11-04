---
name: "rar-cat-agent-skills-redlining-content"
description: "Redlines a document based on changes from a template with Track Changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/redlining_content", "rar_sha256": "23f87285631370ceeebed84404c33b157dde7837d12fcffb70a243232f687688", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
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
