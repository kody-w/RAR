---
name: "rar-cat-agent-skills-acroform-writer"
description: "Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/acroform_writer", "rar_sha256": "443631d1d4364661b643c3d85cf3a0fadab6021e31c0796662765d71940be22a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sandeep Angara", "tags": ["acroform", "pdf", "forms", "python", "documents"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/acroform_writer`. The original RAPP
agent is preserved byte-for-byte in `acroform_writer_agent.py` and in the RCI capsule.

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

AcroForm Writer — Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#acroform-writer
  Upstream author: Sandeep Angara
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `acroform_writer_agent.py` and embedded as the fenced Python below (sha256 443631d1d4364661…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `acroform_writer_agent.py` first:

```bash
python3 acroform_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 acroform_writer_agent.py   # or on stdin
python3 acroform_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AcroForm Writer — Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#acroform-writer
  Upstream author: Sandeep Angara
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/acroform_writer',
    "version": '3.0.2',
    "display_name": 'AcroForm Writer',
    "description": "Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF",
    "author": 'Sandeep Angara',
    "tags": ['acroform', 'pdf', 'forms', 'python', 'documents'],
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
        "upstream_slug": 'acroform-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#acroform-writer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b96d3187f92bf269',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.667, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AcroformWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AcroformWriter'
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
    print(AcroformWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
