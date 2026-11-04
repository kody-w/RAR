---
name: "rar-cat-agent-skills-style-analyzer"
description: "Analyzes your Teams chats and emails to build a reusable profile of your writing voice \u2014 greetings, tone, length, punctuation, sign-offs, common phrases, and quirks \u2014 and saves it to memory for other assistants to use."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/style_analyzer", "rar_sha256": "1363ed8c46022859bf6dc1a2b7e0d09752f35890797cdc99d9530e2af2965880", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["writing", "style", "teams", "email", "memory", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `style_analyzer_agent.py` and embedded as the fenced Python below (sha256 1363ed8c46022859…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `style_analyzer_agent.py` first:

```bash
python3 style_analyzer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 style_analyzer_agent.py   # or on stdin
python3 style_analyzer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/style_analyzer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/style_analyzer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/style_analyzer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
