---
name: "rar-cat-agent-skills-power-automate-desktop-assessment"
description: "Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_desktop_assessment", "rar_sha256": "a002ab6df0f13d216069dc399971ecec085e96ce854ee960de87ac043cd8435a", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "power_automate_desktop_assessment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/power-automate-desktop-assessment:66a70fddee121a0710d00e3e856648cd1300dd6e6153833f7814a7c638609f35", "kind": "skill"}, "version": "2.1.0", "author": "Ricardo Calejo", "tags": ["power_automate", "desktop_flows", "automation", "assessment", "governance"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/power_automate_desktop_assessment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `power_automate_desktop_assessment_agent.py` is
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
