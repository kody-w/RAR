---
name: "rar-cat-agent-skills-linkedin-content-system"
description: "Create evidence-led LinkedIn posts, promos, newsletter intros, and long-form copy from supplied facts or drafts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_system", "rar_sha256": "cd5a44eb81ec76324921f288cf231f95096b3a9c67f5a5269038dc5b748eb744", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["linkedin", "social_media", "writing", "marketing", "content"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `linkedin_content_system_agent.py` and embedded as the fenced Python below (sha256 cd5a44eb81ec7632…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `linkedin_content_system_agent.py` first:

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
    "version": '1.1.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
