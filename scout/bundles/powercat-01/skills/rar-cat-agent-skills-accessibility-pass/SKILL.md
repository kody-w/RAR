---
name: "rar-cat-agent-skills-accessibility-pass"
description: "Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/accessibility_pass", "rar_sha256": "87ab5363801dd38441801dd9d3cfc6ec1fa5da08c259b741f21dc1026b289b09", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["accessibility", "documents", "presentations", "powerpoint", "quality", "scripts"]}
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
