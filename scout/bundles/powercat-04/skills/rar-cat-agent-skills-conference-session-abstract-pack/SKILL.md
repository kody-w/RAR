---
name: "rar-cat-agent-skills-conference-session-abstract-pack"
description: "Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conference_session_abstract_pack", "rar_sha256": "2f037010b37d46b3b8c438a051efa8a15331159a047f2d7bf66dc4ab81cfa2b2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "conference", "abstract", "speaking", "content", "productivity"]}
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
