---
name: "rar-cat-agent-skills-persona-reaction-panel"
description: "Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships \u2014 surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/persona_reaction_panel", "rar_sha256": "471d20b0f203e9a3937b853274583f5028962fe9de6d1da42222cc2b2771bc33", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Olivia Zhang", "tags": ["communications", "change_management", "launch_readiness", "personas", "qa"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/persona_reaction_panel`. The original RAPP
agent is preserved byte-for-byte in `persona_reaction_panel_agent.py` and in the RCI capsule.

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
