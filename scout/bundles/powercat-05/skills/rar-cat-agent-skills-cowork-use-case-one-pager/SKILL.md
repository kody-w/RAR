---
name: "rar-cat-agent-skills-cowork-use-case-one-pager"
description: "Turn a Cowork conversation, into a one-page HTML use case write-up \u2014 narrative, impact figures, workflow steps, and outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/cowork_use_case_one_pager", "rar_sha256": "ea74002cbb93d2e5d5d336f091b9f4b6d89012e4669548ce3057b6443d09d75f", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.3", "author": "Tim Sparks", "tags": ["productivity", "use_case", "html", "documents", "writing", "audit"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/cowork_use_case_one_pager`. The original RAPP
agent is preserved byte-for-byte in `cowork_use_case_one_pager_agent.py` and in the RCI capsule.

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

Cowork Use Case One-Pager — Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager
  Upstream author: Tim Sparks
  Upstream version: 1.0.1
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `cowork_use_case_one_pager_agent.py` and embedded as the fenced Python below (sha256 ea74002cbb93d2e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `cowork_use_case_one_pager_agent.py` first:

```bash
python3 cowork_use_case_one_pager_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 cowork_use_case_one_pager_agent.py   # or on stdin
python3 cowork_use_case_one_pager_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/cowork_use_case_one_pager_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/cowork_use_case_one_pager_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/cowork_use_case_one_pager/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Cowork Use Case One-Pager — Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager
  Upstream author: Tim Sparks
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/cowork_use_case_one_pager',
    "version": '3.0.3',
    "display_name": 'Cowork Use Case One-Pager',
    "description": 'Turn a Cowork conversation, into a one-page HTML use case write-up — narrative, impact figures, workflow steps, and outputs.',
    "author": 'Tim Sparks',
    "tags": ['productivity', 'use_case', 'html', 'documents', 'writing', 'audit'],
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
        "upstream_slug": 'cowork-use-case-one-pager',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#cowork-use-case-one-pager',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e6c8d90451f0dc94',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.556, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'tag:writing', 'word:write'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CoworkUseCaseOnePager(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CoworkUseCaseOnePager'
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
    print(CoworkUseCaseOnePager().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
