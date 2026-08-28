---
name: "rar-cat-agent-skills-power-automate-documentation"
description: "Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_documentation", "rar_sha256": "db07d9c1a188ccc5657ca62c42bf1782d6716fd9edc11d5efd9ee5c9f9490f30", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Mathias Salomonsen", "tags": ["power_automate", "documentation", "audit", "governance"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/power_automate_documentation`. The original RAPP
agent is preserved byte-for-byte in `power_automate_documentation_agent.py` and in the RCI capsule.

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
