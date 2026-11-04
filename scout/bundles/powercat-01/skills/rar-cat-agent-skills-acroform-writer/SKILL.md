---
name: "rar-cat-agent-skills-acroform-writer"
description: "Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/acroform_writer", "rar_sha256": "d9cb428f86f969b809e2bb18378be5096f7e87a590f6bd2d8321d18e6087091d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sandeep Angara", "tags": ["acroform", "pdf", "forms", "python", "documents"]}
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
