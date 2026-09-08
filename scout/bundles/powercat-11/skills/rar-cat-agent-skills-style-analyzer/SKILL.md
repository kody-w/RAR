---
name: "rar-cat-agent-skills-style-analyzer"
description: "Analyzes your Teams chats and emails to build a reusable profile of your writing voice \u2014 greetings, tone, length, punctuation, sign-offs, common phrases, and quirks \u2014 and saves it to memory for other assistants to use."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/style_analyzer", "rar_sha256": "640028ca7ac28a8544a35fd8371ecdd351608fe501ca4b59525f116e1e3c0b7c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["writing", "style", "teams", "email", "memory", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/style_analyzer`. The original RAPP
agent is preserved byte-for-byte in `style_analyzer_agent.py` and in the RCI capsule.

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

Communication Style Analyzer — Analyzes your Teams chats and emails to build a reusable profile of your writing voice — greetings, tone, length, punctuation, sign-offs, common phrases, and quirks — and saves it to memory for other assistants to use.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#style-analyzer
  Upstream author: Srinivas Varukala
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `style_analyzer_agent.py` and embedded as the fenced Python below (sha256 640028ca7ac28a85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `style_analyzer_agent.py` first:

```bash
python3 style_analyzer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 style_analyzer_agent.py   # or on stdin
python3 style_analyzer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Communication Style Analyzer — Analyzes your Teams chats and emails to build a reusable profile of your writing voice — greetings, tone, length, punctuation, sign-offs, common phrases, and quirks — and saves it to memory for other assistants to use.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#style-analyzer
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/style_analyzer',
    "version": '3.0.2',
    "display_name": 'Communication Style Analyzer',
    "description": 'Analyzes your Teams chats and emails to build a reusable profile of your writing voice — greetings, tone, length, punctuation, sign-offs, common phrases, and quirks — and saves it to memory for other assistants to use.',
    "author": 'Srinivas Varukala',
    "tags": ['writing', 'style', 'teams', 'email', 'memory', 'productivity'],
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
        "upstream_slug": 'style-analyzer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#style-analyzer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e5e6f66aa29bdddf',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class StyleAnalyzer(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StyleAnalyzer'
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
    print(StyleAnalyzer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
