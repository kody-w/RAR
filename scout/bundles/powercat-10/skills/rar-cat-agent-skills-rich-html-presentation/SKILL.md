---
name: "rar-cat-agent-skills-rich-html-presentation"
description: "Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/rich_html_presentation", "rar_sha256": "840d0228ff9167063d5c04517549c9a9b64c22fa85f9e8a8da393481809fb956", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.2.2", "author": "Henry Jammes", "tags": ["presentations", "html", "design", "productivity", "writing"]}
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
