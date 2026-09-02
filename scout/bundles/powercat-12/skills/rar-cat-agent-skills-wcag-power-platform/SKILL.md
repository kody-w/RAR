---
name: "rar-cat-agent-skills-wcag-power-platform"
description: "Makes everything the agent builds or reviews conform to WCAG 2.1 AA \u2014 HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wcag_power_platform", "rar_sha256": "64c5ea9482a1d1ada8874099c362a028318cf35ce157fe91e5642f6eebdaf1b5", "source_kind": "rar-agent", "source_commit": "409a3c18c6511b9cbf68a9f6716c5be9715b10c4", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "wcag_power_platform_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/wcag-power-platform:b33a0bf534cce1d48fdc21636e7ee6445307a7971502a14f4f812f84bcc83d9e", "kind": "skill"}, "version": "2.0.0", "author": "Mark Christie", "tags": ["accessibility", "wcag", "a11y", "power_platform", "power_apps", "pcf", "power_pages", "web"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/wcag_power_platform`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `wcag_power_platform_agent.py` is
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

WCAG 2.1 for Web Apps & Power Platform — Makes everything the agent builds or reviews conform to WCAG 2.1 AA — HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wcag-power-platform
  Upstream author: Mark Christie
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wcag_power_platform_agent.py` and embedded as the fenced Python below (sha256 64c5ea9482a1d1ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wcag_power_platform_agent.py` first:

```bash
python3 wcag_power_platform_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wcag_power_platform_agent.py   # or on stdin
python3 wcag_power_platform_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
WCAG 2.1 for Web Apps & Power Platform — Makes everything the agent builds or reviews conform to WCAG 2.1 AA — HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wcag-power-platform
  Upstream author: Mark Christie
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/wcag_power_platform',
    "version": '2.0.0',
    "display_name": 'WCAG 2.1 for Web Apps & Power Platform',
    "description": 'Makes everything the agent builds or reviews conform to WCAG 2.1 AA — HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages.',
    "author": 'Mark Christie',
    "tags": ['accessibility', 'wcag', 'a11y', 'power_platform', 'power_apps', 'pcf', 'power_pages', 'web'],
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
        "upstream_slug": 'wcag-power-platform',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#wcag-power-platform',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'df1198a270713293',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:accessibility'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class WcagPowerPlatform(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WcagPowerPlatform'
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
    print(WcagPowerPlatform().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
