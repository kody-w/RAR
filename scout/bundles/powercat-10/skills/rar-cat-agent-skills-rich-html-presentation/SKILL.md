---
name: "rar-cat-agent-skills-rich-html-presentation"
description: "Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/rich_html_presentation", "rar_sha256": "840d0228ff9167063d5c04517549c9a9b64c22fa85f9e8a8da393481809fb956", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.2.2", "author": "Henry Jammes", "tags": ["presentations", "html", "design", "productivity", "writing"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rich_html_presentation_agent.py` and embedded as the fenced Python below (sha256 840d0228ff916706…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rich_html_presentation_agent.py` first:

```bash
python3 rich_html_presentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rich_html_presentation_agent.py   # or on stdin
python3 rich_html_presentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/rich_html_presentation_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rich_html_presentation_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/rich_html_presentation/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
