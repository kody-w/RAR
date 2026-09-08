---
name: "rar-cat-agent-skills-wcag-power-platform"
description: "Makes everything the agent builds or reviews conform to WCAG 2.1 AA \u2014 HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wcag_power_platform", "rar_sha256": "37075dfcfef21add8a31629f5621e192de0f1738315b147f734d0f645cf5dff7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Mark Christie", "tags": ["accessibility", "wcag", "a11y", "power_platform", "power_apps", "pcf", "power_pages", "web"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wcag_power_platform_agent.py` and embedded as the fenced Python below (sha256 37075dfcfef21add…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wcag_power_platform_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
