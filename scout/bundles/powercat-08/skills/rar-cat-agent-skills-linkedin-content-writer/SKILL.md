---
name: "rar-cat-agent-skills-linkedin-content-writer"
description: "Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_writer", "rar_sha256": "0cd18fa07894aca3d64e11c86ed0a6d8eff173f27962ee6a8897dd2afff2c6b2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Becky Still, Digital Boop Ltd", "tags": ["linkedin", "social_media", "writing", "content"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/linkedin_content_writer`. The original RAPP
agent is preserved byte-for-byte in `linkedin_content_writer_agent.py` and in the RCI capsule.

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

LinkedIn Content Writer — Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer
  Upstream author: Becky Still, Digital Boop Ltd
  Upstream version: 1.0.1
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `linkedin_content_writer_agent.py` and embedded as the fenced Python below (sha256 0cd18fa07894aca3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `linkedin_content_writer_agent.py` first:

```bash
python3 linkedin_content_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 linkedin_content_writer_agent.py   # or on stdin
python3 linkedin_content_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
LinkedIn Content Writer — Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer
  Upstream author: Becky Still, Digital Boop Ltd
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/linkedin_content_writer',
    "version": '3.0.3',
    "display_name": 'LinkedIn Content Writer',
    "description": 'Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.',
    "author": 'Becky Still, Digital Boop Ltd',
    "tags": ['linkedin', 'social_media', 'writing', 'content'],
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
        "upstream_slug": 'linkedin-content-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b67b1c225f5d7237',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class LinkedinContentWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LinkedinContentWriter'
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
    print(LinkedinContentWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
