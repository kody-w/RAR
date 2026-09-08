---
name: "rar-cat-agent-skills-anonymised-case-study-writer"
description: "Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/anonymised_case_study_writer", "rar_sha256": "a33da39c5a36434bb8c16f1d206623b4f32f7826daa65859162fce827c579996", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "case_study", "marketing", "documents", "content", "privacy"]}
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
