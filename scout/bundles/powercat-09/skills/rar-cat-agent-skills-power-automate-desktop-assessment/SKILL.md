---
name: "rar-cat-agent-skills-power-automate-desktop-assessment"
description: "Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_desktop_assessment", "rar_sha256": "6ff056fe92c6b801457fd674f9e59f20cb8d232458838a03d7506839420897ec", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.2", "author": "Ricardo Calejo", "tags": ["power_automate", "desktop_flows", "automation", "assessment", "governance"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_automate_desktop_assessment_agent.py` and embedded as the fenced Python below (sha256 6ff056fe92c6b801…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_automate_desktop_assessment_agent.py` first:

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
    "version": '3.1.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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
    print(PowerAutomateDesktopAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
