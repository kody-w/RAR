---
name: "rar-cat-agent-skills-linkedin-content-writer"
description: "Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_writer", "rar_sha256": "a6d7fa21211ae1f4b734b11aded5d0278fb3c47fd78e3c763bf630ebaacf691f", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.3", "author": "Becky Still, Digital Boop Ltd", "tags": ["linkedin", "social_media", "writing", "content"]}
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
