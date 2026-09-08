---
name: "rar-cat-agent-skills-redlining-content"
description: "Redlines a document based on changes from a template with Track Changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/redlining_content", "rar_sha256": "28f933da117e15feeca641c67a251548a586847b5641189c1780a8633db5b5f8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `redlining_content_agent.py` and embedded as the fenced Python below (sha256 28f933da117e15fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `redlining_content_agent.py` first:

```bash
python3 redlining_content_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 redlining_content_agent.py   # or on stdin
python3 redlining_content_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
