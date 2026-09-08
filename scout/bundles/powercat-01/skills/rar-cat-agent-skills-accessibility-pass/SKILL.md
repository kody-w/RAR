---
name: "rar-cat-agent-skills-accessibility-pass"
description: "Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/accessibility_pass", "rar_sha256": "2ce6f88d58c2f5c0ca93ed74369fbcfafcca0c06ec2f5492710a5a20a3ca8f8d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["accessibility", "documents", "presentations", "powerpoint", "quality", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/accessibility_pass`. The original RAPP
agent is preserved byte-for-byte in `accessibility_pass_agent.py` and in the RCI capsule.

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

Accessibility Pass — Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#accessibility-pass
  Upstream author: Tim Karlsson
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `accessibility_pass_agent.py` and embedded as the fenced Python below (sha256 2ce6f88d58c2f5c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `accessibility_pass_agent.py` first:

```bash
python3 accessibility_pass_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 accessibility_pass_agent.py   # or on stdin
python3 accessibility_pass_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Accessibility Pass — Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#accessibility-pass
  Upstream author: Tim Karlsson
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/accessibility_pass',
    "version": '3.0.2',
    "display_name": 'Accessibility Pass',
    "description": "Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds.",
    "author": 'Tim Karlsson',
    "tags": ['accessibility', 'documents', 'presentations', 'powerpoint', 'quality', 'scripts'],
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
        "upstream_slug": 'accessibility-pass',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#accessibility-pass',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '183550ba28bed17f',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.471, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'tag:powerpoint', 'tag:presentations', 'word:deck', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AccessibilityPass(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AccessibilityPass'
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
    print(AccessibilityPass().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
