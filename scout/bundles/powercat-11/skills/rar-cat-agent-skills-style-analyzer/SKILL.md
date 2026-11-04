---
name: "rar-cat-agent-skills-style-analyzer"
description: "Analyzes your Teams chats and emails to build a reusable profile of your writing voice \u2014 greetings, tone, length, punctuation, sign-offs, common phrases, and quirks \u2014 and saves it to memory for other assistants to use."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/style_analyzer", "rar_sha256": "1363ed8c46022859bf6dc1a2b7e0d09752f35890797cdc99d9530e2af2965880", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["writing", "style", "teams", "email", "memory", "productivity"]}
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
