---
name: "rar-cat-agent-skills-linkedin-content-system"
description: "Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_system", "rar_sha256": "8f2cf6fa8bde17f9ba6a01d54864ee5b1c02c560ece7c7488862e58cb7a441e7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["linkedin", "social_media", "writing", "marketing", "content"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/linkedin_content_system`. The original RAPP
agent is preserved byte-for-byte in `linkedin_content_system_agent.py` and in the RCI capsule.

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

LinkedIn Content System — Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-system
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `linkedin_content_system_agent.py` and embedded as the fenced Python below (sha256 8f2cf6fa8bde17f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `linkedin_content_system_agent.py` first:

```bash
python3 linkedin_content_system_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 linkedin_content_system_agent.py   # or on stdin
python3 linkedin_content_system_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
LinkedIn Content System — Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-system
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/linkedin_content_system',
    "version": '2.1.2',
    "display_name": 'LinkedIn Content System',
    "description": 'Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts.',
    "author": 'Simon Owen',
    "tags": ['linkedin', 'social_media', 'writing', 'marketing', 'content'],
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
        "upstream_slug": 'linkedin-content-system',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#linkedin-content-system',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '207c56909d447f78',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class LinkedinContentSystem(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LinkedinContentSystem'
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
    print(LinkedinContentSystem().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
