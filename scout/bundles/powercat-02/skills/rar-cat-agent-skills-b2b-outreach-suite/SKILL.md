---
name: "rar-cat-agent-skills-b2b-outreach-suite"
description: "A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/b2b_outreach_suite", "rar_sha256": "dd2ff9fa0279217e4c73141b6680ecc31bb0dcf55b50f43d15f580b82452c119", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Marcel", "tags": ["sales_enablement", "email", "linkedin", "writing", "marketing", "content"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/b2b_outreach_suite`. The original RAPP
agent is preserved byte-for-byte in `b2b_outreach_suite_agent.py` and in the RCI capsule.

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

B2B Outreach Suite — A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#b2b-outreach-suite
  Upstream author: Marcel
  Upstream version: 1.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `b2b_outreach_suite_agent.py` and embedded as the fenced Python below (sha256 dd2ff9fa0279217e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `b2b_outreach_suite_agent.py` first:

```bash
python3 b2b_outreach_suite_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 b2b_outreach_suite_agent.py   # or on stdin
python3 b2b_outreach_suite_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
B2B Outreach Suite — A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#b2b-outreach-suite
  Upstream author: Marcel
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/b2b_outreach_suite',
    "version": '2.0.0',
    "display_name": 'B2B Outreach Suite',
    "description": 'A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language.',
    "author": 'Marcel',
    "tags": ['sales_enablement', 'email', 'linkedin', 'writing', 'marketing', 'content'],
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
        "upstream_slug": 'b2b-outreach-suite',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#b2b-outreach-suite',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b6d141c5052aba20',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.857, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:email', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class B2bOutreachSuite(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'B2bOutreachSuite'
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
    print(B2bOutreachSuite().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
