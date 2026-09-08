---
name: "rar-cat-agent-skills-cowork-use-case-one-pager"
description: "Turn a Cowork conversation, into a one-page HTML use case write-up \u2014 narrative, impact figures, workflow steps, and outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/cowork_use_case_one_pager", "rar_sha256": "36fd44a76d80525c9ac4de4a7428e0bc4be342ca07dc8c6c8f1ade0df11a895f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Tim Sparks", "tags": ["productivity", "use_case", "html", "documents", "writing", "audit"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `cowork_use_case_one_pager_agent.py` and embedded as the fenced Python below (sha256 36fd44a76d80525c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `cowork_use_case_one_pager_agent.py` first:

```bash
python3 cowork_use_case_one_pager_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 cowork_use_case_one_pager_agent.py   # or on stdin
python3 cowork_use_case_one_pager_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
