---
name: "rar-cat-agent-skills-linkedin-content-writer"
description: "Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_writer", "rar_sha256": "a6d7fa21211ae1f4b734b11aded5d0278fb3c47fd78e3c763bf630ebaacf691f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Becky Still, Digital Boop Ltd", "tags": ["linkedin", "social_media", "writing", "content"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/linkedin_content_writer`. The original RAPP
agent is preserved byte-for-byte in `linkedin_content_writer_agent.py` and in the RCI capsule.

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

LinkedIn Content Writer — Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer
  Upstream author: Becky Still, Digital Boop Ltd
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `linkedin_content_writer_agent.py` and embedded as the fenced Python below (sha256 a6d7fa21211ae1f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `linkedin_content_writer_agent.py` first:

```bash
python3 linkedin_content_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 linkedin_content_writer_agent.py   # or on stdin
python3 linkedin_content_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/linkedin_content_writer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/linkedin_content_writer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/linkedin_content_writer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
LinkedIn Content Writer — Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer
  Upstream author: Becky Still, Digital Boop Ltd
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/linkedin_content_writer',
    "version": '3.0.3',
    "display_name": 'LinkedIn Content Writer',
    "description": 'Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.',
    "author": 'Becky Still, Digital Boop Ltd',
    "tags": ['linkedin', 'social_media', 'writing', 'content'],
    "category": 'general',
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
        "upstream_slug": 'linkedin-content-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b67b1c225f5d7237',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class LinkedinContentWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LinkedinContentWriter'
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
    print(LinkedinContentWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
