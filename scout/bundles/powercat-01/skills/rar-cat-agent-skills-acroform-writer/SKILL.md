---
name: "rar-cat-agent-skills-acroform-writer"
description: "Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/acroform_writer", "rar_sha256": "d9cb428f86f969b809e2bb18378be5096f7e87a590f6bd2d8321d18e6087091d", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Sandeep Angara", "tags": ["acroform", "pdf", "forms", "python", "documents"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `acroform_writer_agent.py` and embedded as the fenced Python below (sha256 d9cb428f86f969b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `acroform_writer_agent.py` first:

```bash
python3 acroform_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 acroform_writer_agent.py   # or on stdin
python3 acroform_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/acroform_writer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/acroform_writer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/acroform_writer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
