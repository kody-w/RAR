---
name: "rar-cat-agent-skills-linkedin-content-writer"
description: "Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_writer", "rar_sha256": "0cd18fa07894aca3d64e11c86ed0a6d8eff173f27962ee6a8897dd2afff2c6b2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Becky Still, Digital Boop Ltd", "tags": ["linkedin", "social_media", "writing", "content"]}
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
