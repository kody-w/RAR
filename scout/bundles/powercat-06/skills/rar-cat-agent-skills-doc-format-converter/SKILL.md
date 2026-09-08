---
name: "rar-cat-agent-skills-doc-format-converter"
description: "Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text \u2014 fully offline, using only the libraries already in the agent sandbox."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/doc_format_converter", "rar_sha256": "23adb975b7c161e8ac5e8c9af419d38a2c1eae82abe86a26cd99bc570ba2c1ee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Andreas Adner", "tags": ["documents", "conversion", "markdown", "pdf", "office", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/doc_format_converter`. The original RAPP
agent is preserved byte-for-byte in `doc_format_converter_agent.py` and in the RCI capsule.

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

Universal Document Converter — Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#doc-format-converter
  Upstream author: Andreas Adner
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `doc_format_converter_agent.py` and embedded as the fenced Python below (sha256 23adb975b7c161e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `doc_format_converter_agent.py` first:

```bash
python3 doc_format_converter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 doc_format_converter_agent.py   # or on stdin
python3 doc_format_converter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Universal Document Converter — Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#doc-format-converter
  Upstream author: Andreas Adner
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/doc_format_converter',
    "version": '3.0.2',
    "display_name": 'Universal Document Converter',
    "description": 'Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.',
    "author": 'Andreas Adner',
    "tags": ['documents', 'conversion', 'markdown', 'pdf', 'office', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'doc-format-converter',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#doc-format-converter',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd1c0d69a8989af49',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.375, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class DocFormatConverter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DocFormatConverter'
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
    print(DocFormatConverter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
