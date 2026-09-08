---
name: "rar-cat-agent-skills-linkedin-content-system"
description: "Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_system", "rar_sha256": "8f2cf6fa8bde17f9ba6a01d54864ee5b1c02c560ece7c7488862e58cb7a441e7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["linkedin", "social_media", "writing", "marketing", "content"]}
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
