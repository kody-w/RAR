---
name: "rar-cat-agent-skills-power-automate-documentation"
description: "Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_documentation", "rar_sha256": "db07d9c1a188ccc5657ca62c42bf1782d6716fd9edc11d5efd9ee5c9f9490f30", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "power_automate_documentation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/power-automate-documentation:34c1541d8658fb754e21267d4573885239532e2d1b5dca863e0e9604d8c0d0b4", "kind": "skill"}, "version": "2.0.0", "author": "Mathias Salomonsen", "tags": ["power_automate", "documentation", "audit", "governance"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/power_automate_documentation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `power_automate_documentation_agent.py` is
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

Power Automate Documentation — Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-documentation
  Upstream author: Mathias Salomonsen
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_automate_documentation_agent.py` and embedded as the fenced Python below (sha256 db07d9c1a188ccc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_automate_documentation_agent.py` first:

```bash
python3 power_automate_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_automate_documentation_agent.py   # or on stdin
python3 power_automate_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Power Automate Documentation — Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-documentation
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/power_automate_documentation',
    "version": '2.0.0',
    "display_name": 'Power Automate Documentation',
    "description": 'Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically.',
    "author": 'Mathias Salomonsen',
    "tags": ['power_automate', 'documentation', 'audit', 'governance'],
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
        "upstream_slug": 'power-automate-documentation',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#power-automate-documentation',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4c5eb6e7dd7c2d70',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'tag:governance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PowerAutomateDocumentation(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PowerAutomateDocumentation'
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
    print(PowerAutomateDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
