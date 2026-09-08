---
name: "rar-cat-agent-skills-rich-html-presentation"
description: "Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/rich_html_presentation", "rar_sha256": "f8f6f22899b994c7047f09873a6508f5e4a0aad70f5551620130f1793d8bfdb4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.2.2", "author": "Henry Jammes", "tags": ["presentations", "html", "design", "productivity", "writing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/rich_html_presentation`. The original RAPP
agent is preserved byte-for-byte in `rich_html_presentation_agent.py` and in the RCI capsule.

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

Rich HTML Presentation — Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#rich-html-presentation
  Upstream author: Henry Jammes
  Upstream version: 1.2.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rich_html_presentation_agent.py` and embedded as the fenced Python below (sha256 f8f6f22899b994c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rich_html_presentation_agent.py` first:

```bash
python3 rich_html_presentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rich_html_presentation_agent.py   # or on stdin
python3 rich_html_presentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rich HTML Presentation — Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#rich-html-presentation
  Upstream author: Henry Jammes
  Upstream version: 1.2.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/rich_html_presentation',
    "version": '3.2.2',
    "display_name": 'Rich HTML Presentation',
    "description": 'Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.',
    "author": 'Henry Jammes',
    "tags": ['presentations', 'html', 'design', 'productivity', 'writing'],
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
        "upstream_slug": 'rich-html-presentation',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#rich-html-presentation',
        "upstream_version": '1.2.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dc40638371835363',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.667, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:presentations', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class RichHtmlPresentation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RichHtmlPresentation'
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
    print(RichHtmlPresentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
