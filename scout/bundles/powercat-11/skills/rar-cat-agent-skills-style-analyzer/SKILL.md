---
name: "rar-cat-agent-skills-style-analyzer"
description: "Analyzes your Teams chats and emails to build a reusable profile of your writing voice \u2014 greetings, tone, length, punctuation, sign-offs, common phrases, and quirks \u2014 and saves it to memory for other assistants to use."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/style_analyzer", "rar_sha256": "640028ca7ac28a8544a35fd8371ecdd351608fe501ca4b59525f116e1e3c0b7c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["writing", "style", "teams", "email", "memory", "productivity"]}
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
