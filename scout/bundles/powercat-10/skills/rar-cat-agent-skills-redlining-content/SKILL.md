---
name: "rar-cat-agent-skills-redlining-content"
description: "Redlines a document based on changes from a template with Track Changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/redlining_content", "rar_sha256": "28f933da117e15feeca641c67a251548a586847b5641189c1780a8633db5b5f8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
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
