---
name: "rar-cat-agent-skills-wcag-power-platform"
description: "Makes everything the agent builds or reviews conform to WCAG 2.1 AA \u2014 HTML pages, SPAs, theming, PCF controls, model-driven and canvas apps, and Power Pages."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wcag_power_platform", "rar_sha256": "fcd22c913fc835ae83ff41a7ab8e9bd01ea977e290a401462651c622c0ae156c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Mark Christie", "tags": ["accessibility", "wcag", "a11y", "power_platform", "power_apps", "pcf", "power_pages", "web"]}
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
