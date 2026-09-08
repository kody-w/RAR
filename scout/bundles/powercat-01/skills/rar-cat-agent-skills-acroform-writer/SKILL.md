---
name: "rar-cat-agent-skills-acroform-writer"
description: "Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/acroform_writer", "rar_sha256": "443631d1d4364661b643c3d85cf3a0fadab6021e31c0796662765d71940be22a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sandeep Angara", "tags": ["acroform", "pdf", "forms", "python", "documents"]}
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
