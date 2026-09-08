---
name: "rar-cat-agent-skills-accessibility-pass"
description: "Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/accessibility_pass", "rar_sha256": "2ce6f88d58c2f5c0ca93ed74369fbcfafcca0c06ec2f5492710a5a20a3ca8f8d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["accessibility", "documents", "presentations", "powerpoint", "quality", "scripts"]}
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
