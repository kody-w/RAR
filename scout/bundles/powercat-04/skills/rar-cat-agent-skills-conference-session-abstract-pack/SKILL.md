---
name: "rar-cat-agent-skills-conference-session-abstract-pack"
description: "Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conference_session_abstract_pack", "rar_sha256": "2f037010b37d46b3b8c438a051efa8a15331159a047f2d7bf66dc4ab81cfa2b2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "conference", "abstract", "speaking", "content", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/conference_session_abstract_pack`. The original RAPP
agent is preserved byte-for-byte in `conference_session_abstract_pack_agent.py` and in the RCI capsule.

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

Conference Session Abstract Pack — Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack
  Upstream author: Simon Owen
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `conference_session_abstract_pack_agent.py` and embedded as the fenced Python below (sha256 2f037010b37d46b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `conference_session_abstract_pack_agent.py` first:

```bash
python3 conference_session_abstract_pack_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 conference_session_abstract_pack_agent.py   # or on stdin
python3 conference_session_abstract_pack_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conference Session Abstract Pack — Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/conference_session_abstract_pack',
    "version": '2.1.2',
    "display_name": 'Conference Session Abstract Pack',
    "description": 'Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.',
    "author": 'Simon Owen',
    "tags": ['writing', 'conference', 'abstract', 'speaking', 'content', 'productivity'],
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
        "upstream_slug": 'conference-session-abstract-pack',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '79b0788cb04dc619',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ConferenceSessionAbstractPack(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConferenceSessionAbstractPack'
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
    print(ConferenceSessionAbstractPack().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
