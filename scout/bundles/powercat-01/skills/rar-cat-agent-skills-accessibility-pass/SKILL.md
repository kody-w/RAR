---
name: "rar-cat-agent-skills-accessibility-pass"
description: "Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/accessibility_pass", "rar_sha256": "87ab5363801dd38441801dd9d3cfc6ec1fa5da08c259b741f21dc1026b289b09", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["accessibility", "documents", "presentations", "powerpoint", "quality", "scripts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `accessibility_pass_agent.py` and embedded as the fenced Python below (sha256 87ab5363801dd384…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `accessibility_pass_agent.py` first:

```bash
python3 accessibility_pass_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 accessibility_pass_agent.py   # or on stdin
python3 accessibility_pass_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/accessibility_pass_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/accessibility_pass_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/accessibility_pass/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
