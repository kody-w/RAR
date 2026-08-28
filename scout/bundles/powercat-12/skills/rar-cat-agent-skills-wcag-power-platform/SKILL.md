---
name: "rar-cat-agent-skills-wcag-power-platform"
description: "Makes everything the agent builds or reviews conform to WCAG 2.1 AA \u2014 HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wcag_power_platform", "rar_sha256": "64c5ea9482a1d1ada8874099c362a028318cf35ce157fe91e5642f6eebdaf1b5", "source_kind": "rar-agent", "source_commit": "409a3c18c6511b9cbf68a9f6716c5be9715b10c4", "version": "2.0.0", "author": "Mark Christie", "tags": ["accessibility", "wcag", "a11y", "power_platform", "power_apps", "pcf", "power_pages", "web"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/wcag_power_platform`. The original RAPP
agent is preserved byte-for-byte in `wcag_power_platform_agent.py` and in the RCI capsule.

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
