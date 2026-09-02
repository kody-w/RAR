---
name: "rar-cat-agent-skills-persona-reaction-panel"
description: "Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships \u2014 surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/persona_reaction_panel", "rar_sha256": "471d20b0f203e9a3937b853274583f5028962fe9de6d1da42222cc2b2771bc33", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "persona_reaction_panel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/persona-reaction-panel:90ae0da3532138f9bea4558527e1b60bc6e270dc9d57658ee39d6ddf632e17fe", "kind": "skill"}, "version": "2.0.0", "author": "Olivia Zhang", "tags": ["communications", "change_management", "launch_readiness", "personas", "qa"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/persona_reaction_panel`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `persona_reaction_panel_agent.py` is
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

Persona Reaction Panel — Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships — surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#persona-reaction-panel
  Upstream author: Olivia Zhang
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `persona_reaction_panel_agent.py` and embedded as the fenced Python below (sha256 471d20b0f203e9a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `persona_reaction_panel_agent.py` first:

```bash
python3 persona_reaction_panel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 persona_reaction_panel_agent.py   # or on stdin
python3 persona_reaction_panel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Persona Reaction Panel — Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships — surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#persona-reaction-panel
  Upstream author: Olivia Zhang
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/persona_reaction_panel',
    "version": '2.0.0',
    "display_name": 'Persona Reaction Panel',
    "description": 'Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships — surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file.',
    "author": 'Olivia Zhang',
    "tags": ['communications', 'change_management', 'launch_readiness', 'personas', 'qa'],
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
        "upstream_slug": 'persona-reaction-panel',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#persona-reaction-panel',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd947b7c2da61f3de',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PersonaReactionPanel(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PersonaReactionPanel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(PersonaReactionPanel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
