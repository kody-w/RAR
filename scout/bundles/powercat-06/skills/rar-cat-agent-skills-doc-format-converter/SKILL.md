---
name: "rar-cat-agent-skills-doc-format-converter"
description: "Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text \u2014 fully offline, using only the libraries already in the agent sandbox."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/doc_format_converter", "rar_sha256": "23adb975b7c161e8ac5e8c9af419d38a2c1eae82abe86a26cd99bc570ba2c1ee", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Andreas Adner", "tags": ["documents", "conversion", "markdown", "pdf", "office", "scripts"]}
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
