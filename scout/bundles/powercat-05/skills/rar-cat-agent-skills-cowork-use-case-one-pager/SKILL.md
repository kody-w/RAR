---
name: "rar-cat-agent-skills-cowork-use-case-one-pager"
description: "Turn a Cowork conversation, into a one-page HTML use case write-up \u2014 narrative, impact figures, workflow steps, and outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/cowork_use_case_one_pager", "rar_sha256": "36fd44a76d80525c9ac4de4a7428e0bc4be342ca07dc8c6c8f1ade0df11a895f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Tim Sparks", "tags": ["productivity", "use_case", "html", "documents", "writing", "audit"]}
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
