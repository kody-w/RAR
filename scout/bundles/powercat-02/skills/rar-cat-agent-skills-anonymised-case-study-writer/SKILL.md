---
name: "rar-cat-agent-skills-anonymised-case-study-writer"
description: "Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/anonymised_case_study_writer", "rar_sha256": "49d3b3efccee510686f44a4fed6b95a9b507f706bb3c594d126aa9cda655b398", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "case_study", "marketing", "documents", "content", "privacy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/anonymised_case_study_writer`. The original RAPP
agent is preserved byte-for-byte in `anonymised_case_study_writer_agent.py` and in the RCI capsule.

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

Anonymised Case Study Writer — Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `anonymised_case_study_writer_agent.py` and embedded as the fenced Python below (sha256 49d3b3efccee5106…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `anonymised_case_study_writer_agent.py` first:

```bash
python3 anonymised_case_study_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 anonymised_case_study_writer_agent.py   # or on stdin
python3 anonymised_case_study_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/anonymised_case_study_writer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/anonymised_case_study_writer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/anonymised_case_study_writer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Anonymised Case Study Writer — Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/anonymised_case_study_writer',
    "version": '2.1.2',
    "display_name": 'Anonymised Case Study Writer',
    "description": 'Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.',
    "author": 'Simon Owen',
    "tags": ['writing', 'case_study', 'marketing', 'documents', 'content', 'privacy'],
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
        "upstream_slug": 'anonymised-case-study-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '30ca39e3e8405c3e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.857, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:documents', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AnonymisedCaseStudyWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnonymisedCaseStudyWriter'
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
    print(AnonymisedCaseStudyWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
