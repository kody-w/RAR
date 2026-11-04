---
name: "rar-cat-agent-skills-wcag-power-platform"
description: "Makes everything the agent builds or reviews conform to WCAG 2.1 AA \u2014 HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wcag_power_platform", "rar_sha256": "fcd22c913fc835ae83ff41a7ab8e9bd01ea977e290a401462651c622c0ae156c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Mark Christie", "tags": ["accessibility", "wcag", "a11y", "power_platform", "power_apps", "pcf", "power_pages", "web"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wcag_power_platform_agent.py` and embedded as the fenced Python below (sha256 fcd22c913fc835ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wcag_power_platform_agent.py` first:

```bash
python3 wcag_power_platform_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wcag_power_platform_agent.py   # or on stdin
python3 wcag_power_platform_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/wcag_power_platform_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/wcag_power_platform_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/wcag_power_platform/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
