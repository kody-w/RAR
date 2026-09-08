---
name: "rar-cat-agent-skills-wcag-power-platform"
description: "Makes everything the agent builds or reviews conform to WCAG 2.1 AA \u2014 HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wcag_power_platform", "rar_sha256": "37075dfcfef21add8a31629f5621e192de0f1738315b147f734d0f645cf5dff7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Mark Christie", "tags": ["accessibility", "wcag", "a11y", "power_platform", "power_apps", "pcf", "power_pages", "web"]}
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
