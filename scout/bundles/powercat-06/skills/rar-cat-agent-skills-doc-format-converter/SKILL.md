---
name: "rar-cat-agent-skills-doc-format-converter"
description: "Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text \u2014 fully offline, using only the libraries already in the agent sandbox."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/doc_format_converter", "rar_sha256": "f4717f434448dedb4118c9bac67f91897994ccf3a9cee2ebed68021661ec4131", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Andreas Adner", "tags": ["documents", "conversion", "markdown", "pdf", "office", "scripts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `doc_format_converter_agent.py` and embedded as the fenced Python below (sha256 f4717f434448dedb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `doc_format_converter_agent.py` first:

```bash
python3 doc_format_converter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 doc_format_converter_agent.py   # or on stdin
python3 doc_format_converter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/doc_format_converter_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/doc_format_converter_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/doc_format_converter/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
