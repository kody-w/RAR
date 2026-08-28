---
name: "rar-cat-agent-skills-power-automate-desktop-assessment"
description: "Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_desktop_assessment", "rar_sha256": "a002ab6df0f13d216069dc399971ecec085e96ce854ee960de87ac043cd8435a", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.1.0", "author": "Ricardo Calejo", "tags": ["power_automate", "desktop_flows", "automation", "assessment", "governance"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/power_automate_desktop_assessment`. The original RAPP
agent is preserved byte-for-byte in `power_automate_desktop_assessment_agent.py` and in the RCI capsule.

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

Power Automate Desktop Assessment — Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-desktop-assessment
  Upstream author: Ricardo Calejo
  Upstream version: 1.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_automate_desktop_assessment_agent.py` and embedded as the fenced Python below (sha256 a002ab6df0f13d21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_automate_desktop_assessment_agent.py` first:

```bash
python3 power_automate_desktop_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_automate_desktop_assessment_agent.py   # or on stdin
python3 power_automate_desktop_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Power Automate Desktop Assessment — Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-desktop-assessment
  Upstream author: Ricardo Calejo
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/power_automate_desktop_assessment',
    "version": '2.1.0',
    "display_name": 'Power Automate Desktop Assessment',
    "description": 'Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance.',
    "author": 'Ricardo Calejo',
    "tags": ['power_automate', 'desktop_flows', 'automation', 'assessment', 'governance'],
    "category": 'analysis',
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
        "upstream_slug": 'power-automate-desktop-assessment',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#power-automate-desktop-assessment',
        "upstream_version": '1.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd026e3d4a8378798',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.333, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance', 'word:assess'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PowerAutomateDesktopAssessment(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PowerAutomateDesktopAssessment'
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
    print(PowerAutomateDesktopAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
