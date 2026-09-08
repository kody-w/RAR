---
name: "rar-cat-agent-skills-anonymised-case-study-writer"
description: "Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/anonymised_case_study_writer", "rar_sha256": "a33da39c5a36434bb8c16f1d206623b4f32f7826daa65859162fce827c579996", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "case_study", "marketing", "documents", "content", "privacy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/anonymised_case_study_writer`. The original RAPP
agent is preserved byte-for-byte in `anonymised_case_study_writer_agent.py` and in the RCI capsule.

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

Anonymised Case Study Writer — Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `anonymised_case_study_writer_agent.py` and embedded as the fenced Python below (sha256 a33da39c5a36434b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `anonymised_case_study_writer_agent.py` first:

```bash
python3 anonymised_case_study_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 anonymised_case_study_writer_agent.py   # or on stdin
python3 anonymised_case_study_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Anonymised Case Study Writer — Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/anonymised_case_study_writer',
    "version": '2.1.2',
    "display_name": 'Anonymised Case Study Writer',
    "description": 'Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.',
    "author": 'Simon Owen',
    "tags": ['writing', 'case_study', 'marketing', 'documents', 'content', 'privacy'],
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
        "upstream_slug": 'anonymised-case-study-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '30ca39e3e8405c3e',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.857, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:documents', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AnonymisedCaseStudyWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnonymisedCaseStudyWriter'
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
    print(AnonymisedCaseStudyWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
