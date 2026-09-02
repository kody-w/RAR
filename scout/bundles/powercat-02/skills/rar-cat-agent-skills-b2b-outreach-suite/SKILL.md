---
name: "rar-cat-agent-skills-b2b-outreach-suite"
description: "A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/b2b_outreach_suite", "rar_sha256": "dd2ff9fa0279217e4c73141b6680ecc31bb0dcf55b50f43d15f580b82452c119", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "b2b_outreach_suite_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/b2b-outreach-suite:1e44b25bc10b98aac8233bf0fc982140889e60a736cfb0c2dd961e28f25ab9a8", "kind": "skill"}, "version": "2.0.0", "author": "Marcel", "tags": ["sales_enablement", "email", "linkedin", "writing", "marketing", "content"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/b2b_outreach_suite`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `b2b_outreach_suite_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
