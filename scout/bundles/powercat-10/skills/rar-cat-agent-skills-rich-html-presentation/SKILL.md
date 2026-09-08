---
name: "rar-cat-agent-skills-rich-html-presentation"
description: "Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/rich_html_presentation", "rar_sha256": "f8f6f22899b994c7047f09873a6508f5e4a0aad70f5551620130f1793d8bfdb4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.2.2", "author": "Henry Jammes", "tags": ["presentations", "html", "design", "productivity", "writing"]}
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
