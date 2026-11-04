---
name: "rar-cat-agent-skills-cowork-use-case-one-pager"
description: "Turn a Cowork conversation, into a one-page HTML use case write-up \u2014 narrative, impact figures, workflow steps, and outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/cowork_use_case_one_pager", "rar_sha256": "ea74002cbb93d2e5d5d336f091b9f4b6d89012e4669548ce3057b6443d09d75f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Tim Sparks", "tags": ["productivity", "use_case", "html", "documents", "writing", "audit"]}
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
